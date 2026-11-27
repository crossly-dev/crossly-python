"""Run the shared vectors against the Python port."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from crossly_webhooks import verify_webhook, WebhookVerificationError

data = json.loads((pathlib.Path(__file__).parent.parent / "test-vectors.json").read_text(encoding="utf-8"))
tol = data["toleranceSeconds"]
ok = bad = 0
for v in data["vectors"]:
    try:
        verify_webhook(v["body"], v["header"], v["secret"], tolerance_seconds=tol, now=v["now"])
        got = "ok"
    except WebhookVerificationError as e:
        got = e.reason
    except Exception as e:  # noqa: BLE001 — any other throw is itself a failure
        got = f"threw:{type(e).__name__}"
    if got == v["expect"]:
        ok += 1
    else:
        bad += 1
        print(f"  MISMATCH {v['name']}: expected {v['expect']}, got {got}")
print(f"  python: {ok}/{len(data['vectors'])} vectors agree")
sys.exit(1 if bad else 0)
