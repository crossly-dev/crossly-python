#!/usr/bin/env node
/**
 * Move freshly generated clients into the repo and scan them.
 *
 *   node codegen/ci/assemble.mjs        (after codegen/scripts/generate-sdks.mjs --lang <lang>)
 *
 * codegen/sdks/<lang>/{seller,buyer,webhooks} REPLACE the repo's seller/, buyer/ and webhooks/ (replaced, not
 * merged: a file for a route that no longer exists is a method that 404s). Then each entry of codegen/repo.json's
 * `vendorWebhooks` copies the hand-written verifier INTO an installable package, so `pip install crossly` (etc.)
 * can verify a webhook without copying files from this repo, and the copy is checked byte-identical to the
 * conformance-tested source. Last, the forbidden-pattern scan: generated code is still code, and a spec that ever
 * carried a token would bake it into every client at once. Exit 1 on a hit.
 */
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { auditFiles } from '../scripts/mirror-forbidden.mjs';

const CODEGEN = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const REPO = resolve(CODEGEN, '..');
const repo = JSON.parse(readFileSync(join(CODEGEN, 'repo.json'), 'utf8'));
const out = join(CODEGEN, 'sdks', repo.lang);

for (const part of ['seller', 'buyer']) {
  if (!existsSync(join(out, part))) {
    console.error(`${out}/${part} is missing: generation failed, refusing to assemble half a repo`);
    process.exit(1);
  }
}
for (const part of ['seller', 'buyer', 'webhooks']) {
  rmSync(join(REPO, part), { recursive: true, force: true });
  if (existsSync(join(out, part))) cpSync(join(out, part), join(REPO, part), { recursive: true });
}

const source = join(CODEGEN, 'integrations', 'webhooks', repo.lang);
for (const v of repo.vendorWebhooks ?? []) {
  const from = join(source, v.from);
  const to = join(REPO, v.to);
  if (!existsSync(dirname(to))) {
    console.error(`vendorWebhooks: ${dirname(v.to)} does not exist in the generated client (did the package name change?)`);
    process.exit(1);
  }
  mkdirSync(dirname(to), { recursive: true });
  cpSync(from, to);
  if (!readFileSync(from).equals(readFileSync(to))) {
    console.error(`vendorWebhooks: ${v.to} is not identical to ${v.from}`);
    process.exit(1);
  }
  console.log(`webhook verifier -> ${v.to}`);
}

const walk = (d) =>
  readdirSync(d, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? walk(join(d, e.name)) : [join(d, e.name)]));
const files = ['seller', 'buyer', 'webhooks']
  .filter((p) => existsSync(join(REPO, p)))
  .flatMap((p) => walk(join(REPO, p)))
  .map((f) => relative(REPO, f));
const hits = auditFiles(REPO, files);
console.log(`${repo.lang}: ${files.length} files, ${hits.length} forbidden-pattern finding(s)`);
for (const h of hits) console.log(`  !! ${h.file}: ${h.name} (${h.sample})`);
process.exit(hits.length ? 1 : 0);
