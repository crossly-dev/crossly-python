# crossly.WorldApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spatial_invite_accept**](WorldApi.md#create_spatial_invite_accept) | **POST** /v1/spatial/invites/accept | Redeem an invite code (dashes optional); returns the room it opens.
[**create_spatial_property_lease_withdraw**](WorldApi.md#create_spatial_property_lease_withdraw) | **POST** /v1/spatial/property/leases/{id}/withdraw | Withdraw a lease offer nobody has accepted yet.
[**create_spatial_scene**](WorldApi.md#create_spatial_scene) | **POST** /v1/spatial/scenes | Start a 3D room: a collection (your items on shelves) or a warehouse (racks you arrange). Private until you make it public.
[**create_spatial_scene_grant**](WorldApi.md#create_spatial_scene_grant) | **POST** /v1/spatial/scenes/{id}/grants | Let a specific user into one of your rooms (visitor or staff), no code needed.
[**create_spatial_scene_invite**](WorldApi.md#create_spatial_scene_invite) | **POST** /v1/spatial/scenes/{id}/invites | Mint an invite code to one of your rooms (visitor or staff, optional expiry in hours). The code is in this response only: just its hash is stored.
[**create_spatial_scene_node**](WorldApi.md#create_spatial_scene_node) | **POST** /v1/spatial/scenes/{id}/nodes | Add a unit (rack, shelf, bin) to one of your warehouse rooms.
[**create_spatial_scene_place**](WorldApi.md#create_spatial_scene_place) | **POST** /v1/spatial/scenes/{id}/place | Pin an inventory item to a slot in one of your rooms: by warehouse nodeId, or by a collection container key and index.
[**create_spatial_scene_rename**](WorldApi.md#create_spatial_scene_rename) | **POST** /v1/spatial/scenes/{id}/rename | Rename one of your rooms.
[**create_spatial_scene_shop_place**](WorldApi.md#create_spatial_scene_shop_place) | **POST** /v1/spatial/scenes/{id}/shop/place | Place an inventory item in a section and display of your shop room.
[**create_spatial_scene_unpin**](WorldApi.md#create_spatial_scene_unpin) | **POST** /v1/spatial/scenes/{id}/unpin | Clear every pin in one of your rooms, so it arranges itself again.
[**create_spatial_scene_visibility**](WorldApi.md#create_spatial_scene_visibility) | **POST** /v1/spatial/scenes/{id}/visibility | Make one of your rooms private, unlisted (anyone with the link) or public (in the lobby and searchable).
[**create_spatial_scene_warehouse_stock**](WorldApi.md#create_spatial_scene_warehouse_stock) | **POST** /v1/spatial/scenes/{id}/warehouse/stock | Put an inventory item (or unit) on a rack in one of your warehouse rooms.
[**create_spatial_shop_neighbourhood**](WorldApi.md#create_spatial_shop_neighbourhood) | **POST** /v1/spatial/shop/neighbourhood | Move your shop to another neighbourhood (by slug).
[**create_spatial_street_apply**](WorldApi.md#create_spatial_street_apply) | **POST** /v1/spatial/streets/{slug}/apply | Ask to open your shop on a street whose owner reviews applications.
[**create_spatial_street_invite**](WorldApi.md#create_spatial_street_invite) | **POST** /v1/spatial/streets/{slug}/invite | Invite a shop (by its slug) to open on a street you own.
[**create_world_avatar_equip**](WorldApi.md#create_world_avatar_equip) | **POST** /v1/world/avatar/equip | Wear something you already own -- exactly ONE of { cosmeticId } (a cosmetic you hold), { receiptId } (a Crossly purchase from your closet) or { inventoryItemId } (your own stock). The slot comes from the thing itself; slot is only a fallback for an item with no catalog shape. Replaces whatever was in that slot. Moves no money. Answers the slot and your loadout after the change.
[**create_world_avatar_unequip**](WorldApi.md#create_world_avatar_unequip) | **POST** /v1/world/avatar/unequip | Take off whatever is in one slot. Idempotent: an empty slot answers removed:false. Answers your loadout after the change.
[**create_world_avatar_wearable**](WorldApi.md#create_world_avatar_wearable) | **POST** /v1/world/avatar/wearables | Author a wearable for a body slot (a mesh profile and params, an asking price in COSM base units as a string). A submission: inactive until an operator approves it.
[**create_world_contest**](WorldApi.md#create_world_contest) | **POST** /v1/world/contests | Set up a skill contest on a game placed in your place: title, game (its instance id), entry { mode, feeCents? }, prizes by place, funder, window, attempts. Paid entry needs the operator to allow it where it runs.
[**create_world_contest_entry_settle_payment**](WorldApi.md#create_world_contest_entry_settle_payment) | **POST** /v1/world/contests/entries/{id}/settle-payment | Read the fee of a paid entry back from Stripe and settle it (safe to repeat).
[**create_world_contest_join**](WorldApi.md#create_world_contest_join) | **POST** /v1/world/contests/{id}/join | Enter a contest. Free and sponsored contests take you in at once; a paid one answers a client secret to pay the entry fee.
[**create_world_convention**](WorldApi.md#create_world_convention) | **POST** /v1/world/conventions | Host a convention in one of your rooms: title, dates, tables and how sellers get one (invite, free, a fee in cents, or a revenue share in basis points).
[**create_world_convention_accept**](WorldApi.md#create_world_convention_accept) | **POST** /v1/world/conventions/{id}/accept | Accept: your own invitation (no body), or, as host, an application (username).
[**create_world_convention_apply**](WorldApi.md#create_world_convention_apply) | **POST** /v1/world/conventions/{id}/apply | Ask for a table at a convention.
[**create_world_convention_invite**](WorldApi.md#create_world_convention_invite) | **POST** /v1/world/conventions/{id}/invite | Invite a seller (by shop handle) to a convention you host.
[**create_world_convention_paid**](WorldApi.md#create_world_convention_paid) | **POST** /v1/world/conventions/{id}/paid | As host, record that a seller (username) paid their table fee off-platform. Moves no money.
[**create_world_convention_withdraw**](WorldApi.md#create_world_convention_withdraw) | **POST** /v1/world/conventions/{id}/withdraw | Withdraw your table or decline your invitation; as host, decline someone (username).
[**create_world_crew**](WorldApi.md#create_world_crew) | **POST** /v1/world/crews | Start a crew you own: { name (2-32 chars), tag (2-5 letters or digits, shown on members&#39; nameplates) }. Answers its id and join code. 409 when you are already in a crew.
[**create_world_crew_chat**](WorldApi.md#create_world_crew_chat) | **POST** /v1/world/crew/chat | Say a line to your crew (body: text, up to 400 characters). Returns data.messages, the crew chat ring (the last 50 lines, kept in memory only), and data.said when your line went out; a blocked or too-quick line is dropped silently. 404 when you are in no crew.
[**create_world_crew_join**](WorldApi.md#create_world_crew_join) | **POST** /v1/world/crews/join | Join a crew by the code a member gave you. 404 for an unknown code, 409 when you are already in a crew or it is full (30).
[**create_world_crew_leave**](WorldApi.md#create_world_crew_leave) | **POST** /v1/world/crews/leave | Leave your crew. If you own it, the crew is disbanded. Idempotent: leaving when in none succeeds.
[**create_world_decor_design**](WorldApi.md#create_world_decor_design) | **POST** /v1/world/decor/designs | Author a decor design (what it unlocks, a mesh profile and params, an asking price in COSM base units as a string). Inactive until an operator approves it.
[**create_world_decor_design_submit**](WorldApi.md#create_world_decor_design_submit) | **POST** /v1/world/decor/designs/{id}/submit | Send one of your decor designs to the review queue.
[**create_world_decor_retract**](WorldApi.md#create_world_decor_retract) | **POST** /v1/world/decor/retract | Take a placed decor piece back into your inventory; answers the inventory after.
[**create_world_dm**](WorldApi.md#create_world_dm) | **POST** /v1/world/dms/{userId} | Send a direct message to a friend (a mutual follow; never across a block), up to 400 characters, through the world chat guard. 403 when they are not a friend, 429 when sent too quickly.
[**create_world_follow**](WorldApi.md#create_world_follow) | **POST** /v1/world/follows/{userId} | Follow somebody. When they follow you back you are friends (friends-here, invites, messages). Idempotent.
[**create_world_friend_invite**](WorldApi.md#create_world_friend_invite) | **POST** /v1/world/friends/{userId}/invite | \&quot;Join me\&quot;: send one friend (a mutual follow) a notification with a link to the PUBLIC room you name by slug. 404 when they are not a friend or the room is not public; 429 when you invited them in the last minute.
[**create_world_game_package**](WorldApi.md#create_world_game_package) | **POST** /v1/world/games/packages | Submit a game package version for review: files as { path, base64 } (game.json, thumb.png, logic/, scene/, audio/, images/). Checked like the CLI, assets quarantined, the entry document dry-run, then reviewed by a person.
[**create_world_game_package_check**](WorldApi.md#create_world_game_package_check) | **POST** /v1/world/games/packages/check | Validate a game package exactly as a submission is checked (the shared intake report, your version still free) without storing, uploading or queuing anything: world-kit validate for an agent. Same files body as submit.
[**create_world_game_rating**](WorldApi.md#create_world_game_rating) | **POST** /v1/world/games/{id}/rating | Rate a game you played, 1 to 5 stars (rating again replaces it). Only players the runner recorded in that game can rate it.
[**create_world_game_report**](WorldApi.md#create_world_game_report) | **POST** /v1/world/games/{id}/report | Report a game: reason broken | unfair | offensive | scam | other, optional detail. Staff review it; the creator is told the reason, never who.
[**create_world_game_store_checkout**](WorldApi.md#create_world_game_store_checkout) | **POST** /v1/world/games/{id}/store/{item}/checkout | Buy an item or pass from a game store: answers a client secret for the payment; the item is yours once it succeeds.
[**create_world_grail_match**](WorldApi.md#create_world_grail_match) | **POST** /v1/world/grails/match | Grail glints: send the ids on show somewhere (listingIds -- listings.id, inventoryIds, skuIds -- catalogue market SKUs; up to 400 each) and get back data.listingIds / data.inventoryIds / data.skuIds: the ones that are things you already want -- an open bid, a watched or wishlisted listing (or one selling the same SKU), a market watch, or a card your deck is missing. Read-only.
[**create_world_hall_loan**](WorldApi.md#create_world_hall_loan) | **POST** /v1/world/hall/loans | Lend a piece from your vault to this week&#39;s Hall of Grails exhibition: { vaultItemId, credit: &#39;name&#39; | &#39;anonymous&#39; }. It shows under your plaque until the exhibition ends; it stays in your vault (still listable and withdrawable), and stops showing if it leaves.
[**create_world_home_ask**](WorldApi.md#create_world_home_ask) | **POST** /v1/world/homes/{slug}/ask | Ask a home owner whether they would sell a piece you saw there (an item or a decor piece).
[**create_world_home_guestbook**](WorldApi.md#create_world_home_guestbook) | **POST** /v1/world/homes/{slug}/guestbook | Sign a home guestbook (one short line).
[**create_world_home_guestbook_report**](WorldApi.md#create_world_home_guestbook_report) | **POST** /v1/world/homes/{slug}/guestbook/{id}/report | Report a guestbook entry to moderation.
[**create_world_hunt_start**](WorldApi.md#create_world_hunt_start) | **POST** /v1/world/hunt/start | Start the Great Hunt this season by reading its first riddle (the Copper key&#39;s). Idempotent: starting again answers your progress unchanged. Answers the same shape as GET /v1/world/hunt. 409 when no season is running.
[**create_world_interactive_asset**](WorldApi.md#create_world_interactive_asset) | **POST** /v1/world/interactive/assets | Upload one asset for your designs: kind glb (4 MB), wav (4 MB) or png (1 MB), the file as base64. Answers its sha256 and the path to reference from MML.
[**create_world_interactive_design**](WorldApi.md#create_world_interactive_design) | **POST** /v1/world/interactive/designs | Create an interactive design: name, footprint (s, m, l or f), optional tint and description, an asking price in COSM base units (a string, six decimals) and optional max supply. Inactive until ops approve a submitted version.
[**create_world_interactive_design_check**](WorldApi.md#create_world_interactive_design_check) | **POST** /v1/world/interactive/designs/{id}/check | Check the draft: static rules, that every referenced upload exists, and a sandboxed dry run. Budgeted per person.
[**create_world_interactive_design_preview**](WorldApi.md#create_world_interactive_design_preview) | **POST** /v1/world/interactive/designs/{id}/preview | A private preview token for the draft (author only) and the socket path that runs it. Budgeted per person.
[**create_world_interactive_design_submit**](WorldApi.md#create_world_interactive_design_submit) | **POST** /v1/world/interactive/designs/{id}/submit | Freeze the draft as a new version and send it to ops review. Up to 10 a day.
[**create_world_interactive_reset**](WorldApi.md#create_world_interactive_reset) | **POST** /v1/world/interactive/reset | Wipe the stored state of an interactive piece standing in a place you own (a home or your boutique).
[**create_world_job_appraisal_answer**](WorldApi.md#create_world_job_appraisal_answer) | **POST** /v1/world/jobs/appraisals/{id}/answers | Answer a price check: your estimate of the item value in CENTS and an optional note. Moves no money; the asker may accept it.
[**create_world_job_shift_claim**](WorldApi.md#create_world_job_shift_claim) | **POST** /v1/world/jobs/shifts/{id}/claim | Claim an open shift. You work it by being in the place while it runs.
[**create_world_job_shift_release**](WorldApi.md#create_world_job_shift_release) | **POST** /v1/world/jobs/shifts/{id}/release | Give a shift you claimed back to the board.
[**create_world_outfit**](WorldApi.md#create_world_outfit) | **POST** /v1/world/outfits | Save what you are wearing now as a named look: { name (1-32 chars), appearance? (skin, hair, hairColour, eyes, build -- unknown keys fall back to the default) }. Each worn thing is recorded as the door it goes back on by; one that no longer traces to something you own is listed in skipped and not saved. 409 when you already keep 6.
[**create_world_outfit_apply**](WorldApi.md#create_world_outfit_apply) | **POST** /v1/world/outfits/{id}/apply | Put a saved look on. Every item goes through the same equip as POST /v1/world/avatar/equip, so ownership still holds: something you no longer own is listed in skipped with the reason and not worn. Slots the look left empty are emptied (cleared). Answers the appearance of the look (for your character -- appearance lives on your device), applied, skipped and cleared. Moves no money.
[**create_world_party**](WorldApi.md#create_world_party) | **POST** /v1/world/parties | Start a party with you as leader (up to 8 members).
[**create_world_party_chat**](WorldApi.md#create_world_party_chat) | **POST** /v1/world/parties/{id}/chat | Say something in your party chat (up to 2000 characters).
[**create_world_party_invite**](WorldApi.md#create_world_party_invite) | **POST** /v1/world/parties/{id}/invite | Invite a friend (userId) to your party.
[**create_world_party_invite_accept**](WorldApi.md#create_world_party_invite_accept) | **POST** /v1/world/parties/invites/{inviteId}/accept | Accept a party invite.
[**create_world_party_invite_decline**](WorldApi.md#create_world_party_invite_decline) | **POST** /v1/world/parties/invites/{inviteId}/decline | Decline a party invite.
[**create_world_party_kick**](WorldApi.md#create_world_party_kick) | **POST** /v1/world/parties/{id}/kick | As leader, remove a member (userId).
[**create_world_party_leader**](WorldApi.md#create_world_party_leader) | **POST** /v1/world/parties/{id}/leader | As leader, pass the lead to a member (userId).
[**create_world_party_leave**](WorldApi.md#create_world_party_leave) | **POST** /v1/world/parties/{id}/leave | Leave your party (the lead passes on if you led it).
[**create_world_party_wishlist**](WorldApi.md#create_world_party_wishlist) | **POST** /v1/world/parties/{id}/wishlist | Add a listing (listingId, or its shop slug) to the party wishlist; answers the wishlist.
[**create_world_party_wishlist_vote**](WorldApi.md#create_world_party_wishlist_vote) | **POST** /v1/world/parties/{id}/wishlist/{listingId}/vote | Thumb a wishlist listing up or down (null clears your vote); answers the wishlist.
[**create_world_place_item_want**](WorldApi.md#create_world_place_item_want) | **POST** /v1/world/places/{slug}/items/{itemId}/want | Tell a room owner you would buy one of their items (once per person per item; they see the count). Moves no money.
[**create_world_space**](WorldApi.md#create_world_space) | **POST** /v1/world/spaces | Open a Space (sellers only, at most two): slug, name, venue, optional membership and about.
[**create_world_space_event**](WorldApi.md#create_world_space_event) | **POST** /v1/world/spaces/{slug}/events | As host or co-host, put an event on: title, kind, optional about, ISO start and end with offset.
[**create_world_space_event_rsvp**](WorldApi.md#create_world_space_event_rsvp) | **POST** /v1/world/spaces/{slug}/events/{id}/rsvp | Say whether you are going to an event.
[**create_world_space_invite**](WorldApi.md#create_world_space_invite) | **POST** /v1/world/spaces/{slug}/invite | Invite somebody (userId) to a Space.
[**create_world_space_join**](WorldApi.md#create_world_space_join) | **POST** /v1/world/spaces/{slug}/join | Join a Space, or ask to when it is request-only.
[**create_world_space_leave**](WorldApi.md#create_world_space_leave) | **POST** /v1/world/spaces/{slug}/leave | Leave a Space.
[**create_world_space_request_by_user_id**](WorldApi.md#create_world_space_request_by_user_id) | **POST** /v1/world/spaces/{slug}/requests/{userId} | As host or co-host, accept or turn down a request to join.
[**create_world_space_role**](WorldApi.md#create_world_space_role) | **POST** /v1/world/spaces/{slug}/role | As host, make a member a co-host or back to a member.
[**delete_spatial_scene_grant**](WorldApi.md#delete_spatial_scene_grant) | **DELETE** /v1/spatial/scenes/{id}/grants/{grantId} | Take somebody&#39;s access to your room away, or kill an invite nobody has used yet.
[**delete_spatial_scene_node**](WorldApi.md#delete_spatial_scene_node) | **DELETE** /v1/spatial/scenes/{id}/nodes | Remove units (by id, up to 500) from one of your warehouse rooms.
[**delete_spatial_scene_warehouse_stock**](WorldApi.md#delete_spatial_scene_warehouse_stock) | **DELETE** /v1/spatial/scenes/{id}/warehouse/stock | Take an inventory item (or unit) off its rack.
[**delete_spatial_street_request**](WorldApi.md#delete_spatial_street_request) | **DELETE** /v1/spatial/streets/requests/{id} | Withdraw a street request you made that has not been founded yet.
[**delete_world_block**](WorldApi.md#delete_world_block) | **DELETE** /v1/world/blocks/{id} | Unblock somebody (by the block id from GET /v1/world/blocks).
[**delete_world_collection_capability**](WorldApi.md#delete_world_collection_capability) | **DELETE** /v1/world/collections/{chain}/{contract}/capabilities | Withdraw your declaration for a collection.
[**delete_world_follow**](WorldApi.md#delete_world_follow) | **DELETE** /v1/world/follows/{userId} | Unfollow somebody. Idempotent.
[**delete_world_hall_loan**](WorldApi.md#delete_world_hall_loan) | **DELETE** /v1/world/hall/loans/{id} | Take one of your loans off show in the Hall of Grails.
[**delete_world_home_guestbook**](WorldApi.md#delete_world_home_guestbook) | **DELETE** /v1/world/homes/{slug}/guestbook/{id} | As the home owner, hide a guestbook entry.
[**delete_world_interactive_design**](WorldApi.md#delete_world_interactive_design) | **DELETE** /v1/world/interactive/designs/{id} | Delete a draft design, or archive a submitted one (off sale; owned copies keep working).
[**delete_world_job_shift**](WorldApi.md#delete_world_job_shift) | **DELETE** /v1/world/jobs/shifts/{id} | Cancel a shift you posted that nobody has worked yet.
[**delete_world_outfit**](WorldApi.md#delete_world_outfit) | **DELETE** /v1/world/outfits/{id} | Delete a saved look. 404 when it is not yours.
[**delete_world_party_wishlist**](WorldApi.md#delete_world_party_wishlist) | **DELETE** /v1/world/parties/{id}/wishlist/{listingId} | Take a listing you added off the party wishlist; answers the wishlist.
[**delete_world_place_ban**](WorldApi.md#delete_world_place_ban) | **DELETE** /v1/world/places/{slug}/bans/{userId} | Lift a ban from a place you own; they can walk in again right away.
[**delete_world_space**](WorldApi.md#delete_world_space) | **DELETE** /v1/world/spaces/{slug} | As host, close a Space.
[**delete_world_space_event**](WorldApi.md#delete_world_space_event) | **DELETE** /v1/world/spaces/{slug}/events/{id} | As host or co-host, cancel an event.
[**get_spatial_scene_attention**](WorldApi.md#get_spatial_scene_attention) | **GET** /v1/spatial/scenes/{sceneId}/attention | What visitors looked at in one of your rooms: viewers, looks, inspects and dwell per item over the last days (1-35, default 30).
[**get_spatial_scene_window**](WorldApi.md#get_spatial_scene_window) | **GET** /v1/spatial/scenes/{id}/window | The listings you chose for the street window of your shop, in slot order (left, middle, right; empty &#x3D; newest first), and &#x60;choices&#x60;: your listings that can go in it, newest first.
[**get_spatial_shop_neighbourhood**](WorldApi.md#get_spatial_shop_neighbourhood) | **GET** /v1/spatial/shop/neighbourhood | Your shop&#39;s neighbourhood, and whether and where it may move.
[**get_spatial_space**](WorldApi.md#get_spatial_space) | **GET** /v1/spatial/spaces | The room catalogue: every space profile (what it holds, how it is sorted, its containers) and the warehouse units.
[**get_spatial_street_admission**](WorldApi.md#get_spatial_street_admission) | **GET** /v1/spatial/streets/admissions | Street applications and invitations: yours, and those waiting on streets you own.
[**get_spatial_street_decor**](WorldApi.md#get_spatial_street_decor) | **GET** /v1/spatial/streets/{slug}/decor | The decor on a street you may dress, and what you can place.
[**get_world_arcade**](WorldApi.md#get_world_arcade) | **GET** /v1/world/arcade | The Arcade in Crossly World: data.cabinets (slot, where it stands, host -- piece, price_guess or empty --, game, title, blurb, the piece it hosts and where, record, packageId and thumbnail for a creator game from the Game Directory, players) and data.scores (the High Score wall: per game a title, kind -- leaderboard, record or top -- and up to five ASCII lines; a name shows only for somebody who chose to be seen by name, everyone else is \&quot;A player\&quot;), plus creatorGames (creator games with a cabinet now). Games are played in the world.
[**get_world_aurora**](WorldApi.md#get_world_aurora) | **GET** /v1/world/aurora | The Sales Aurora over the Commons in Crossly World: every real sale on Crossly in the last data.windowDays (30) days. data.total (sales in the window), data.families (key, label, colour, count per colour family: cards, coins, jewellery, electronics, media, fashion, toys, other) and data.sales (newest first, at most 48: family, ageHours, fresh -- sold in the last ten minutes, which shimmers). Aggregate only: no item, price, seller or platform. data.updatedAt is when it was read.
[**get_world_auto_shop**](WorldApi.md#get_world_auto_shop) | **GET** /v1/world/auto-shop | Whether Crossly keeps a world shop for you automatically: enabled, and the shop (id, name, visibility, autoCreated, address, label) or null. Change it with PATCH /v1/world/auto-shop.
[**get_world_avatar_identity**](WorldApi.md#get_world_avatar_identity) | **GET** /v1/world/avatar/identity | Whether others see your name in the world (named), or not (anonymous); null if you have never chosen.
[**get_world_avatar_loadout**](WorldApi.md#get_world_avatar_loadout) | **GET** /v1/world/avatar/loadout | What you are wearing: the rig, its slots (avatar_head, avatar_body, avatar_outer -- a jacket over the top, avatar_legs, avatar_feet, avatar_back) and each worn entry -- a cosmetic or a real item -- with its verified-purchase mark. Carries no price, receipt id, seller or order.
[**get_world_avatar_loadout_by_user_id**](WorldApi.md#get_world_avatar_loadout_by_user_id) | **GET** /v1/world/avatar/loadout/{userId} | What somebody else is wearing, with the verified-purchase mark on each real item -- public on purpose, since a check only its owner can see is not a check. No price, receipt id, seller or order.
[**get_world_avatar_look**](WorldApi.md#get_world_avatar_look) | **GET** /v1/world/avatar/look | Your world look on the account: the handle you chose (null if anonymous) and your appearance; null if you never made one.
[**get_world_avatar_nft_badge**](WorldApi.md#get_world_avatar_nft_badge) | **GET** /v1/world/avatar/nft-badge | The NFT you wear on your nameplate in the world, or null.
[**get_world_capability**](WorldApi.md#get_world_capability) | **GET** /v1/world/capabilities | What your held NFTs unlock in Crossly World: each token with the capabilities its collection declared (wear, display, emote, gate, ...). Holding is your verified wallets (their synced tokens); the capabilities of a transferred token go within five minutes.
[**get_world_capability_catalogue**](WorldApi.md#get_world_capability_catalogue) | **GET** /v1/world/capabilities/catalogue | The capability kinds of spec crossly.nft-capabilities/1: what each does, whether only the creator of the collection may declare it, whether it needs review, and which clients honour it.
[**get_world_capability_wear**](WorldApi.md#get_world_capability_wear) | **GET** /v1/world/capabilities/wear | What you wear from your NFTs and COSM copies: your pick per avatar slot (head, body, legs, feet, back) and what the room sees.
[**get_world_chest**](WorldApi.md#get_world_chest) | **GET** /v1/world/chests | The Commons chest: data.window (this 20-minute window, UTC), spot ([x, z] on the plaza), endsAt (when the next chest comes) and mine (openedThis, and opened -- how many windows you have opened one in; the Chest opener pin comes at 10). A chest is opened by walking up to it in Crossly World, never over the API.
[**get_world_collection_capability**](WorldApi.md#get_world_collection_capability) | **GET** /v1/world/collections/{chain}/{contract}/capabilities | The live capability declaration of a collection (404 when it has none).
[**get_world_contest_mine**](WorldApi.md#get_world_contest_mine) | **GET** /v1/world/contests/mine | Your contest entries (best score, attempts used, payment state) and prizes (granted, or owed until their gate opens).
[**get_world_convention**](WorldApi.md#get_world_convention) | **GET** /v1/world/conventions/{id} | One convention. 404 for an unknown or malformed id alike.
[**get_world_cosm_balance**](WorldApi.md#get_world_cosm_balance) | **GET** /v1/world/cosm/balance | Your COSM balance: baseUnits (a STRING -- COSM has 6 decimals and overflows a JSON number), decimals, available (false &#x3D; COSM is not provisioned on this deployment, not a zero balance).
[**get_world_crew**](WorldApi.md#get_world_crew) | **GET** /v1/world/crew | Your crew: data.crew is null when you are in none, else its name, tag, join code and whether you own it; data.members lists up to 30 members, each with the public room they are in right now when they chose to be seen by name (else null).
[**get_world_crew_chat**](WorldApi.md#get_world_crew_chat) | **GET** /v1/world/crew/chat | Your crew chat: data.messages is the last 50 lines (from, name, text, at), kept in memory only, so it starts empty after a restart. 404 when you are in no crew.
[**get_world_crew_leaderboard**](WorldApi.md#get_world_crew_leaderboard) | **GET** /v1/world/crew/leaderboards | The game leaderboards (Price Guess, hunts, speed trades; this week and all time) ranked among your crew only, each member by the name the crew sees. 404 when you are in no crew.
[**get_world_dm**](WorldApi.md#get_world_dm) | **GET** /v1/world/dms/{userId} | Your direct-message thread with one friend, oldest first (the last 100 lines: id, from, text, at, mine). Reading it marks their lines read.
[**get_world_emote_showable**](WorldApi.md#get_world_emote_showable) | **GET** /v1/world/emotes/showable | The things you own that a show-off emote can hold up.
[**get_world_firefly**](WorldApi.md#get_world_firefly) | **GET** /v1/world/fireflies | Fireflies on the Commons lawn: data.day (today, UTC), today (fireflies everyone has caught today) and mine (today -- your catches today, up to perDay -- total, all your catches; the Firefly Catcher pin comes at 30 -- and perDay). Fireflies are caught by walking up to a lit one in Crossly World after dark, never over the API, and nothing is spent.
[**get_world_fit_stat**](WorldApi.md#get_world_fit_stat) | **GET** /v1/world/fits/stats | Your walking storefront, last 7 days: distinct people who tapped \&quot;Shop this\&quot; or \&quot;Offer\&quot; on what you wore, and how many of each. Counts only; nobody is identified.
[**get_world_fit_value**](WorldApi.md#get_world_fit_value) | **GET** /v1/world/fit-value | What your outfit is worth on the market: cents (sum of each catalogued piece&#39;s order-book price -- last sale, else lowest ask), pieces worn, how many were priced, and share (whether you show it on your card).
[**get_world_game**](WorldApi.md#get_world_game) | **GET** /v1/world/games/{id} | One live game: its manifest, its store items and which you own.
[**get_world_game_leaderboard**](WorldApi.md#get_world_game_leaderboard) | **GET** /v1/world/games/{id}/leaderboard | A live game leaderboard, this week and all time, by its manifest scoring (wins, best points, or best time). Only people who chose to be named show by name. scoring is null for a game that keeps no board.
[**get_world_game_package**](WorldApi.md#get_world_game_package) | **GET** /v1/world/games/packages/{id} | One of your game packages with every version, its review state and decision note.
[**get_world_game_template**](WorldApi.md#get_world_game_template) | **GET** /v1/world/games/templates/{kind} | A fresh game package from a template (table, arena, object; collection is an NFT capability declaration), as { path, base64 } files: the world-kit init, for an agent with no local kit. ?id&#x3D;my-game&amp;name&#x3D;My Game.
[**get_world_hall**](WorldApi.md#get_world_hall) | **GET** /v1/world/hall | The Hall of Grails in Crossly World: data.exhibition (key, title, blurb, endsAt -- a new one every Monday UTC -- and next, the coming one&#39;s title) and data.exhibits, up to twelve real catalogue items in slot order (skuId, name, brand, imageUrl, thumbUrl, retailCents, lowestAskCents, lastSaleCents: the live order book, null when the market has none). The first stands on the centre plinth. Buy, bid or watch an exhibit through the market endpoints with its skuId.
[**get_world_hall_loan**](WorldApi.md#get_world_hall_loan) | **GET** /v1/world/hall/loans | Lend to the Hall: this week&#39;s exhibition (key, title, categorySlug, endsAt), your loans on show (id, vaultItemId, skuId, name, credit, since) and the vault pieces you can lend (eligible: vaultItemId, skuId, name, imageUrl, grade) -- held in your Crossly vault, not pledged, in the exhibition&#39;s category. perMember is how many you may lend each week.
[**get_world_home_placeable**](WorldApi.md#get_world_home_placeable) | **GET** /v1/world/home/placeable | What you can place in your home: your items and your furniture.
[**get_world_hunt**](WorldApi.md#get_world_hunt) | **GET** /v1/world/hunt | Your Great Hunt: data.season (id, name, startsAt, endsAt, the title and how many earn it, live), started (you read the first clue), held (keys held, 0-3, always in the order copper, jade, crystal), keys (each with its name, colour, its riddle once it is yours to read, and when you picked it up), and cleared (your rank through the Gate this season, when, and whether you earned the title) or null. Keys are picked up by walking to them in Crossly World; nothing here takes one.
[**get_world_hunt_scoreboard**](WorldApi.md#get_world_hunt_scoreboard) | **GET** /v1/world/hunt/scoreboard | The Great Hunt Scoreboard, as the monolith in the Commons shows it: data.season (the running season, or the last one between seasons), finishers (the first ten through the Gate in order: rank, name, short, named, at, titled -- a name shows only for somebody who chose to be seen by name in the world, everyone else is \&quot;A player\&quot;) and total (everybody through the Gate this season).
[**get_world_interactive_design**](WorldApi.md#get_world_interactive_design) | **GET** /v1/world/interactive/designs/{id} | One of your interactive designs: its draft source, the last static check, and every submitted version with its review state.
[**get_world_job**](WorldApi.md#get_world_job) | **GET** /v1/world/jobs | The jobs board: open staff shifts you could claim, your claimed shifts and open price checks (appraisals), as the world shows them.
[**get_world_kite**](WorldApi.md#get_world_kite) | **GET** /v1/world/kites | Kites flown on the Commons lawn: data.day (today, UTC), today (kites everyone has flown today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have flown one on; the Kite flyer pin comes at 5). Kites are flown by standing out on the lawn in Crossly World by day, never over the API, and nothing is spent.
[**get_world_lantern**](WorldApi.md#get_world_lantern) | **GET** /v1/world/lanterns | Sky lanterns in the Commons: data.day (today, UTC), today (lanterns everyone has released today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have released one on; the Lantern lighter pin comes at 5). Lanterns are released at the lantern stand in Crossly World, never over the API, and nothing is spent.
[**get_world_party_chat**](WorldApi.md#get_world_party_chat) | **GET** /v1/world/parties/{id}/chat | Your party chat: the recent lines. 404 when this is not your party.
[**get_world_place_board**](WorldApi.md#get_world_place_board) | **GET** /v1/world/places/{slug}/boards | The Trade Floor&#39;s wall of wants, its authentication desk and its Vault Markets ticker (vaultMovers: bookKey, name, label, units, markCents, change24hBps; only the trade-floor place has them).
[**get_world_place_collection**](WorldApi.md#get_world_place_collection) | **GET** /v1/world/places/{slug}/collections/{category}/{brand}/{model} | One collection room: every piece of the set, owned or missing. 404 for an unknown room or set.
[**get_world_place_drop**](WorldApi.md#get_world_place_drop) | **GET** /v1/world/places/{slug}/drop | The owner&#39;s next drop (name, cover, time, live) and how many people are waiting in the room.
[**get_world_place_item_interest**](WorldApi.md#get_world_place_item_interest) | **GET** /v1/world/places/{slug}/items/{itemId}/interest | How many people looked at one item in this room today.
[**get_world_place_live**](WorldApi.md#get_world_place_live) | **GET** /v1/world/places/{slug}/live | The owner&#39;s live sale: their stream and the lot on the block, or null.
[**get_world_place_seller**](WorldApi.md#get_world_place_seller) | **GET** /v1/world/places/{slug}/seller | The shop whose public room this is (username and name), or null.
[**get_world_place_shop_pet**](WorldApi.md#get_world_place_shop_pet) | **GET** /v1/world/places/{slug}/shop-pet | The shop&#39;s pet kind, or null.
[**get_world_space**](WorldApi.md#get_world_space) | **GET** /v1/world/spaces/{slug} | One Space: its layout, host, events and your place in it.
[**get_world_space_can_host**](WorldApi.md#get_world_space_can_host) | **GET** /v1/world/spaces/can-host | Whether you may open a Space: sellers only, at most two active.
[**get_world_trial_leaderboard**](WorldApi.md#get_world_trial_leaderboard) | **GET** /v1/world/trials/{course}/leaderboard | A Time Trials course&#39;s boards, as the board beside it in the Commons shows them: data.course, week, weekly (this week&#39;s ten fastest: rank, name, short, named, ms, at) and allTime (the ten fastest ever, each person once). A name shows only for somebody who chose to be seen by name in the world; everyone else is \&quot;A player\&quot;. 404 for an unknown course; course 1 is commons-loop.
[**get_world_trial_mine**](WorldApi.md#get_world_trial_mine) | **GET** /v1/world/trials/mine | Your Hoverboard Time Trials bests: data.week (its Monday, YYYY-MM-DD, UTC) and courses, each with course (id, name, parMs, rings, lengthM), week (your best lap this week in ms, your place on the weekly board, laps finished, and the split at each ring) or null, and allTime (your best ever in ms, your place on the all-time board, when) or null. Laps are timed by Crossly from where it saw you ride in the world; nothing here writes one.
[**get_world_wallet**](WorldApi.md#get_world_wallet) | **GET** /v1/world/wallet | Every balance you hold in Crossly World, read-only: bucksCents (Crossly Bucks, cents); cbx (available, decimals, and the three CBX balances kept apart as base-unit STRINGS -- granted (spend here only), earned (withdrawable once matured), connected (a delegation ceiling on your own wallet, not cash on hand) -- plus pendingCents of cashback not yet matured); cosm (available, decimals, baseUnits string). available:false means that currency is not provisioned on this deployment, not that you hold none.
[**get_world_wish**](WorldApi.md#get_world_wish) | **GET** /v1/world/wishes | The Wishing Fountain in the Commons: data.day (today, UTC), today (wishes everyone has made today) and mine (madeToday, days -- how many days you have wished on, the Wishmaker pin comes at 7 -- and nextAt, when tomorrow&#39;s wish opens). One wish a day; a wish is made by tossing a coin at the fountain in Crossly World, never over the API, and nothing is spent.
[**list_spatial_scene_grants**](WorldApi.md#list_spatial_scene_grants) | **GET** /v1/spatial/scenes/{id}/grants | Everyone who can currently walk into one of your rooms, and unused invites. Never returns codes.
[**list_spatial_scene_warehouse_unplaced**](WorldApi.md#list_spatial_scene_warehouse_unplaced) | **GET** /v1/spatial/scenes/{id}/warehouse/unplaced | Stock not yet on a shelf in a warehouse room you can arrange (q filters by title).
[**list_spatial_shared_with_me**](WorldApi.md#list_spatial_shared_with_me) | **GET** /v1/spatial/shared-with-me | Rooms other people let you into.
[**list_spatial_street_leases**](WorldApi.md#list_spatial_street_leases) | **GET** /v1/spatial/streets/{slug}/leases | Plots on a street offered for lease: weekly rent in CENTS and terms.
[**list_world_avatar_closet**](WorldApi.md#list_world_avatar_closet) | **GET** /v1/world/avatar/closet | Everything you can verifiably wear (your Crossly purchase receipts), newest first: receiptId, item title, brand, size, image, catalog sku/variant, quantity, purchasedAt. Pass a receiptId to POST /v1/world/avatar/equip to put one on. limit 1-200, offset for paging.
[**list_world_avatar_stock**](WorldApi.md#list_world_avatar_stock) | **GET** /v1/world/avatar/stock | Items of your OWN inventory you could wear into a room as a walking storefront: inventoryItemId, title, image and the slot it would go on. Pass an inventoryItemId to POST /v1/world/avatar/equip.
[**list_world_avatar_wearables**](WorldApi.md#list_world_avatar_wearables) | **GET** /v1/world/avatar/wearables | Wearables you have authored as a designer: id, sku, name, slot, priceBaseUnits (COSM base units, a string), maxSupply, mintedCount, active (false until reviewed). meta.available is false when COSM is not provisioned here.
[**list_world_best_dressed**](WorldApi.md#list_world_best_dressed) | **GET** /v1/world/best-dressed | This week&#39;s best-dressed board (Monday-based), top ten: name, profile username and loves. Only people still choosing to be seen by name.
[**list_world_capability_declarations**](WorldApi.md#list_world_capability_declarations) | **GET** /v1/world/capabilities/declarations | Your capability declarations, in every review state (pending, live, rejected with the note from the reviewer).
[**list_world_contest_standings**](WorldApi.md#list_world_contest_standings) | **GET** /v1/world/contests/{id}/standings | The standings of a contest now: best score first (or lowest, for a time game), ties to whoever got there first.
[**list_world_contests**](WorldApi.md#list_world_contests) | **GET** /v1/world/contests | Open skill contests on Crossly World games, soonest ending first: entry mode (free, sponsored, paid) and prizes.
[**list_world_convention_exhibitors**](WorldApi.md#list_world_convention_exhibitors) | **GET** /v1/world/conventions/{id}/exhibitors | The host roster: who applied, who was invited, who is coming (by shop handle). Host only; 404 otherwise.
[**list_world_convention_mine**](WorldApi.md#list_world_convention_mine) | **GET** /v1/world/conventions/mine | Conventions you host and conventions you are exhibiting at.
[**list_world_conventions**](WorldApi.md#list_world_conventions) | **GET** /v1/world/conventions | Conventions open to sellers now or soon: title, room, dates, and how to get a table (invite, free, fee or revenue share).
[**list_world_cosm_cosmetics**](WorldApi.md#list_world_cosm_cosmetics) | **GET** /v1/world/cosm/cosmetics | The active cosmetics catalogue, optionally by tier (premium | earned | stake_exclusive) or slot: sku, name, slot, tier, priceCents (premium only), priceBaseUnits (earned only, COSM base units string), supply, fusable, preview and what it unlocks. Read-only: cosmetics are bought on crossly.net. meta.available / meta.decimals.
[**list_world_cosm_designs**](WorldApi.md#list_world_cosm_designs) | **GET** /v1/world/cosm/designs | Your COSM designs in the world: popularity toward the free chain unlock a popular limited design earns, whether it is on chain, and your opt-out. Declare what a design does with chain cosm and the design id as the contract.
[**list_world_cosm_inventory**](WorldApi.md#list_world_cosm_inventory) | **GET** /v1/world/cosm/inventory | Cosmetics you hold, newest first: ownershipId, cosmeticId, sku, name, slot, tier, how it was acquired, bound, edition number, acquiredAt and what it unlocks. Pass a cosmeticId to POST /v1/world/avatar/equip to wear one. meta.available.
[**list_world_decor_catalogue**](WorldApi.md#list_world_decor_catalogue) | **GET** /v1/world/decor/catalogue | The Decor Shop: every active cosmetic grouped by surface (avatar | home | shop | stall | street) and slot -- name, tier, priceCents (premium: the dollar price, paid in CBX at spot) or priceBaseUnits (earned: COSM, base-unit string), edition supply and remaining, tint swatch, preview, what it unlocks, owned + your edition number, and buyWith. Read-only: buying and minting happen on crossly.net/shop/decor. meta.available, meta.mint {open, reason}, meta.cbx {open, reason} (CBX opens at mint), meta.balances (your COSM and CBX, base-unit strings), meta.surfaces. Never sold by card.
[**list_world_decor_designs**](WorldApi.md#list_world_decor_designs) | **GET** /v1/world/decor/designs | Your decor designs and their review state. available is false until COSM is provisioned.
[**list_world_decor_inventory**](WorldApi.md#list_world_decor_inventory) | **GET** /v1/world/decor/inventory | Your decor as an INVENTORY. Decor is a quantity: every copy is one unit -- a placed prop (home_prop, prop) uses one per placement, a finish (wallpaper, floor, theme, shopfront, facade, sign style, street lamp/banner/paving/arch, booth canopy/pattern/lights/counter) one per space it dresses; free values are unlimited. Per item: key, value, pair (key:value), name, sku, surface, placeable, tint, owned, placed, available, placements [{ space { kind: home | shop | stall | street, id, name }, count }], copies [{ ownershipId, editionNumber }]. meta.available, meta.spaces (every space you dress). Read-only: placing and retracting happen in the app or on crossly.net.
[**list_world_decor_market**](WorldApi.md#list_world_decor_market) | **GET** /v1/world/decor/market | Decor copies other people are reselling (asks in COSM); optional pair filter. Read only: listing and buying stay on crossly.net.
[**list_world_decor_mine**](WorldApi.md#list_world_decor_mine) | **GET** /v1/world/decor/mine | Decor you hold AND decor you have minted to your wallet, newest first: ownershipId, cosmeticId, sku, name, surface, slot, tier, acquiredVia, bound, editionNumber of maxSupply, mintState (held | minting | minted), mintAddress, mintable, and what it unlocks. meta.available, meta.mint.
[**list_world_decor_stalls**](WorldApi.md#list_world_decor_stalls) | **GET** /v1/world/decor/stalls | Your stall bookings, to dress their booths.
[**list_world_decor_streets**](WorldApi.md#list_world_decor_streets) | **GET** /v1/world/decor/streets | Streets you may dress.
[**list_world_dms**](WorldApi.md#list_world_dms) | **GET** /v1/world/dms | Your friends (mutual follows) for direct messages: each with userId, name, the last line between you (text, at, mine) or null, and how many of theirs you have not read; most recent first.
[**list_world_following_rooms**](WorldApi.md#list_world_following_rooms) | **GET** /v1/world/following/rooms | The public rooms of people you follow, to walk into.
[**list_world_follows**](WorldApi.md#list_world_follows) | **GET** /v1/world/follows | Everybody you follow in Crossly World, newest first, each with mutual: true when they follow you back (a friend).
[**list_world_friend_here**](WorldApi.md#list_world_friend_here) | **GET** /v1/world/friends/here | Your friends in Crossly World right now, and where (when they share it).
[**list_world_friends**](WorldApi.md#list_world_friends) | **GET** /v1/world/friends | Your friends (mutual follows), each with the PUBLIC room they are in right now when they chose to be seen by name there (else null), and their home address slug when they let friends visit. Invisible and anonymous friends are never located.
[**list_world_game_packages**](WorldApi.md#list_world_game_packages) | **GET** /v1/world/games/packages | Your game packages, each with its latest version and review state.
[**list_world_game_rewards**](WorldApi.md#list_world_game_rewards) | **GET** /v1/world/games/rewards | Rewards you won in games: granted, or recorded as unfunded for COSM and CBX (a game prints no value).
[**list_world_games**](WorldApi.md#list_world_games) | **GET** /v1/world/games | The Game Directory: every live, reviewed game package with its players, places, rewards, contests and the piece people place.
[**list_world_home_building**](WorldApi.md#list_world_home_building) | **GET** /v1/world/home/building | Homes whose owner made you a co-builder.
[**list_world_interactive_catalogue**](WorldApi.md#list_world_interactive_catalogue) | **GET** /v1/world/interactive/catalogue | Interactive objects: every piece that runs a shared script in a room (first-party and approved creator designs). Per item: model (the piece key a home layout or boutique prop stores), decorValue (the home_prop value its SKU claims), source (first_party | creator), name, blurb, size [x, z] metres, fallbackMesh, cosmeticId (the SKU on the Decor Shop, null when not on sale) and version (a creator design: the approved version every copy runs). Read-only: buying is on crossly.net/shop/decor.
[**list_world_interactive_designs**](WorldApi.md#list_world_interactive_designs) | **GET** /v1/world/interactive/designs | Your interactive-object designs (MML documents you wrote), newest first: id, handle, name, footprint (s | m | l | f), tint, priceBaseUnits (COSM, base-unit string), maxSupply, model, decorValue, cosmeticId, liveVersion (the approved version every copy runs; null &#x3D; none), withdrawnReason, archivedAt (you archived it: off sale, owned copies keep running; null &#x3D; not archived), latestVersion { version, state: pending | approved | rejected | withdrawn | cancelled, decisionNote }, inReview. &#x60;archived&#x60;: exclude (default), include or only archived designs. Read-only: writing, previewing, submitting and archiving happen on crossly.net/shop/decor?tab&#x3D;interactive.
[**list_world_job_posted**](WorldApi.md#list_world_job_posted) | **GET** /v1/world/jobs/posted | Shifts you posted for your rooms, with who claimed each and how it went.
[**list_world_outfits**](WorldApi.md#list_world_outfits) | **GET** /v1/world/outfits | Your saved outfits (up to 6, oldest first): id, name, appearance (skin, hair, hairColour, eyes, build) and items -- each worn thing as the door it goes back on by (slot, door: cosmetic | receipt | stock, id, label). Put one on with POST /v1/world/outfits/:id/apply.
[**list_world_place_bans**](WorldApi.md#list_world_place_bans) | **GET** /v1/world/places/{slug}/bans | Who is banned from a place you own (your boutique or home).
[**list_world_place_bundles**](WorldApi.md#list_world_place_bundles) | **GET** /v1/world/places/{slug}/bundles | The owner&#39;s bundle deals mapped onto this room&#39;s items (itemIds null &#x3D; any N from the shop). The discount is decided at checkout.
[**list_world_place_collections**](WorldApi.md#list_world_place_collections) | **GET** /v1/world/places/{slug}/collections | The owner&#39;s collection rooms: one per category, brand and model they collect.
[**list_world_place_offers**](WorldApi.md#list_world_place_offers) | **GET** /v1/world/places/{slug}/offers | What is for sale in a public room: price, condition and stock, with market references. 404 when no such room is shared.
[**list_world_place_radar**](WorldApi.md#list_world_place_radar) | **GET** /v1/world/places/{slug}/radar | What you have that someone here wants, and what is here that you want: matched on catalog ids.
[**list_world_place_trade_tables**](WorldApi.md#list_world_place_trade_tables) | **GET** /v1/world/places/{slug}/trade-tables | The open trade tables in a place: who is sitting and what is laid on the mat.
[**list_world_place_trades**](WorldApi.md#list_world_place_trades) | **GET** /v1/world/places/{slug}/trades | Items in this room open to trades, each with its trade post path.
[**list_world_provenance**](WorldApi.md#list_world_provenance) | **GET** /v1/world/provenance | Provenance trails: where in Crossly World your purchases were found, newest first (optionally ?listingIds&#x3D;a,b -- platform listing ids). data: [{ platformListingId, slug (the listing public slug), kind (room | window | stall | space | drop | auction | worn | agent), place (its name, or null when gone), at, line -- e.g. \&quot;Found at The Sneaker Vault, Oct 2026\&quot; }]. Yours only.
[**list_world_quests**](WorldApi.md#list_world_quests) | **GET** /v1/world/quests | Every world quest with your progress: key, the pin it earns, goal, target, count, done, colour. meta.wearing is the pin on your nameplate (or null); meta.streak your current and best daily visit streak. Progress only comes from what the server saw -- there is no write of it.
[**list_world_space_mine**](WorldApi.md#list_world_space_mine) | **GET** /v1/world/spaces/mine | Spaces you belong to.
[**list_world_space_requests**](WorldApi.md#list_world_space_requests) | **GET** /v1/world/spaces/{slug}/requests | As host or co-host, who asked to join.
[**list_world_space_whats_on**](WorldApi.md#list_world_space_whats_on) | **GET** /v1/world/spaces/whats-on | Live and upcoming events across Spaces (streets&#x3D;1 and stage&#x3D;1 add street and Main Stage events).
[**list_world_spaces**](WorldApi.md#list_world_spaces) | **GET** /v1/world/spaces | The Spaces directory: seller-hosted clubs with a venue, members and events (optional venue filter).
[**list_world_streaks**](WorldApi.md#list_world_streaks) | **GET** /v1/world/streaks | The longest current daily visit streaks (2+ days), top ten: name and days. Only people still choosing to be seen by name.
[**list_world_trade_mine**](WorldApi.md#list_world_trade_mine) | **GET** /v1/world/trades/mine | Your trades and each item progress through the authentication gate (verified or failed).
[**list_world_trade_table_binder**](WorldApi.md#list_world_trade_table_binder) | **GET** /v1/world/trade-tables/binder | Your binder: unsold collection rows that are catalog items and may be laid on a trade mat -- key, variantId, condition, grade, portfolioId, name, image and valueCents (market value, cents).
[**list_world_trade_table_listings**](WorldApi.md#list_world_trade_table_listings) | **GET** /v1/world/trade-tables/listings | Your open Trade Block trade listings a trade table can be opened on in the world, each with its items&#39; names.
[**update_spatial_scene_cosmetic**](WorldApi.md#update_spatial_scene_cosmetic) | **PATCH** /v1/spatial/scenes/{id}/cosmetics | Redecorate one of your rooms (wall, floor, lighting, trim...). Unknown keys are dropped; the response is what survived. &#x60;clear&#x60; lists keys to reset.
[**update_spatial_scene_node**](WorldApi.md#update_spatial_scene_node) | **PATCH** /v1/spatial/scenes/{id}/nodes/{nodeId} | Move a rack in one of your warehouse rooms (position in metres).
[**update_spatial_scene_setting**](WorldApi.md#update_spatial_scene_setting) | **PATCH** /v1/spatial/scenes/{id}/settings | How one of your rooms is laid out and lit: grouping and sort keys, theme, overlay and the arrival camera. Cosmetics and the shop layout have their own writers.
[**update_spatial_scene_shop_layout**](WorldApi.md#update_spatial_scene_shop_layout) | **PUT** /v1/spatial/scenes/{id}/shop/layout | Save your shop room&#39;s sections and displays (validated server-side; the response is the stored layout).
[**update_spatial_scene_window**](WorldApi.md#update_spatial_scene_window) | **PUT** /v1/spatial/scenes/{id}/window | Choose up to three of your live Crossly listings for the street window of your shop, in slot order. Picks that sell drop out and the newest fill in; an empty list goes back to newest first.
[**update_spatial_street_decor**](WorldApi.md#update_spatial_street_decor) | **PUT** /v1/spatial/streets/{slug}/decor | Dress a street you own with decor you hold (validated against your inventory).
[**update_spatial_street_owned**](WorldApi.md#update_spatial_street_owned) | **PATCH** /v1/spatial/streets/owned/{id} | Who may open a shop on a street you own (open, apply or invite).
[**update_world_auto_shop**](WorldApi.md#update_world_auto_shop) | **PATCH** /v1/world/auto-shop | Turn your automatic world shop off ({ enabled: false } -- an auto-created shop is made private, never deleted) or back on. Answers the new status.
[**update_world_avatar_identity**](WorldApi.md#update_world_avatar_identity) | **PUT** /v1/world/avatar/identity | Choose named or anonymous. Rooms you are already in keep the old answer until you rejoin.
[**update_world_avatar_look**](WorldApi.md#update_world_avatar_look) | **PUT** /v1/world/avatar/look | Save your world look to the account, so every device starts from it. look: null stays anonymous.
[**update_world_avatar_nft_badge**](WorldApi.md#update_world_avatar_nft_badge) | **PUT** /v1/world/avatar/nft-badge | Wear an NFT you hold on your nameplate (null to take it off). Checked again each time you join a room.
[**update_world_capability_wear**](WorldApi.md#update_world_capability_wear) | **PUT** /v1/world/capabilities/wear | Wear a held token on an avatar slot (refId from GET /v1/world/capabilities), or pass refId null to take it off. Its collection must declare a wear capability for that slot.
[**update_world_collection_capability**](WorldApi.md#update_world_collection_capability) | **PUT** /v1/world/collections/{chain}/{contract}/capabilities | Declare what the tokens of a collection can do (the whole declaration, spec crossly.nft-capabilities/1). As its creator (launched on Crossly or claimed) any kind; as a holder, cosmetic kinds only. Replaces your previous declaration; pending if it names an uploaded asset or an always-reviewed kind.
[**update_world_convention_status**](WorldApi.md#update_world_convention_status) | **PUT** /v1/world/conventions/{id}/status | Open, start, end or cancel a convention you host.
[**update_world_cosm_design_chain_auto_unlock**](WorldApi.md#update_world_cosm_design_chain_auto_unlock) | **PUT** /v1/world/cosm/designs/{id}/chain-auto-unlock | Opt one of your COSM designs in or out of the free chain unlock it earns when popular (on by default). Answers its popularity.
[**update_world_emote_wheel**](WorldApi.md#update_world_emote_wheel) | **PUT** /v1/world/emotes/wheel | Arrange your emote wheel: up to 8 slots, each an emote id, a moment slot or null. Returns the saved wheel (locked or unknown ids are dropped).
[**update_world_fit_value_share**](WorldApi.md#update_world_fit_value_share) | **PUT** /v1/world/fit-value/share | Whether people in a room can see what your outfit is worth.
[**update_world_home**](WorldApi.md#update_world_home) | **PATCH** /v1/world/home | Your home: privacy (open, friends, private), theme, and wall, floor and mood decor you hold.
[**update_world_home_builder**](WorldApi.md#update_world_home_builder) | **PUT** /v1/world/home/builders | Set the co-builders of your home: { userIds } -- friends (mutual follows) only, at most 4, replacing the list ([] clears it). They may rearrange your home in the world with your things and add free furniture, never your bought pieces. New co-builders get a world notice.
[**update_world_home_layout**](WorldApi.md#update_world_home_layout) | **PUT** /v1/world/home/layout | Arrange your home: the full layout (up to 200 pieces you own), validated server-side.
[**update_world_home_layout_by_slug**](WorldApi.md#update_world_home_layout_by_slug) | **PUT** /v1/world/homes/{slug}/layout | Rearrange a home you co-build (never adding the owner bought pieces).
[**update_world_interactive_design_draft**](WorldApi.md#update_world_interactive_design_draft) | **PUT** /v1/world/interactive/designs/{id}/draft | Save the draft MML source (up to 64 KB); the response carries its static check.
[**update_world_listing_holders_only**](WorldApi.md#update_world_listing_holders_only) | **PUT** /v1/world/listings/{id}/holders-only | Reserve one of your listings for holders of a collection you declared a holders_only perk for (or release it). Checkout refuses anybody else.
[**update_world_outfit**](WorldApi.md#update_world_outfit) | **PATCH** /v1/world/outfits/{id} | Rename a saved look: { name (1-32 chars) }. 404 when it is not yours.
[**update_world_pet_active**](WorldApi.md#update_world_pet_active) | **PUT** /v1/world/pets/active | Walk one of your pets with you in the world, or none (kind: null).
[**update_world_quest_pin**](WorldApi.md#update_world_quest_pin) | **PUT** /v1/world/quests/pin | Wear a pin you EARNED from a quest on your nameplate, or { pin: null } to wear none. 403 for a pin you have not earned. Shows from the next room you walk into.
[**update_world_room_holder_gate**](WorldApi.md#update_world_room_holder_gate) | **PUT** /v1/world/rooms/{id}/holder-gate | Make your room holders-only (its collection rooms follow). Send null to open it again. Returns &#x60;{ gate }&#x60;.
[**update_world_space**](WorldApi.md#update_world_space) | **PATCH** /v1/world/spaces/{slug} | As host, change a Space name, about or membership.
[**update_world_space_holder_gate**](WorldApi.md#update_world_space_holder_gate) | **PUT** /v1/world/spaces/{slug}/holder-gate | Make your Space holders-only: only holders of an NFT collection join it (others can look in). Send null to open it again. Returns &#x60;{ gate }&#x60;.
[**update_world_stall_booking_booth**](WorldApi.md#update_world_stall_booking_booth) | **PUT** /v1/world/stalls/bookings/{id}/booth | Dress the booth of a stall you booked (decor you hold).


# **create_spatial_invite_accept**
> CreateSpatialInviteAcceptResponse create_spatial_invite_accept()

Redeem an invite code (dashes optional); returns the room it opens.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_invite_accept_response import CreateSpatialInviteAcceptResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Redeem an invite code (dashes optional); returns the room it opens.
        api_response = api_instance.create_spatial_invite_accept()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_invite_accept: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSpatialInviteAcceptResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_property_lease_withdraw**
> DeleteDaoProposalResponse create_spatial_property_lease_withdraw(id)

Withdraw a lease offer nobody has accepted yet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.dao.delete_dao_proposal_response import DeleteDaoProposalResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw a lease offer nobody has accepted yet.
        api_response = api_instance.create_spatial_property_lease_withdraw(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_property_lease_withdraw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteDaoProposalResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene**
> SpatialSceneResponse2 create_spatial_scene(create_spatial_scene_request)

Start a 3D room: a collection (your items on shelves) or a warehouse (racks you arrange). Private until you make it public.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_scene_request import CreateSpatialSceneRequest
from crossly.model.common.error import Error
from crossly.model.common.spatial_scene_response2 import SpatialSceneResponse2
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_spatial_scene_request = CreateSpatialSceneRequest(
        kind="collection",
        name="name_example",
        category_slug="category_slug_example",
    ) # CreateSpatialSceneRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a 3D room: a collection (your items on shelves) or a warehouse (racks you arrange). Private until you make it public.
        api_response = api_instance.create_spatial_scene(create_spatial_scene_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_spatial_scene_request** | **CreateSpatialSceneRequest**|  |

### Return type

**SpatialSceneResponse2**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_grant**
> CreateSpatialSceneGrantResponse create_spatial_scene_grant(id)

Let a specific user into one of your rooms (visitor or staff), no code needed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_scene_grant_response import CreateSpatialSceneGrantResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Let a specific user into one of your rooms (visitor or staff), no code needed.
        api_response = api_instance.create_spatial_scene_grant(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_grant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateSpatialSceneGrantResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_invite**
> CreateSpatialSceneInviteResponse create_spatial_scene_invite(id)

Mint an invite code to one of your rooms (visitor or staff, optional expiry in hours). The code is in this response only: just its hash is stored.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.create_spatial_scene_invite_response import CreateSpatialSceneInviteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mint an invite code to one of your rooms (visitor or staff, optional expiry in hours). The code is in this response only: just its hash is stored.
        api_response = api_instance.create_spatial_scene_invite(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateSpatialSceneInviteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_node**
> CreateSpatialSceneNodeResponse create_spatial_scene_node(id)

Add a unit (rack, shelf, bin) to one of your warehouse rooms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_scene_node_response import CreateSpatialSceneNodeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add a unit (rack, shelf, bin) to one of your warehouse rooms.
        api_response = api_instance.create_spatial_scene_node(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateSpatialSceneNodeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_place**
> SpatialSceneResponse create_spatial_scene_place(id)

Pin an inventory item to a slot in one of your rooms: by warehouse nodeId, or by a collection container key and index.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.spatial_scene_response import SpatialSceneResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Pin an inventory item to a slot in one of your rooms: by warehouse nodeId, or by a collection container key and index.
        api_response = api_instance.create_spatial_scene_place(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_place: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**SpatialSceneResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_rename**
> SpatialSceneResponse2 create_spatial_scene_rename(id, create_spatial_scene_rename_request)

Rename one of your rooms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.spatial_scene_response2 import SpatialSceneResponse2
from crossly.model.spatial.create_spatial_scene_rename_request import CreateSpatialSceneRenameRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    create_spatial_scene_rename_request = CreateSpatialSceneRenameRequest(
        name="name_example",
    ) # CreateSpatialSceneRenameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Rename one of your rooms.
        api_response = api_instance.create_spatial_scene_rename(id, create_spatial_scene_rename_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_rename: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **create_spatial_scene_rename_request** | **CreateSpatialSceneRenameRequest**|  |

### Return type

**SpatialSceneResponse2**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_shop_place**
> SpatialSceneResponse create_spatial_scene_shop_place(id)

Place an inventory item in a section and display of your shop room.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.spatial_scene_response import SpatialSceneResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Place an inventory item in a section and display of your shop room.
        api_response = api_instance.create_spatial_scene_shop_place(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_shop_place: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**SpatialSceneResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_unpin**
> DeleteSpatialSceneNodeResponse create_spatial_scene_unpin(id)

Clear every pin in one of your rooms, so it arranges itself again.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_node_response import DeleteSpatialSceneNodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Clear every pin in one of your rooms, so it arranges itself again.
        api_response = api_instance.create_spatial_scene_unpin(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_unpin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteSpatialSceneNodeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_visibility**
> SpatialSceneResponse2 create_spatial_scene_visibility(id, create_spatial_scene_visibility_request)

Make one of your rooms private, unlisted (anyone with the link) or public (in the lobby and searchable).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.spatial_scene_response2 import SpatialSceneResponse2
from crossly.model.spatial.create_spatial_scene_visibility_request import CreateSpatialSceneVisibilityRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    create_spatial_scene_visibility_request = CreateSpatialSceneVisibilityRequest(
        visibility="private",
    ) # CreateSpatialSceneVisibilityRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Make one of your rooms private, unlisted (anyone with the link) or public (in the lobby and searchable).
        api_response = api_instance.create_spatial_scene_visibility(id, create_spatial_scene_visibility_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_visibility: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **create_spatial_scene_visibility_request** | **CreateSpatialSceneVisibilityRequest**|  |

### Return type

**SpatialSceneResponse2**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_scene_warehouse_stock**
> SpatialSceneResponse create_spatial_scene_warehouse_stock(id)

Put an inventory item (or unit) on a rack in one of your warehouse rooms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.spatial_scene_response import SpatialSceneResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Put an inventory item (or unit) on a rack in one of your warehouse rooms.
        api_response = api_instance.create_spatial_scene_warehouse_stock(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_scene_warehouse_stock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**SpatialSceneResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_shop_neighbourhood**
> CreateSpatialShopNeighbourhoodResponse create_spatial_shop_neighbourhood()

Move your shop to another neighbourhood (by slug).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_shop_neighbourhood_response import CreateSpatialShopNeighbourhoodResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Move your shop to another neighbourhood (by slug).
        api_response = api_instance.create_spatial_shop_neighbourhood()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_shop_neighbourhood: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSpatialShopNeighbourhoodResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_street_apply**
> CreateSpatialStreetApplyResponse create_spatial_street_apply(slug)

Ask to open your shop on a street whose owner reviews applications.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_street_apply_response import CreateSpatialStreetApplyResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ask to open your shop on a street whose owner reviews applications.
        api_response = api_instance.create_spatial_street_apply(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_street_apply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateSpatialStreetApplyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_spatial_street_invite**
> CreateSpatialStreetApplyResponse create_spatial_street_invite(slug)

Invite a shop (by its slug) to open on a street you own.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.create_spatial_street_apply_response import CreateSpatialStreetApplyResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Invite a shop (by its slug) to open on a street you own.
        api_response = api_instance.create_spatial_street_invite(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_spatial_street_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateSpatialStreetApplyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_avatar_equip**
> CreateWorldAvatarEquipResponse create_world_avatar_equip(create_world_avatar_equip_request)

Wear something you already own -- exactly ONE of { cosmeticId } (a cosmetic you hold), { receiptId } (a Crossly purchase from your closet) or { inventoryItemId } (your own stock). The slot comes from the thing itself; slot is only a fallback for an item with no catalog shape. Replaces whatever was in that slot. Moves no money. Answers the slot and your loadout after the change.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_avatar_equip_response import CreateWorldAvatarEquipResponse
from crossly.model.world.create_world_avatar_equip_request import CreateWorldAvatarEquipRequest
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_avatar_equip_request = CreateWorldAvatarEquipRequest(
        cosmetic_id="cosmetic_id_example",
        receipt_id="receipt_id_example",
        inventory_item_id="inventory_item_id_example",
        slot="avatar_head",
    ) # CreateWorldAvatarEquipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Wear something you already own -- exactly ONE of { cosmeticId } (a cosmetic you hold), { receiptId } (a Crossly purchase from your closet) or { inventoryItemId } (your own stock). The slot comes from the thing itself; slot is only a fallback for an item with no catalog shape. Replaces whatever was in that slot. Moves no money. Answers the slot and your loadout after the change.
        api_response = api_instance.create_world_avatar_equip(create_world_avatar_equip_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_avatar_equip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_avatar_equip_request** | **CreateWorldAvatarEquipRequest**|  |

### Return type

**CreateWorldAvatarEquipResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_avatar_unequip**
> CreateWorldAvatarUnequipResponse create_world_avatar_unequip(create_world_avatar_unequip_request)

Take off whatever is in one slot. Idempotent: an empty slot answers removed:false. Answers your loadout after the change.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_avatar_unequip_request import CreateWorldAvatarUnequipRequest
from crossly.model.common.error import Error
from crossly.model.world.create_world_avatar_unequip_response import CreateWorldAvatarUnequipResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_avatar_unequip_request = CreateWorldAvatarUnequipRequest(
        slot="avatar_head",
    ) # CreateWorldAvatarUnequipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Take off whatever is in one slot. Idempotent: an empty slot answers removed:false. Answers your loadout after the change.
        api_response = api_instance.create_world_avatar_unequip(create_world_avatar_unequip_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_avatar_unequip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_avatar_unequip_request** | **CreateWorldAvatarUnequipRequest**|  |

### Return type

**CreateWorldAvatarUnequipResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_avatar_wearable**
> CreateWorldAvatarWearableResponse create_world_avatar_wearable()

Author a wearable for a body slot (a mesh profile and params, an asking price in COSM base units as a string). A submission: inactive until an operator approves it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_avatar_wearable_response import CreateWorldAvatarWearableResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Author a wearable for a body slot (a mesh profile and params, an asking price in COSM base units as a string). A submission: inactive until an operator approves it.
        api_response = api_instance.create_world_avatar_wearable()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_avatar_wearable: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldAvatarWearableResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_contest**
> CreateWorldContestResponse create_world_contest()

Set up a skill contest on a game placed in your place: title, game (its instance id), entry { mode, feeCents? }, prizes by place, funder, window, attempts. Paid entry needs the operator to allow it where it runs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_contest_response import CreateWorldContestResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set up a skill contest on a game placed in your place: title, game (its instance id), entry { mode, feeCents? }, prizes by place, funder, window, attempts. Paid entry needs the operator to allow it where it runs.
        api_response = api_instance.create_world_contest()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_contest: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldContestResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_contest_entry_settle_payment**
> CreateWorldContestEntrySettlePaymentResponse create_world_contest_entry_settle_payment(id)

Read the fee of a paid entry back from Stripe and settle it (safe to repeat).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_contest_entry_settle_payment_response import CreateWorldContestEntrySettlePaymentResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Read the fee of a paid entry back from Stripe and settle it (safe to repeat).
        api_response = api_instance.create_world_contest_entry_settle_payment(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_contest_entry_settle_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldContestEntrySettlePaymentResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_contest_join**
> CreateWorldContestJoinResponse create_world_contest_join(id)

Enter a contest. Free and sponsored contests take you in at once; a paid one answers a client secret to pay the entry fee.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_contest_join_response import CreateWorldContestJoinResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enter a contest. Free and sponsored contests take you in at once; a paid one answers a client secret to pay the entry fee.
        api_response = api_instance.create_world_contest_join(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_contest_join: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldContestJoinResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention**
> CreateWorldConventionResponse create_world_convention()

Host a convention in one of your rooms: title, dates, tables and how sellers get one (invite, free, a fee in cents, or a revenue share in basis points).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_convention_response import CreateWorldConventionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Host a convention in one of your rooms: title, dates, tables and how sellers get one (invite, free, a fee in cents, or a revenue share in basis points).
        api_response = api_instance.create_world_convention()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldConventionResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention_accept**
> CreateWorldConventionAcceptResponse create_world_convention_accept(id)

Accept: your own invitation (no body), or, as host, an application (username).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_convention_accept_response import CreateWorldConventionAcceptResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept: your own invitation (no body), or, as host, an application (username).
        api_response = api_instance.create_world_convention_accept(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention_accept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldConventionAcceptResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention_apply**
> CreateWorldConventionApplyResponse create_world_convention_apply(id)

Ask for a table at a convention.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_convention_apply_response import CreateWorldConventionApplyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ask for a table at a convention.
        api_response = api_instance.create_world_convention_apply(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention_apply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldConventionApplyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention_invite**
> CreateWorldSpaceInviteResponse create_world_convention_invite(id)

Invite a seller (by shop handle) to a convention you host.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_space_invite_response import CreateWorldSpaceInviteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Invite a seller (by shop handle) to a convention you host.
        api_response = api_instance.create_world_convention_invite(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldSpaceInviteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention_paid**
> CreateBreakCancelResponse create_world_convention_paid(id)

As host, record that a seller (username) paid their table fee off-platform. Moves no money.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host, record that a seller (username) paid their table fee off-platform. Moves no money.
        api_response = api_instance.create_world_convention_paid(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention_paid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_convention_withdraw**
> CreateBreakCancelResponse create_world_convention_withdraw(id)

Withdraw your table or decline your invitation; as host, decline someone (username).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw your table or decline your invitation; as host, decline someone (username).
        api_response = api_instance.create_world_convention_withdraw(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_convention_withdraw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_crew**
> CreateWorldCrewResponse create_world_crew(create_world_crew_request)

Start a crew you own: { name (2-32 chars), tag (2-5 letters or digits, shown on members' nameplates) }. Answers its id and join code. 409 when you are already in a crew.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_crew_request import CreateWorldCrewRequest
from crossly.model.common.error import Error
from crossly.model.world.create_world_crew_response import CreateWorldCrewResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_crew_request = CreateWorldCrewRequest(
        name="name_example",
        tag="tag_example",
    ) # CreateWorldCrewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a crew you own: { name (2-32 chars), tag (2-5 letters or digits, shown on members' nameplates) }. Answers its id and join code. 409 when you are already in a crew.
        api_response = api_instance.create_world_crew(create_world_crew_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_crew: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_crew_request** | **CreateWorldCrewRequest**|  |

### Return type

**CreateWorldCrewResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_crew_chat**
> WorldResponse create_world_crew_chat(create_world_crew_chat_request)

Say a line to your crew (body: text, up to 400 characters). Returns data.messages, the crew chat ring (the last 50 lines, kept in memory only), and data.said when your line went out; a blocked or too-quick line is dropped silently. 404 when you are in no crew.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.world_response import WorldResponse
from crossly.model.world.create_world_crew_chat_request import CreateWorldCrewChatRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_crew_chat_request = CreateWorldCrewChatRequest(
        text="text_example",
    ) # CreateWorldCrewChatRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Say a line to your crew (body: text, up to 400 characters). Returns data.messages, the crew chat ring (the last 50 lines, kept in memory only), and data.said when your line went out; a blocked or too-quick line is dropped silently. 404 when you are in no crew.
        api_response = api_instance.create_world_crew_chat(create_world_crew_chat_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_crew_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_crew_chat_request** | **CreateWorldCrewChatRequest**|  |

### Return type

**WorldResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_crew_join**
> CreateWorldCrewJoinResponse create_world_crew_join(create_world_crew_join_request)

Join a crew by the code a member gave you. 404 for an unknown code, 409 when you are already in a crew or it is full (30).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_crew_join_response import CreateWorldCrewJoinResponse
from crossly.model.common.error import Error
from crossly.model.world.create_world_crew_join_request import CreateWorldCrewJoinRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_crew_join_request = CreateWorldCrewJoinRequest(
        code="code_example",
    ) # CreateWorldCrewJoinRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Join a crew by the code a member gave you. 404 for an unknown code, 409 when you are already in a crew or it is full (30).
        api_response = api_instance.create_world_crew_join(create_world_crew_join_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_crew_join: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_crew_join_request** | **CreateWorldCrewJoinRequest**|  |

### Return type

**CreateWorldCrewJoinResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_crew_leave**
> CreateWorldCrewLeaveResponse create_world_crew_leave()

Leave your crew. If you own it, the crew is disbanded. Idempotent: leaving when in none succeeds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_crew_leave_response import CreateWorldCrewLeaveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Leave your crew. If you own it, the crew is disbanded. Idempotent: leaving when in none succeeds.
        api_response = api_instance.create_world_crew_leave()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_crew_leave: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldCrewLeaveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_decor_design**
> CreateWorldDecorDesignResponse create_world_decor_design()

Author a decor design (what it unlocks, a mesh profile and params, an asking price in COSM base units as a string). Inactive until an operator approves it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_decor_design_response import CreateWorldDecorDesignResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Author a decor design (what it unlocks, a mesh profile and params, an asking price in COSM base units as a string). Inactive until an operator approves it.
        api_response = api_instance.create_world_decor_design()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_decor_design: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldDecorDesignResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_decor_design_submit**
> CreateWorldDecorDesignSubmitResponse create_world_decor_design_submit(id)

Send one of your decor designs to the review queue.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_decor_design_submit_response import CreateWorldDecorDesignSubmitResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Send one of your decor designs to the review queue.
        api_response = api_instance.create_world_decor_design_submit(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_decor_design_submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldDecorDesignSubmitResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_decor_retract**
> CreateWorldDecorRetractResponse create_world_decor_retract()

Take a placed decor piece back into your inventory; answers the inventory after.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_decor_retract_response import CreateWorldDecorRetractResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Take a placed decor piece back into your inventory; answers the inventory after.
        api_response = api_instance.create_world_decor_retract()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_decor_retract: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldDecorRetractResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_dm**
> CreateWorldDmResponse create_world_dm(user_id, create_world_crew_chat_request)

Send a direct message to a friend (a mutual follow; never across a block), up to 400 characters, through the world chat guard. 403 when they are not a friend, 429 when sent too quickly.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_crew_chat_request import CreateWorldCrewChatRequest
from crossly.model.world.create_world_dm_response import CreateWorldDmResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 
    create_world_crew_chat_request = CreateWorldCrewChatRequest(
        text="text_example",
    ) # CreateWorldCrewChatRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Send a direct message to a friend (a mutual follow; never across a block), up to 400 characters, through the world chat guard. 403 when they are not a friend, 429 when sent too quickly.
        api_response = api_instance.create_world_dm(user_id, create_world_crew_chat_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_dm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **create_world_crew_chat_request** | **CreateWorldCrewChatRequest**|  |

### Return type

**CreateWorldDmResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_follow**
> CreateWorldFollowResponse create_world_follow(user_id)

Follow somebody. When they follow you back you are friends (friends-here, invites, messages). Idempotent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_follow_response import CreateWorldFollowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Follow somebody. When they follow you back you are friends (friends-here, invites, messages). Idempotent.
        api_response = api_instance.create_world_follow(user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_follow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**CreateWorldFollowResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_friend_invite**
> CreateWorldFriendInviteResponse create_world_friend_invite(user_id, create_world_friend_invite_request)

\"Join me\": send one friend (a mutual follow) a notification with a link to the PUBLIC room you name by slug. 404 when they are not a friend or the room is not public; 429 when you invited them in the last minute.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_friend_invite_response import CreateWorldFriendInviteResponse
from crossly.model.world.create_world_friend_invite_request import CreateWorldFriendInviteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 
    create_world_friend_invite_request = CreateWorldFriendInviteRequest(
        slug="slug_example",
    ) # CreateWorldFriendInviteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # \"Join me\": send one friend (a mutual follow) a notification with a link to the PUBLIC room you name by slug. 404 when they are not a friend or the room is not public; 429 when you invited them in the last minute.
        api_response = api_instance.create_world_friend_invite(user_id, create_world_friend_invite_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_friend_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **create_world_friend_invite_request** | **CreateWorldFriendInviteRequest**|  |

### Return type

**CreateWorldFriendInviteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_game_package**
> CreateWorldGamePackageResponse create_world_game_package()

Submit a game package version for review: files as { path, base64 } (game.json, thumb.png, logic/, scene/, audio/, images/). Checked like the CLI, assets quarantined, the entry document dry-run, then reviewed by a person.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_game_package_response import CreateWorldGamePackageResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Submit a game package version for review: files as { path, base64 } (game.json, thumb.png, logic/, scene/, audio/, images/). Checked like the CLI, assets quarantined, the entry document dry-run, then reviewed by a person.
        api_response = api_instance.create_world_game_package()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_game_package: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldGamePackageResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_game_package_check**
> CreateWorldGamePackageCheckResponse create_world_game_package_check()

Validate a game package exactly as a submission is checked (the shared intake report, your version still free) without storing, uploading or queuing anything: world-kit validate for an agent. Same files body as submit.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_game_package_check_response import CreateWorldGamePackageCheckResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Validate a game package exactly as a submission is checked (the shared intake report, your version still free) without storing, uploading or queuing anything: world-kit validate for an agent. Same files body as submit.
        api_response = api_instance.create_world_game_package_check()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_game_package_check: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldGamePackageCheckResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_game_rating**
> CreateWorldGameRatingResponse create_world_game_rating(id)

Rate a game you played, 1 to 5 stars (rating again replaces it). Only players the runner recorded in that game can rate it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_game_rating_response import CreateWorldGameRatingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Rate a game you played, 1 to 5 stars (rating again replaces it). Only players the runner recorded in that game can rate it.
        api_response = api_instance.create_world_game_rating(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_game_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldGameRatingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_game_report**
> CreateWorldGameReportResponse create_world_game_report(id)

Report a game: reason broken | unfair | offensive | scam | other, optional detail. Staff review it; the creator is told the reason, never who.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_game_report_response import CreateWorldGameReportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Report a game: reason broken | unfair | offensive | scam | other, optional detail. Staff review it; the creator is told the reason, never who.
        api_response = api_instance.create_world_game_report(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_game_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldGameReportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_game_store_checkout**
> CreateWorldGameStoreCheckoutResponse create_world_game_store_checkout(id, item)

Buy an item or pass from a game store: answers a client secret for the payment; the item is yours once it succeeds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_game_store_checkout_response import CreateWorldGameStoreCheckoutResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    item = "item_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy an item or pass from a game store: answers a client secret for the payment; the item is yours once it succeeds.
        api_response = api_instance.create_world_game_store_checkout(id, item)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_game_store_checkout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **item** | **str**|  |

### Return type

**CreateWorldGameStoreCheckoutResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_grail_match**
> CreateWorldGrailMatchResponse create_world_grail_match()

Grail glints: send the ids on show somewhere (listingIds -- listings.id, inventoryIds, skuIds -- catalogue market SKUs; up to 400 each) and get back data.listingIds / data.inventoryIds / data.skuIds: the ones that are things you already want -- an open bid, a watched or wishlisted listing (or one selling the same SKU), a market watch, or a card your deck is missing. Read-only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_grail_match_response import CreateWorldGrailMatchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Grail glints: send the ids on show somewhere (listingIds -- listings.id, inventoryIds, skuIds -- catalogue market SKUs; up to 400 each) and get back data.listingIds / data.inventoryIds / data.skuIds: the ones that are things you already want -- an open bid, a watched or wishlisted listing (or one selling the same SKU), a market watch, or a card your deck is missing. Read-only.
        api_response = api_instance.create_world_grail_match()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_grail_match: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldGrailMatchResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_hall_loan**
> CreateWorldHallLoanResponse create_world_hall_loan()

Lend a piece from your vault to this week's Hall of Grails exhibition: { vaultItemId, credit: 'name' | 'anonymous' }. It shows under your plaque until the exhibition ends; it stays in your vault (still listable and withdrawable), and stops showing if it leaves.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_hall_loan_response import CreateWorldHallLoanResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lend a piece from your vault to this week's Hall of Grails exhibition: { vaultItemId, credit: 'name' | 'anonymous' }. It shows under your plaque until the exhibition ends; it stays in your vault (still listable and withdrawable), and stops showing if it leaves.
        api_response = api_instance.create_world_hall_loan()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_hall_loan: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldHallLoanResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_home_ask**
> CreateWorldHomeAskResponse create_world_home_ask(slug)

Ask a home owner whether they would sell a piece you saw there (an item or a decor piece).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_home_ask_response import CreateWorldHomeAskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ask a home owner whether they would sell a piece you saw there (an item or a decor piece).
        api_response = api_instance.create_world_home_ask(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_home_ask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldHomeAskResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_home_guestbook**
> CreateWorldHomeGuestbookResponse create_world_home_guestbook(slug)

Sign a home guestbook (one short line).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_home_guestbook_response import CreateWorldHomeGuestbookResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Sign a home guestbook (one short line).
        api_response = api_instance.create_world_home_guestbook(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_home_guestbook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldHomeGuestbookResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_home_guestbook_report**
> CreateWorldGameReportResponse create_world_home_guestbook_report(slug, id)

Report a guestbook entry to moderation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_game_report_response import CreateWorldGameReportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Report a guestbook entry to moderation.
        api_response = api_instance.create_world_home_guestbook_report(slug, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_home_guestbook_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **id** | **str**|  |

### Return type

**CreateWorldGameReportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_hunt_start**
> GetWorldHuntResponse create_world_hunt_start()

Start the Great Hunt this season by reading its first riddle (the Copper key's). Idempotent: starting again answers your progress unchanged. Answers the same shape as GET /v1/world/hunt. 409 when no season is running.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_hunt_response import GetWorldHuntResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start the Great Hunt this season by reading its first riddle (the Copper key's). Idempotent: starting again answers your progress unchanged. Answers the same shape as GET /v1/world/hunt. 409 when no season is running.
        api_response = api_instance.create_world_hunt_start()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_hunt_start: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHuntResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_asset**
> CreateWorldInteractiveAssetResponse create_world_interactive_asset()

Upload one asset for your designs: kind glb (4 MB), wav (4 MB) or png (1 MB), the file as base64. Answers its sha256 and the path to reference from MML.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_interactive_asset_response import CreateWorldInteractiveAssetResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Upload one asset for your designs: kind glb (4 MB), wav (4 MB) or png (1 MB), the file as base64. Answers its sha256 and the path to reference from MML.
        api_response = api_instance.create_world_interactive_asset()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_asset: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldInteractiveAssetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_design**
> GetWorldInteractiveDesignResponse create_world_interactive_design()

Create an interactive design: name, footprint (s, m, l or f), optional tint and description, an asking price in COSM base units (a string, six decimals) and optional max supply. Inactive until ops approve a submitted version.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_interactive_design_response import GetWorldInteractiveDesignResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an interactive design: name, footprint (s, m, l or f), optional tint and description, an asking price in COSM base units (a string, six decimals) and optional max supply. Inactive until ops approve a submitted version.
        api_response = api_instance.create_world_interactive_design()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_design: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldInteractiveDesignResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_design_check**
> CreateWorldInteractiveDesignCheckResponse create_world_interactive_design_check(id)

Check the draft: static rules, that every referenced upload exists, and a sandboxed dry run. Budgeted per person.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_interactive_design_check_response import CreateWorldInteractiveDesignCheckResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check the draft: static rules, that every referenced upload exists, and a sandboxed dry run. Budgeted per person.
        api_response = api_instance.create_world_interactive_design_check(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_design_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldInteractiveDesignCheckResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_design_preview**
> CreateWorldInteractiveDesignPreviewResponse create_world_interactive_design_preview(id)

A private preview token for the draft (author only) and the socket path that runs it. Budgeted per person.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_interactive_design_preview_response import CreateWorldInteractiveDesignPreviewResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A private preview token for the draft (author only) and the socket path that runs it. Budgeted per person.
        api_response = api_instance.create_world_interactive_design_preview(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_design_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldInteractiveDesignPreviewResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_design_submit**
> CreateWorldInteractiveDesignSubmitResponse create_world_interactive_design_submit(id)

Freeze the draft as a new version and send it to ops review. Up to 10 a day.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_interactive_design_submit_response import CreateWorldInteractiveDesignSubmitResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Freeze the draft as a new version and send it to ops review. Up to 10 a day.
        api_response = api_instance.create_world_interactive_design_submit(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_design_submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldInteractiveDesignSubmitResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_interactive_reset**
> CreateWorldInteractiveResetResponse create_world_interactive_reset()

Wipe the stored state of an interactive piece standing in a place you own (a home or your boutique).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_interactive_reset_response import CreateWorldInteractiveResetResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wipe the stored state of an interactive piece standing in a place you own (a home or your boutique).
        api_response = api_instance.create_world_interactive_reset()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_interactive_reset: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldInteractiveResetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_job_appraisal_answer**
> CreateWorldJobAppraisalAnswerResponse create_world_job_appraisal_answer(id)

Answer a price check: your estimate of the item value in CENTS and an optional note. Moves no money; the asker may accept it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_job_appraisal_answer_response import CreateWorldJobAppraisalAnswerResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Answer a price check: your estimate of the item value in CENTS and an optional note. Moves no money; the asker may accept it.
        api_response = api_instance.create_world_job_appraisal_answer(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_job_appraisal_answer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldJobAppraisalAnswerResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_job_shift_claim**
> CreateWorldJobShiftClaimResponse create_world_job_shift_claim(id)

Claim an open shift. You work it by being in the place while it runs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_job_shift_claim_response import CreateWorldJobShiftClaimResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Claim an open shift. You work it by being in the place while it runs.
        api_response = api_instance.create_world_job_shift_claim(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_job_shift_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldJobShiftClaimResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_job_shift_release**
> CreateWorldJobShiftReleaseResponse create_world_job_shift_release(id)

Give a shift you claimed back to the board.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_job_shift_release_response import CreateWorldJobShiftReleaseResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Give a shift you claimed back to the board.
        api_response = api_instance.create_world_job_shift_release(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_job_shift_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldJobShiftReleaseResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_outfit**
> CreateWorldOutfitResponse create_world_outfit(create_world_outfit_request)

Save what you are wearing now as a named look: { name (1-32 chars), appearance? (skin, hair, hairColour, eyes, build -- unknown keys fall back to the default) }. Each worn thing is recorded as the door it goes back on by; one that no longer traces to something you own is listed in skipped and not saved. 409 when you already keep 6.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_outfit_request import CreateWorldOutfitRequest
from crossly.model.common.error import Error
from crossly.model.world.create_world_outfit_response import CreateWorldOutfitResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    create_world_outfit_request = CreateWorldOutfitRequest(
        name="name_example",
        appearance={
            "key": None,
        },
    ) # CreateWorldOutfitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Save what you are wearing now as a named look: { name (1-32 chars), appearance? (skin, hair, hairColour, eyes, build -- unknown keys fall back to the default) }. Each worn thing is recorded as the door it goes back on by; one that no longer traces to something you own is listed in skipped and not saved. 409 when you already keep 6.
        api_response = api_instance.create_world_outfit(create_world_outfit_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_outfit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_outfit_request** | **CreateWorldOutfitRequest**|  |

### Return type

**CreateWorldOutfitResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_outfit_apply**
> CreateWorldOutfitApplyResponse create_world_outfit_apply(id)

Put a saved look on. Every item goes through the same equip as POST /v1/world/avatar/equip, so ownership still holds: something you no longer own is listed in skipped with the reason and not worn. Slots the look left empty are emptied (cleared). Answers the appearance of the look (for your character -- appearance lives on your device), applied, skipped and cleared. Moves no money.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_outfit_apply_response import CreateWorldOutfitApplyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Put a saved look on. Every item goes through the same equip as POST /v1/world/avatar/equip, so ownership still holds: something you no longer own is listed in skipped with the reason and not worn. Slots the look left empty are emptied (cleared). Answers the appearance of the look (for your character -- appearance lives on your device), applied, skipped and cleared. Moves no money.
        api_response = api_instance.create_world_outfit_apply(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_outfit_apply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldOutfitApplyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party**
> CreateBreakResponse create_world_party()

Start a party with you as leader (up to 8 members).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_response import CreateBreakResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start a party with you as leader (up to 8 members).
        api_response = api_instance.create_world_party()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateBreakResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_chat**
> WorldResponse create_world_party_chat(id)

Say something in your party chat (up to 2000 characters).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.world_response import WorldResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Say something in your party chat (up to 2000 characters).
        api_response = api_instance.create_world_party_chat(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**WorldResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_invite**
> CreateWorldPartyInviteResponse create_world_party_invite(id)

Invite a friend (userId) to your party.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_invite_response import CreateWorldPartyInviteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Invite a friend (userId) to your party.
        api_response = api_instance.create_world_party_invite(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldPartyInviteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_invite_accept**
> CreateWorldPartyInviteAcceptResponse create_world_party_invite_accept(invite_id)

Accept a party invite.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_invite_accept_response import CreateWorldPartyInviteAcceptResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    invite_id = "inviteId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept a party invite.
        api_response = api_instance.create_world_party_invite_accept(invite_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_invite_accept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  |

### Return type

**CreateWorldPartyInviteAcceptResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_invite_decline**
> CreateWorldPartyInviteAcceptResponse create_world_party_invite_decline(invite_id)

Decline a party invite.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_invite_accept_response import CreateWorldPartyInviteAcceptResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    invite_id = "inviteId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Decline a party invite.
        api_response = api_instance.create_world_party_invite_decline(invite_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_invite_decline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  |

### Return type

**CreateWorldPartyInviteAcceptResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_kick**
> CreateWorldPartyKickResponse create_world_party_kick(id)

As leader, remove a member (userId).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_party_kick_response import CreateWorldPartyKickResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As leader, remove a member (userId).
        api_response = api_instance.create_world_party_kick(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_kick: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldPartyKickResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_leader**
> CreateWorldPartyLeaderResponse create_world_party_leader(id)

As leader, pass the lead to a member (userId).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_leader_response import CreateWorldPartyLeaderResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As leader, pass the lead to a member (userId).
        api_response = api_instance.create_world_party_leader(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_leader: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldPartyLeaderResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_leave**
> CreateWorldPartyLeaveResponse create_world_party_leave(id)

Leave your party (the lead passes on if you led it).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_party_leave_response import CreateWorldPartyLeaveResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Leave your party (the lead passes on if you led it).
        api_response = api_instance.create_world_party_leave(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_leave: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldPartyLeaveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_wishlist**
> CreateWorldPartyWishlistResponse create_world_party_wishlist(id)

Add a listing (listingId, or its shop slug) to the party wishlist; answers the wishlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_wishlist_response import CreateWorldPartyWishlistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add a listing (listingId, or its shop slug) to the party wishlist; answers the wishlist.
        api_response = api_instance.create_world_party_wishlist(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_wishlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorldPartyWishlistResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_party_wishlist_vote**
> CreateWorldPartyWishlistResponse create_world_party_wishlist_vote(id, listing_id)

Thumb a wishlist listing up or down (null clears your vote); answers the wishlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_wishlist_response import CreateWorldPartyWishlistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    listing_id = "listingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Thumb a wishlist listing up or down (null clears your vote); answers the wishlist.
        api_response = api_instance.create_world_party_wishlist_vote(id, listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_party_wishlist_vote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **listing_id** | **str**|  |

### Return type

**CreateWorldPartyWishlistResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_place_item_want**
> CreateWorldPlaceItemWantResponse create_world_place_item_want(slug, item_id)

Tell a room owner you would buy one of their items (once per person per item; they see the count). Moves no money.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_place_item_want_response import CreateWorldPlaceItemWantResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Tell a room owner you would buy one of their items (once per person per item; they see the count). Moves no money.
        api_response = api_instance.create_world_place_item_want(slug, item_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_place_item_want: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **item_id** | **str**|  |

### Return type

**CreateWorldPlaceItemWantResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space**
> CreateWorldSpaceResponse create_world_space()

Open a Space (sellers only, at most two): slug, name, venue, optional membership and about.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_space_response import CreateWorldSpaceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open a Space (sellers only, at most two): slug, name, venue, optional membership and about.
        api_response = api_instance.create_world_space()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWorldSpaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_event**
> CreateWorldSpaceEventResponse create_world_space_event(slug)

As host or co-host, put an event on: title, kind, optional about, ISO start and end with offset.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_space_event_response import CreateWorldSpaceEventResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host or co-host, put an event on: title, kind, optional about, ISO start and end with offset.
        api_response = api_instance.create_world_space_event(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldSpaceEventResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_event_rsvp**
> CreateWorldSpaceEventRsvpResponse create_world_space_event_rsvp(slug, id)

Say whether you are going to an event.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_space_event_rsvp_response import CreateWorldSpaceEventRsvpResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Say whether you are going to an event.
        api_response = api_instance.create_world_space_event_rsvp(slug, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_event_rsvp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **id** | **str**|  |

### Return type

**CreateWorldSpaceEventRsvpResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_invite**
> CreateWorldSpaceInviteResponse create_world_space_invite(slug)

Invite somebody (userId) to a Space.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_space_invite_response import CreateWorldSpaceInviteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Invite somebody (userId) to a Space.
        api_response = api_instance.create_world_space_invite(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldSpaceInviteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_join**
> CreateWorldSpaceJoinResponse create_world_space_join(slug)

Join a Space, or ask to when it is request-only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.create_world_space_join_response import CreateWorldSpaceJoinResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Join a Space, or ask to when it is request-only.
        api_response = api_instance.create_world_space_join(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_join: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldSpaceJoinResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_leave**
> CreateWorldCrewLeaveResponse create_world_space_leave(slug)

Leave a Space.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_crew_leave_response import CreateWorldCrewLeaveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Leave a Space.
        api_response = api_instance.create_world_space_leave(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_leave: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldCrewLeaveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_request_by_user_id**
> CreateWorldSpaceRequestByUserIdResponse create_world_space_request_by_user_id(slug, user_id)

As host or co-host, accept or turn down a request to join.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_space_request_by_user_id_response import CreateWorldSpaceRequestByUserIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host or co-host, accept or turn down a request to join.
        api_response = api_instance.create_world_space_request_by_user_id(slug, user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_request_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **user_id** | **str**|  |

### Return type

**CreateWorldSpaceRequestByUserIdResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_world_space_role**
> CreateWorldSpaceRoleResponse create_world_space_role(slug)

As host, make a member a co-host or back to a member.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_space_role_response import CreateWorldSpaceRoleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host, make a member a co-host or back to a member.
        api_response = api_instance.create_world_space_role(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->create_world_space_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**CreateWorldSpaceRoleResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_spatial_scene_grant**
> DeleteSpatialSceneGrantResponse delete_spatial_scene_grant(id, grant_id)

Take somebody's access to your room away, or kill an invite nobody has used yet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_grant_response import DeleteSpatialSceneGrantResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    grant_id = "grantId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Take somebody's access to your room away, or kill an invite nobody has used yet.
        api_response = api_instance.delete_spatial_scene_grant(id, grant_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_spatial_scene_grant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **grant_id** | **str**|  |

### Return type

**DeleteSpatialSceneGrantResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_spatial_scene_node**
> DeleteSpatialSceneNodeResponse delete_spatial_scene_node(id)

Remove units (by id, up to 500) from one of your warehouse rooms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_node_response import DeleteSpatialSceneNodeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove units (by id, up to 500) from one of your warehouse rooms.
        api_response = api_instance.delete_spatial_scene_node(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_spatial_scene_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteSpatialSceneNodeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_spatial_scene_warehouse_stock**
> DeleteSpatialSceneGrantResponse delete_spatial_scene_warehouse_stock(id)

Take an inventory item (or unit) off its rack.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_grant_response import DeleteSpatialSceneGrantResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Take an inventory item (or unit) off its rack.
        api_response = api_instance.delete_spatial_scene_warehouse_stock(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_spatial_scene_warehouse_stock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteSpatialSceneGrantResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_spatial_street_request**
> DeleteDaoProposalResponse delete_spatial_street_request(id)

Withdraw a street request you made that has not been founded yet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.dao.delete_dao_proposal_response import DeleteDaoProposalResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw a street request you made that has not been founded yet.
        api_response = api_instance.delete_spatial_street_request(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_spatial_street_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteDaoProposalResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_block**
> DeleteWorldBlockResponse delete_world_block(id)

Unblock somebody (by the block id from GET /v1/world/blocks).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.delete_world_block_response import DeleteWorldBlockResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unblock somebody (by the block id from GET /v1/world/blocks).
        api_response = api_instance.delete_world_block(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteWorldBlockResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_collection_capability**
> delete_world_collection_capability(chain, contract)

Withdraw your declaration for a collection.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw your declaration for a collection.
        api_instance.delete_world_collection_capability(chain, contract)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_collection_capability: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

void (empty response body)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content — the request succeeded and there is no body. |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_follow**
> CreateWorldFollowResponse delete_world_follow(user_id)

Unfollow somebody. Idempotent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_follow_response import CreateWorldFollowResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unfollow somebody. Idempotent.
        api_response = api_instance.delete_world_follow(user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_follow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**CreateWorldFollowResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_hall_loan**
> CreateBreakResponse delete_world_hall_loan(id)

Take one of your loans off show in the Hall of Grails.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_response import CreateBreakResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Take one of your loans off show in the Hall of Grails.
        api_response = api_instance.delete_world_hall_loan(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_hall_loan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_home_guestbook**
> DeleteWorldHomeGuestbookResponse delete_world_home_guestbook(slug, id)

As the home owner, hide a guestbook entry.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.delete_world_home_guestbook_response import DeleteWorldHomeGuestbookResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As the home owner, hide a guestbook entry.
        api_response = api_instance.delete_world_home_guestbook(slug, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_home_guestbook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **id** | **str**|  |

### Return type

**DeleteWorldHomeGuestbookResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_interactive_design**
> DeleteWorldInteractiveDesignResponse delete_world_interactive_design(id)

Delete a draft design, or archive a submitted one (off sale; owned copies keep working).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_interactive_design_response import DeleteWorldInteractiveDesignResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a draft design, or archive a submitted one (off sale; owned copies keep working).
        api_response = api_instance.delete_world_interactive_design(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_interactive_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteWorldInteractiveDesignResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_job_shift**
> DeleteWorldJobShiftResponse delete_world_job_shift(id)

Cancel a shift you posted that nobody has worked yet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_job_shift_response import DeleteWorldJobShiftResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a shift you posted that nobody has worked yet.
        api_response = api_instance.delete_world_job_shift(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_job_shift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteWorldJobShiftResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_outfit**
> DeleteWorldOutfitResponse delete_world_outfit(id)

Delete a saved look. 404 when it is not yours.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.delete_world_outfit_response import DeleteWorldOutfitResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a saved look. 404 when it is not yours.
        api_response = api_instance.delete_world_outfit(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_outfit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteWorldOutfitResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_party_wishlist**
> CreateWorldPartyWishlistResponse delete_world_party_wishlist(id, listing_id)

Take a listing you added off the party wishlist; answers the wishlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_wishlist_response import CreateWorldPartyWishlistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    listing_id = "listingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Take a listing you added off the party wishlist; answers the wishlist.
        api_response = api_instance.delete_world_party_wishlist(id, listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_party_wishlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **listing_id** | **str**|  |

### Return type

**CreateWorldPartyWishlistResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_place_ban**
> DeleteWorldPlaceBanResponse delete_world_place_ban(slug, user_id)

Lift a ban from a place you own; they can walk in again right away.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.delete_world_place_ban_response import DeleteWorldPlaceBanResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Lift a ban from a place you own; they can walk in again right away.
        api_response = api_instance.delete_world_place_ban(slug, user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_place_ban: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **user_id** | **str**|  |

### Return type

**DeleteWorldPlaceBanResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_space**
> DeleteWorldSpaceResponse delete_world_space(slug)

As host, close a Space.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.delete_world_space_response import DeleteWorldSpaceResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host, close a Space.
        api_response = api_instance.delete_world_space(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**DeleteWorldSpaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_world_space_event**
> DeleteWorldJobShiftResponse delete_world_space_event(slug, id)

As host or co-host, cancel an event.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_job_shift_response import DeleteWorldJobShiftResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host or co-host, cancel an event.
        api_response = api_instance.delete_world_space_event(slug, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->delete_world_space_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **id** | **str**|  |

### Return type

**DeleteWorldJobShiftResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_scene_attention**
> GetSpatialSceneAttentionResponse get_spatial_scene_attention(scene_id)

What visitors looked at in one of your rooms: viewers, looks, inspects and dwell per item over the last days (1-35, default 30).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.get_spatial_scene_attention_response import GetSpatialSceneAttentionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    scene_id = "sceneId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What visitors looked at in one of your rooms: viewers, looks, inspects and dwell per item over the last days (1-35, default 30).
        api_response = api_instance.get_spatial_scene_attention(scene_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_scene_attention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**|  |

### Return type

**GetSpatialSceneAttentionResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_scene_window**
> GetSpatialSceneWindowResponse get_spatial_scene_window(id)

The listings you chose for the street window of your shop, in slot order (left, middle, right; empty = newest first), and `choices`: your listings that can go in it, newest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.get_spatial_scene_window_response import GetSpatialSceneWindowResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The listings you chose for the street window of your shop, in slot order (left, middle, right; empty = newest first), and `choices`: your listings that can go in it, newest first.
        api_response = api_instance.get_spatial_scene_window(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_scene_window: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetSpatialSceneWindowResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_shop_neighbourhood**
> GetSpatialShopNeighbourhoodResponse get_spatial_shop_neighbourhood()

Your shop's neighbourhood, and whether and where it may move.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.get_spatial_shop_neighbourhood_response import GetSpatialShopNeighbourhoodResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your shop's neighbourhood, and whether and where it may move.
        api_response = api_instance.get_spatial_shop_neighbourhood()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_shop_neighbourhood: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetSpatialShopNeighbourhoodResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_space**
> GetSpatialSpaceResponse get_spatial_space()

The room catalogue: every space profile (what it holds, how it is sorted, its containers) and the warehouse units.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.get_spatial_space_response import GetSpatialSpaceResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The room catalogue: every space profile (what it holds, how it is sorted, its containers) and the warehouse units.
        api_response = api_instance.get_spatial_space()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_space: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetSpatialSpaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_street_admission**
> GetSpatialStreetAdmissionResponse get_spatial_street_admission()

Street applications and invitations: yours, and those waiting on streets you own.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.get_spatial_street_admission_response import GetSpatialStreetAdmissionResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Street applications and invitations: yours, and those waiting on streets you own.
        api_response = api_instance.get_spatial_street_admission()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_street_admission: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetSpatialStreetAdmissionResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_spatial_street_decor**
> GetSpatialStreetDecorResponse get_spatial_street_decor(slug)

The decor on a street you may dress, and what you can place.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.get_spatial_street_decor_response import GetSpatialStreetDecorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The decor on a street you may dress, and what you can place.
        api_response = api_instance.get_spatial_street_decor(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_spatial_street_decor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetSpatialStreetDecorResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_arcade**
> GetWorldArcadeResponse get_world_arcade()

The Arcade in Crossly World: data.cabinets (slot, where it stands, host -- piece, price_guess or empty --, game, title, blurb, the piece it hosts and where, record, packageId and thumbnail for a creator game from the Game Directory, players) and data.scores (the High Score wall: per game a title, kind -- leaderboard, record or top -- and up to five ASCII lines; a name shows only for somebody who chose to be seen by name, everyone else is \"A player\"), plus creatorGames (creator games with a cabinet now). Games are played in the world.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_arcade_response import GetWorldArcadeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Arcade in Crossly World: data.cabinets (slot, where it stands, host -- piece, price_guess or empty --, game, title, blurb, the piece it hosts and where, record, packageId and thumbnail for a creator game from the Game Directory, players) and data.scores (the High Score wall: per game a title, kind -- leaderboard, record or top -- and up to five ASCII lines; a name shows only for somebody who chose to be seen by name, everyone else is \"A player\"), plus creatorGames (creator games with a cabinet now). Games are played in the world.
        api_response = api_instance.get_world_arcade()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_arcade: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldArcadeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_aurora**
> GetWorldAuroraResponse get_world_aurora()

The Sales Aurora over the Commons in Crossly World: every real sale on Crossly in the last data.windowDays (30) days. data.total (sales in the window), data.families (key, label, colour, count per colour family: cards, coins, jewellery, electronics, media, fashion, toys, other) and data.sales (newest first, at most 48: family, ageHours, fresh -- sold in the last ten minutes, which shimmers). Aggregate only: no item, price, seller or platform. data.updatedAt is when it was read.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_aurora_response import GetWorldAuroraResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Sales Aurora over the Commons in Crossly World: every real sale on Crossly in the last data.windowDays (30) days. data.total (sales in the window), data.families (key, label, colour, count per colour family: cards, coins, jewellery, electronics, media, fashion, toys, other) and data.sales (newest first, at most 48: family, ageHours, fresh -- sold in the last ten minutes, which shimmers). Aggregate only: no item, price, seller or platform. data.updatedAt is when it was read.
        api_response = api_instance.get_world_aurora()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_aurora: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAuroraResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_auto_shop**
> GetWorldAutoShopResponse get_world_auto_shop()

Whether Crossly keeps a world shop for you automatically: enabled, and the shop (id, name, visibility, autoCreated, address, label) or null. Change it with PATCH /v1/world/auto-shop.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_auto_shop_response import GetWorldAutoShopResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether Crossly keeps a world shop for you automatically: enabled, and the shop (id, name, visibility, autoCreated, address, label) or null. Change it with PATCH /v1/world/auto-shop.
        api_response = api_instance.get_world_auto_shop()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_auto_shop: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAutoShopResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_avatar_identity**
> GetWorldAvatarIdentityResponse get_world_avatar_identity()

Whether others see your name in the world (named), or not (anonymous); null if you have never chosen.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_avatar_identity_response import GetWorldAvatarIdentityResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether others see your name in the world (named), or not (anonymous); null if you have never chosen.
        api_response = api_instance.get_world_avatar_identity()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_avatar_identity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAvatarIdentityResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_avatar_loadout**
> GetWorldAvatarLoadoutResponse get_world_avatar_loadout()

What you are wearing: the rig, its slots (avatar_head, avatar_body, avatar_outer -- a jacket over the top, avatar_legs, avatar_feet, avatar_back) and each worn entry -- a cosmetic or a real item -- with its verified-purchase mark. Carries no price, receipt id, seller or order.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_avatar_loadout_response import GetWorldAvatarLoadoutResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What you are wearing: the rig, its slots (avatar_head, avatar_body, avatar_outer -- a jacket over the top, avatar_legs, avatar_feet, avatar_back) and each worn entry -- a cosmetic or a real item -- with its verified-purchase mark. Carries no price, receipt id, seller or order.
        api_response = api_instance.get_world_avatar_loadout()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_avatar_loadout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAvatarLoadoutResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_avatar_loadout_by_user_id**
> GetWorldAvatarLoadoutResponse get_world_avatar_loadout_by_user_id(user_id)

What somebody else is wearing, with the verified-purchase mark on each real item -- public on purpose, since a check only its owner can see is not a check. No price, receipt id, seller or order.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_avatar_loadout_response import GetWorldAvatarLoadoutResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What somebody else is wearing, with the verified-purchase mark on each real item -- public on purpose, since a check only its owner can see is not a check. No price, receipt id, seller or order.
        api_response = api_instance.get_world_avatar_loadout_by_user_id(user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_avatar_loadout_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**GetWorldAvatarLoadoutResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_avatar_look**
> GetWorldAvatarLookResponse get_world_avatar_look()

Your world look on the account: the handle you chose (null if anonymous) and your appearance; null if you never made one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_avatar_look_response import GetWorldAvatarLookResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your world look on the account: the handle you chose (null if anonymous) and your appearance; null if you never made one.
        api_response = api_instance.get_world_avatar_look()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_avatar_look: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAvatarLookResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_avatar_nft_badge**
> GetWorldAvatarNftBadgeResponse get_world_avatar_nft_badge()

The NFT you wear on your nameplate in the world, or null.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_avatar_nft_badge_response import GetWorldAvatarNftBadgeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The NFT you wear on your nameplate in the world, or null.
        api_response = api_instance.get_world_avatar_nft_badge()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_avatar_nft_badge: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAvatarNftBadgeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_capability**
> GetWorldCapabilityResponse get_world_capability()

What your held NFTs unlock in Crossly World: each token with the capabilities its collection declared (wear, display, emote, gate, ...). Holding is your verified wallets (their synced tokens); the capabilities of a transferred token go within five minutes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_capability_response import GetWorldCapabilityResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What your held NFTs unlock in Crossly World: each token with the capabilities its collection declared (wear, display, emote, gate, ...). Holding is your verified wallets (their synced tokens); the capabilities of a transferred token go within five minutes.
        api_response = api_instance.get_world_capability()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_capability: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCapabilityResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_capability_catalogue**
> GetWorldCapabilityCatalogueResponse get_world_capability_catalogue()

The capability kinds of spec crossly.nft-capabilities/1: what each does, whether only the creator of the collection may declare it, whether it needs review, and which clients honour it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_capability_catalogue_response import GetWorldCapabilityCatalogueResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The capability kinds of spec crossly.nft-capabilities/1: what each does, whether only the creator of the collection may declare it, whether it needs review, and which clients honour it.
        api_response = api_instance.get_world_capability_catalogue()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_capability_catalogue: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCapabilityCatalogueResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_capability_wear**
> GetWorldCapabilityWearResponse get_world_capability_wear()

What you wear from your NFTs and COSM copies: your pick per avatar slot (head, body, legs, feet, back) and what the room sees.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_capability_wear_response import GetWorldCapabilityWearResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What you wear from your NFTs and COSM copies: your pick per avatar slot (head, body, legs, feet, back) and what the room sees.
        api_response = api_instance.get_world_capability_wear()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_capability_wear: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCapabilityWearResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_chest**
> GetWorldChestResponse get_world_chest()

The Commons chest: data.window (this 20-minute window, UTC), spot ([x, z] on the plaza), endsAt (when the next chest comes) and mine (openedThis, and opened -- how many windows you have opened one in; the Chest opener pin comes at 10). A chest is opened by walking up to it in Crossly World, never over the API.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_chest_response import GetWorldChestResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Commons chest: data.window (this 20-minute window, UTC), spot ([x, z] on the plaza), endsAt (when the next chest comes) and mine (openedThis, and opened -- how many windows you have opened one in; the Chest opener pin comes at 10). A chest is opened by walking up to it in Crossly World, never over the API.
        api_response = api_instance.get_world_chest()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_chest: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldChestResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_collection_capability**
> GetWorldCollectionCapabilityResponse get_world_collection_capability(chain, contract)

The live capability declaration of a collection (404 when it has none).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_collection_capability_response import GetWorldCollectionCapabilityResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The live capability declaration of a collection (404 when it has none).
        api_response = api_instance.get_world_collection_capability(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_collection_capability: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWorldCollectionCapabilityResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_contest_mine**
> GetWorldContestMineResponse get_world_contest_mine()

Your contest entries (best score, attempts used, payment state) and prizes (granted, or owed until their gate opens).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_contest_mine_response import GetWorldContestMineResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your contest entries (best score, attempts used, payment state) and prizes (granted, or owed until their gate opens).
        api_response = api_instance.get_world_contest_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_contest_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldContestMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_convention**
> GetWorldConventionResponse get_world_convention(id)

One convention. 404 for an unknown or malformed id alike.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_convention_response import GetWorldConventionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One convention. 404 for an unknown or malformed id alike.
        api_response = api_instance.get_world_convention(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_convention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorldConventionResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_cosm_balance**
> GetWorldCosmBalanceResponse get_world_cosm_balance()

Your COSM balance: baseUnits (a STRING -- COSM has 6 decimals and overflows a JSON number), decimals, available (false = COSM is not provisioned on this deployment, not a zero balance).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_cosm_balance_response import GetWorldCosmBalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your COSM balance: baseUnits (a STRING -- COSM has 6 decimals and overflows a JSON number), decimals, available (false = COSM is not provisioned on this deployment, not a zero balance).
        api_response = api_instance.get_world_cosm_balance()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_cosm_balance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCosmBalanceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_crew**
> GetWorldCrewResponse get_world_crew()

Your crew: data.crew is null when you are in none, else its name, tag, join code and whether you own it; data.members lists up to 30 members, each with the public room they are in right now when they chose to be seen by name (else null).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_crew_response import GetWorldCrewResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your crew: data.crew is null when you are in none, else its name, tag, join code and whether you own it; data.members lists up to 30 members, each with the public room they are in right now when they chose to be seen by name (else null).
        api_response = api_instance.get_world_crew()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_crew: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCrewResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_crew_chat**
> WorldResponse get_world_crew_chat()

Your crew chat: data.messages is the last 50 lines (from, name, text, at), kept in memory only, so it starts empty after a restart. 404 when you are in no crew.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.world_response import WorldResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your crew chat: data.messages is the last 50 lines (from, name, text, at), kept in memory only, so it starts empty after a restart. 404 when you are in no crew.
        api_response = api_instance.get_world_crew_chat()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_crew_chat: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**WorldResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_crew_leaderboard**
> GetGameLeaderboardResponse get_world_crew_leaderboard()

The game leaderboards (Price Guess, hunts, speed trades; this week and all time) ranked among your crew only, each member by the name the crew sees. 404 when you are in no crew.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.game.get_game_leaderboard_response import GetGameLeaderboardResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The game leaderboards (Price Guess, hunts, speed trades; this week and all time) ranked among your crew only, each member by the name the crew sees. 404 when you are in no crew.
        api_response = api_instance.get_world_crew_leaderboard()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_crew_leaderboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetGameLeaderboardResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_dm**
> GetWorldDmResponse get_world_dm(user_id)

Your direct-message thread with one friend, oldest first (the last 100 lines: id, from, text, at, mine). Reading it marks their lines read.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_dm_response import GetWorldDmResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your direct-message thread with one friend, oldest first (the last 100 lines: id, from, text, at, mine). Reading it marks their lines read.
        api_response = api_instance.get_world_dm(user_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_dm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**GetWorldDmResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_emote_showable**
> GetWorldEmoteShowableResponse get_world_emote_showable()

The things you own that a show-off emote can hold up.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_emote_showable_response import GetWorldEmoteShowableResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The things you own that a show-off emote can hold up.
        api_response = api_instance.get_world_emote_showable()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_emote_showable: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldEmoteShowableResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_firefly**
> GetWorldFireflyResponse get_world_firefly()

Fireflies on the Commons lawn: data.day (today, UTC), today (fireflies everyone has caught today) and mine (today -- your catches today, up to perDay -- total, all your catches; the Firefly Catcher pin comes at 30 -- and perDay). Fireflies are caught by walking up to a lit one in Crossly World after dark, never over the API, and nothing is spent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_firefly_response import GetWorldFireflyResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fireflies on the Commons lawn: data.day (today, UTC), today (fireflies everyone has caught today) and mine (today -- your catches today, up to perDay -- total, all your catches; the Firefly Catcher pin comes at 30 -- and perDay). Fireflies are caught by walking up to a lit one in Crossly World after dark, never over the API, and nothing is spent.
        api_response = api_instance.get_world_firefly()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_firefly: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldFireflyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_fit_stat**
> GetWorldFitStatResponse get_world_fit_stat()

Your walking storefront, last 7 days: distinct people who tapped \"Shop this\" or \"Offer\" on what you wore, and how many of each. Counts only; nobody is identified.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_fit_stat_response import GetWorldFitStatResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your walking storefront, last 7 days: distinct people who tapped \"Shop this\" or \"Offer\" on what you wore, and how many of each. Counts only; nobody is identified.
        api_response = api_instance.get_world_fit_stat()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_fit_stat: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldFitStatResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_fit_value**
> GetWorldFitValueResponse get_world_fit_value()

What your outfit is worth on the market: cents (sum of each catalogued piece's order-book price -- last sale, else lowest ask), pieces worn, how many were priced, and share (whether you show it on your card).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_fit_value_response import GetWorldFitValueResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What your outfit is worth on the market: cents (sum of each catalogued piece's order-book price -- last sale, else lowest ask), pieces worn, how many were priced, and share (whether you show it on your card).
        api_response = api_instance.get_world_fit_value()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_fit_value: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldFitValueResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_game**
> GetWorldGameResponse get_world_game(id)

One live game: its manifest, its store items and which you own.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_game_response import GetWorldGameResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One live game: its manifest, its store items and which you own.
        api_response = api_instance.get_world_game(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorldGameResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_game_leaderboard**
> GetWorldGameLeaderboardResponse get_world_game_leaderboard(id)

A live game leaderboard, this week and all time, by its manifest scoring (wins, best points, or best time). Only people who chose to be named show by name. scoring is null for a game that keeps no board.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_game_leaderboard_response import GetWorldGameLeaderboardResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A live game leaderboard, this week and all time, by its manifest scoring (wins, best points, or best time). Only people who chose to be named show by name. scoring is null for a game that keeps no board.
        api_response = api_instance.get_world_game_leaderboard(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_game_leaderboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorldGameLeaderboardResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_game_package**
> GetWorldGamePackageResponse get_world_game_package(id)

One of your game packages with every version, its review state and decision note.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_game_package_response import GetWorldGamePackageResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One of your game packages with every version, its review state and decision note.
        api_response = api_instance.get_world_game_package(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_game_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorldGamePackageResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_game_template**
> GetWorldGameTemplateResponse get_world_game_template(kind)

A fresh game package from a template (table, arena, object; collection is an NFT capability declaration), as { path, base64 } files: the world-kit init, for an agent with no local kit. ?id=my-game&name=My Game.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_game_template_response import GetWorldGameTemplateResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    kind = "kind_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A fresh game package from a template (table, arena, object; collection is an NFT capability declaration), as { path, base64 } files: the world-kit init, for an agent with no local kit. ?id=my-game&name=My Game.
        api_response = api_instance.get_world_game_template(kind)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_game_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |

### Return type

**GetWorldGameTemplateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_hall**
> GetWorldHallResponse get_world_hall()

The Hall of Grails in Crossly World: data.exhibition (key, title, blurb, endsAt -- a new one every Monday UTC -- and next, the coming one's title) and data.exhibits, up to twelve real catalogue items in slot order (skuId, name, brand, imageUrl, thumbUrl, retailCents, lowestAskCents, lastSaleCents: the live order book, null when the market has none). The first stands on the centre plinth. Buy, bid or watch an exhibit through the market endpoints with its skuId.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_hall_response import GetWorldHallResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Hall of Grails in Crossly World: data.exhibition (key, title, blurb, endsAt -- a new one every Monday UTC -- and next, the coming one's title) and data.exhibits, up to twelve real catalogue items in slot order (skuId, name, brand, imageUrl, thumbUrl, retailCents, lowestAskCents, lastSaleCents: the live order book, null when the market has none). The first stands on the centre plinth. Buy, bid or watch an exhibit through the market endpoints with its skuId.
        api_response = api_instance.get_world_hall()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_hall: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHallResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_hall_loan**
> GetWorldHallLoanResponse get_world_hall_loan()

Lend to the Hall: this week's exhibition (key, title, categorySlug, endsAt), your loans on show (id, vaultItemId, skuId, name, credit, since) and the vault pieces you can lend (eligible: vaultItemId, skuId, name, imageUrl, grade) -- held in your Crossly vault, not pledged, in the exhibition's category. perMember is how many you may lend each week.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_hall_loan_response import GetWorldHallLoanResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lend to the Hall: this week's exhibition (key, title, categorySlug, endsAt), your loans on show (id, vaultItemId, skuId, name, credit, since) and the vault pieces you can lend (eligible: vaultItemId, skuId, name, imageUrl, grade) -- held in your Crossly vault, not pledged, in the exhibition's category. perMember is how many you may lend each week.
        api_response = api_instance.get_world_hall_loan()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_hall_loan: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHallLoanResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_home_placeable**
> GetWorldHomePlaceableResponse get_world_home_placeable()

What you can place in your home: your items and your furniture.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_home_placeable_response import GetWorldHomePlaceableResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What you can place in your home: your items and your furniture.
        api_response = api_instance.get_world_home_placeable()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_home_placeable: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHomePlaceableResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_hunt**
> GetWorldHuntResponse get_world_hunt()

Your Great Hunt: data.season (id, name, startsAt, endsAt, the title and how many earn it, live), started (you read the first clue), held (keys held, 0-3, always in the order copper, jade, crystal), keys (each with its name, colour, its riddle once it is yours to read, and when you picked it up), and cleared (your rank through the Gate this season, when, and whether you earned the title) or null. Keys are picked up by walking to them in Crossly World; nothing here takes one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_hunt_response import GetWorldHuntResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your Great Hunt: data.season (id, name, startsAt, endsAt, the title and how many earn it, live), started (you read the first clue), held (keys held, 0-3, always in the order copper, jade, crystal), keys (each with its name, colour, its riddle once it is yours to read, and when you picked it up), and cleared (your rank through the Gate this season, when, and whether you earned the title) or null. Keys are picked up by walking to them in Crossly World; nothing here takes one.
        api_response = api_instance.get_world_hunt()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_hunt: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHuntResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_hunt_scoreboard**
> GetWorldHuntScoreboardResponse get_world_hunt_scoreboard()

The Great Hunt Scoreboard, as the monolith in the Commons shows it: data.season (the running season, or the last one between seasons), finishers (the first ten through the Gate in order: rank, name, short, named, at, titled -- a name shows only for somebody who chose to be seen by name in the world, everyone else is \"A player\") and total (everybody through the Gate this season).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_hunt_scoreboard_response import GetWorldHuntScoreboardResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Great Hunt Scoreboard, as the monolith in the Commons shows it: data.season (the running season, or the last one between seasons), finishers (the first ten through the Gate in order: rank, name, short, named, at, titled -- a name shows only for somebody who chose to be seen by name in the world, everyone else is \"A player\") and total (everybody through the Gate this season).
        api_response = api_instance.get_world_hunt_scoreboard()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_hunt_scoreboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldHuntScoreboardResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_interactive_design**
> GetWorldInteractiveDesignResponse get_world_interactive_design(id)

One of your interactive designs: its draft source, the last static check, and every submitted version with its review state.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_interactive_design_response import GetWorldInteractiveDesignResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One of your interactive designs: its draft source, the last static check, and every submitted version with its review state.
        api_response = api_instance.get_world_interactive_design(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_interactive_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorldInteractiveDesignResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_job**
> GetWorldJobResponse get_world_job()

The jobs board: open staff shifts you could claim, your claimed shifts and open price checks (appraisals), as the world shows them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_job_response import GetWorldJobResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The jobs board: open staff shifts you could claim, your claimed shifts and open price checks (appraisals), as the world shows them.
        api_response = api_instance.get_world_job()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_job: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldJobResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_kite**
> GetWorldKiteResponse get_world_kite()

Kites flown on the Commons lawn: data.day (today, UTC), today (kites everyone has flown today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have flown one on; the Kite flyer pin comes at 5). Kites are flown by standing out on the lawn in Crossly World by day, never over the API, and nothing is spent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_kite_response import GetWorldKiteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Kites flown on the Commons lawn: data.day (today, UTC), today (kites everyone has flown today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have flown one on; the Kite flyer pin comes at 5). Kites are flown by standing out on the lawn in Crossly World by day, never over the API, and nothing is spent.
        api_response = api_instance.get_world_kite()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_kite: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldKiteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_lantern**
> GetWorldKiteResponse get_world_lantern()

Sky lanterns in the Commons: data.day (today, UTC), today (lanterns everyone has released today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have released one on; the Lantern lighter pin comes at 5). Lanterns are released at the lantern stand in Crossly World, never over the API, and nothing is spent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_kite_response import GetWorldKiteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sky lanterns in the Commons: data.day (today, UTC), today (lanterns everyone has released today) and mine (today -- yours today, up to perDay -- perDay, and days -- the days you have released one on; the Lantern lighter pin comes at 5). Lanterns are released at the lantern stand in Crossly World, never over the API, and nothing is spent.
        api_response = api_instance.get_world_lantern()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_lantern: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldKiteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_party_chat**
> WorldResponse get_world_party_chat(id)

Your party chat: the recent lines. 404 when this is not your party.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.world_response import WorldResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your party chat: the recent lines. 404 when this is not your party.
        api_response = api_instance.get_world_party_chat(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_party_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**WorldResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_board**
> GetWorldPlaceBoardResponse get_world_place_board(slug)

The Trade Floor's wall of wants, its authentication desk and its Vault Markets ticker (vaultMovers: bookKey, name, label, units, markCents, change24hBps; only the trade-floor place has them).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_place_board_response import GetWorldPlaceBoardResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The Trade Floor's wall of wants, its authentication desk and its Vault Markets ticker (vaultMovers: bookKey, name, label, units, markCents, change24hBps; only the trade-floor place has them).
        api_response = api_instance.get_world_place_board(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_board: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldPlaceBoardResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_collection**
> GetWorldPlaceCollectionResponse get_world_place_collection(slug, category, brand, model)

One collection room: every piece of the set, owned or missing. 404 for an unknown room or set.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_place_collection_response import GetWorldPlaceCollectionResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    category = "category_example" # str | 
    brand = "brand_example" # str | 
    model = "model_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One collection room: every piece of the set, owned or missing. 404 for an unknown room or set.
        api_response = api_instance.get_world_place_collection(slug, category, brand, model)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **category** | **str**|  |
 **brand** | **str**|  |
 **model** | **str**|  |

### Return type

**GetWorldPlaceCollectionResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_drop**
> GetWorldPlaceDropResponse get_world_place_drop(slug)

The owner's next drop (name, cover, time, live) and how many people are waiting in the room.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_place_drop_response import GetWorldPlaceDropResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The owner's next drop (name, cover, time, live) and how many people are waiting in the room.
        api_response = api_instance.get_world_place_drop(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldPlaceDropResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_item_interest**
> GetWorldPlaceItemInterestResponse get_world_place_item_interest(slug, item_id)

How many people looked at one item in this room today.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_place_item_interest_response import GetWorldPlaceItemInterestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # How many people looked at one item in this room today.
        api_response = api_instance.get_world_place_item_interest(slug, item_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_item_interest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |
 **item_id** | **str**|  |

### Return type

**GetWorldPlaceItemInterestResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_live**
> GetWorldPlaceLiveResponse get_world_place_live(slug)

The owner's live sale: their stream and the lot on the block, or null.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_place_live_response import GetWorldPlaceLiveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The owner's live sale: their stream and the lot on the block, or null.
        api_response = api_instance.get_world_place_live(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_live: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldPlaceLiveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_seller**
> GetWorldPlaceSellerResponse get_world_place_seller(slug)

The shop whose public room this is (username and name), or null.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_place_seller_response import GetWorldPlaceSellerResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The shop whose public room this is (username and name), or null.
        api_response = api_instance.get_world_place_seller(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_seller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldPlaceSellerResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_place_shop_pet**
> GetWorldPlaceShopPetResponse get_world_place_shop_pet(slug)

The shop's pet kind, or null.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_place_shop_pet_response import GetWorldPlaceShopPetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The shop's pet kind, or null.
        api_response = api_instance.get_world_place_shop_pet(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_place_shop_pet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldPlaceShopPetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_space**
> GetWorldSpaceResponse get_world_space(slug)

One Space: its layout, host, events and your place in it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_space_response import GetWorldSpaceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One Space: its layout, host, events and your place in it.
        api_response = api_instance.get_world_space(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetWorldSpaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_space_can_host**
> GetWorldSpaceCanHostResponse get_world_space_can_host()

Whether you may open a Space: sellers only, at most two active.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_space_can_host_response import GetWorldSpaceCanHostResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether you may open a Space: sellers only, at most two active.
        api_response = api_instance.get_world_space_can_host()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_space_can_host: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldSpaceCanHostResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_trial_leaderboard**
> GetWorldTrialLeaderboardResponse get_world_trial_leaderboard(course)

A Time Trials course's boards, as the board beside it in the Commons shows them: data.course, week, weekly (this week's ten fastest: rank, name, short, named, ms, at) and allTime (the ten fastest ever, each person once). A name shows only for somebody who chose to be seen by name in the world; everyone else is \"A player\". 404 for an unknown course; course 1 is commons-loop.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_trial_leaderboard_response import GetWorldTrialLeaderboardResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    course = "course_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A Time Trials course's boards, as the board beside it in the Commons shows them: data.course, week, weekly (this week's ten fastest: rank, name, short, named, ms, at) and allTime (the ten fastest ever, each person once). A name shows only for somebody who chose to be seen by name in the world; everyone else is \"A player\". 404 for an unknown course; course 1 is commons-loop.
        api_response = api_instance.get_world_trial_leaderboard(course)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_trial_leaderboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course** | **str**|  |

### Return type

**GetWorldTrialLeaderboardResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_trial_mine**
> GetWorldTrialMineResponse get_world_trial_mine()

Your Hoverboard Time Trials bests: data.week (its Monday, YYYY-MM-DD, UTC) and courses, each with course (id, name, parMs, rings, lengthM), week (your best lap this week in ms, your place on the weekly board, laps finished, and the split at each ring) or null, and allTime (your best ever in ms, your place on the all-time board, when) or null. Laps are timed by Crossly from where it saw you ride in the world; nothing here writes one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_trial_mine_response import GetWorldTrialMineResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your Hoverboard Time Trials bests: data.week (its Monday, YYYY-MM-DD, UTC) and courses, each with course (id, name, parMs, rings, lengthM), week (your best lap this week in ms, your place on the weekly board, laps finished, and the split at each ring) or null, and allTime (your best ever in ms, your place on the all-time board, when) or null. Laps are timed by Crossly from where it saw you ride in the world; nothing here writes one.
        api_response = api_instance.get_world_trial_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_trial_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldTrialMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_wallet**
> GetWorldWalletResponse get_world_wallet()

Every balance you hold in Crossly World, read-only: bucksCents (Crossly Bucks, cents); cbx (available, decimals, and the three CBX balances kept apart as base-unit STRINGS -- granted (spend here only), earned (withdrawable once matured), connected (a delegation ceiling on your own wallet, not cash on hand) -- plus pendingCents of cashback not yet matured); cosm (available, decimals, baseUnits string). available:false means that currency is not provisioned on this deployment, not that you hold none.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_wallet_response import GetWorldWalletResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Every balance you hold in Crossly World, read-only: bucksCents (Crossly Bucks, cents); cbx (available, decimals, and the three CBX balances kept apart as base-unit STRINGS -- granted (spend here only), earned (withdrawable once matured), connected (a delegation ceiling on your own wallet, not cash on hand) -- plus pendingCents of cashback not yet matured); cosm (available, decimals, baseUnits string). available:false means that currency is not provisioned on this deployment, not that you hold none.
        api_response = api_instance.get_world_wallet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_wallet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldWalletResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_world_wish**
> GetWorldWishResponse get_world_wish()

The Wishing Fountain in the Commons: data.day (today, UTC), today (wishes everyone has made today) and mine (madeToday, days -- how many days you have wished on, the Wishmaker pin comes at 7 -- and nextAt, when tomorrow's wish opens). One wish a day; a wish is made by tossing a coin at the fountain in Crossly World, never over the API, and nothing is spent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_wish_response import GetWorldWishResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Wishing Fountain in the Commons: data.day (today, UTC), today (wishes everyone has made today) and mine (madeToday, days -- how many days you have wished on, the Wishmaker pin comes at 7 -- and nextAt, when tomorrow's wish opens). One wish a day; a wish is made by tossing a coin at the fountain in Crossly World, never over the API, and nothing is spent.
        api_response = api_instance.get_world_wish()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->get_world_wish: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldWishResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_spatial_scene_grants**
> ListSpatialSceneGrantsResponse list_spatial_scene_grants(id)

Everyone who can currently walk into one of your rooms, and unused invites. Never returns codes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.list_spatial_scene_grants_response import ListSpatialSceneGrantsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Everyone who can currently walk into one of your rooms, and unused invites. Never returns codes.
        api_response = api_instance.list_spatial_scene_grants(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_spatial_scene_grants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListSpatialSceneGrantsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_spatial_scene_warehouse_unplaced**
> ListSpatialSceneWarehouseUnplacedResponse list_spatial_scene_warehouse_unplaced(id)

Stock not yet on a shelf in a warehouse room you can arrange (q filters by title).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.list_spatial_scene_warehouse_unplaced_response import ListSpatialSceneWarehouseUnplacedResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Stock not yet on a shelf in a warehouse room you can arrange (q filters by title).
        api_response = api_instance.list_spatial_scene_warehouse_unplaced(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_spatial_scene_warehouse_unplaced: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListSpatialSceneWarehouseUnplacedResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_spatial_shared_with_me**
> ListSpatialSharedWithMeResponse list_spatial_shared_with_me()

Rooms other people let you into.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.list_spatial_shared_with_me_response import ListSpatialSharedWithMeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rooms other people let you into.
        api_response = api_instance.list_spatial_shared_with_me()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_spatial_shared_with_me: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListSpatialSharedWithMeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_spatial_street_leases**
> ListSpatialStreetLeasesResponse list_spatial_street_leases(slug)

Plots on a street offered for lease: weekly rent in CENTS and terms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.list_spatial_street_leases_response import ListSpatialStreetLeasesResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Plots on a street offered for lease: weekly rent in CENTS and terms.
        api_response = api_instance.list_spatial_street_leases(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_spatial_street_leases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListSpatialStreetLeasesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_avatar_closet**
> ListWorldAvatarClosetResponse list_world_avatar_closet()

Everything you can verifiably wear (your Crossly purchase receipts), newest first: receiptId, item title, brand, size, image, catalog sku/variant, quantity, purchasedAt. Pass a receiptId to POST /v1/world/avatar/equip to put one on. limit 1-200, offset for paging.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_avatar_closet_response import ListWorldAvatarClosetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    limit = 1 # int |  (optional)
    offset = 0 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Everything you can verifiably wear (your Crossly purchase receipts), newest first: receiptId, item title, brand, size, image, catalog sku/variant, quantity, purchasedAt. Pass a receiptId to POST /v1/world/avatar/equip to put one on. limit 1-200, offset for paging.
        api_response = api_instance.list_world_avatar_closet(limit=limit, offset=offset)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_avatar_closet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

**ListWorldAvatarClosetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_avatar_stock**
> ListWorldAvatarStockResponse list_world_avatar_stock()

Items of your OWN inventory you could wear into a room as a walking storefront: inventoryItemId, title, image and the slot it would go on. Pass an inventoryItemId to POST /v1/world/avatar/equip.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_avatar_stock_response import ListWorldAvatarStockResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Items of your OWN inventory you could wear into a room as a walking storefront: inventoryItemId, title, image and the slot it would go on. Pass an inventoryItemId to POST /v1/world/avatar/equip.
        api_response = api_instance.list_world_avatar_stock()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_avatar_stock: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldAvatarStockResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_avatar_wearables**
> ListWorldAvatarWearablesResponse list_world_avatar_wearables()

Wearables you have authored as a designer: id, sku, name, slot, priceBaseUnits (COSM base units, a string), maxSupply, mintedCount, active (false until reviewed). meta.available is false when COSM is not provisioned here.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_avatar_wearables_response import ListWorldAvatarWearablesResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wearables you have authored as a designer: id, sku, name, slot, priceBaseUnits (COSM base units, a string), maxSupply, mintedCount, active (false until reviewed). meta.available is false when COSM is not provisioned here.
        api_response = api_instance.list_world_avatar_wearables()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_avatar_wearables: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldAvatarWearablesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_best_dressed**
> ListWorldBestDressedResponse list_world_best_dressed()

This week's best-dressed board (Monday-based), top ten: name, profile username and loves. Only people still choosing to be seen by name.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_best_dressed_response import ListWorldBestDressedResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # This week's best-dressed board (Monday-based), top ten: name, profile username and loves. Only people still choosing to be seen by name.
        api_response = api_instance.list_world_best_dressed()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_best_dressed: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldBestDressedResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_capability_declarations**
> ListWorldCapabilityDeclarationsResponse list_world_capability_declarations()

Your capability declarations, in every review state (pending, live, rejected with the note from the reviewer).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_capability_declarations_response import ListWorldCapabilityDeclarationsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your capability declarations, in every review state (pending, live, rejected with the note from the reviewer).
        api_response = api_instance.list_world_capability_declarations()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_capability_declarations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldCapabilityDeclarationsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_contest_standings**
> ListWorldContestStandingsResponse list_world_contest_standings(id)

The standings of a contest now: best score first (or lowest, for a time game), ties to whoever got there first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_contest_standings_response import ListWorldContestStandingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The standings of a contest now: best score first (or lowest, for a time game), ties to whoever got there first.
        api_response = api_instance.list_world_contest_standings(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_contest_standings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListWorldContestStandingsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_contests**
> ListWorldContestsResponse list_world_contests()

Open skill contests on Crossly World games, soonest ending first: entry mode (free, sponsored, paid) and prizes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_contests_response import ListWorldContestsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open skill contests on Crossly World games, soonest ending first: entry mode (free, sponsored, paid) and prizes.
        api_response = api_instance.list_world_contests()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_contests: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldContestsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_convention_exhibitors**
> ListWorldConventionExhibitorsResponse list_world_convention_exhibitors(id)

The host roster: who applied, who was invited, who is coming (by shop handle). Host only; 404 otherwise.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_convention_exhibitors_response import ListWorldConventionExhibitorsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The host roster: who applied, who was invited, who is coming (by shop handle). Host only; 404 otherwise.
        api_response = api_instance.list_world_convention_exhibitors(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_convention_exhibitors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListWorldConventionExhibitorsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_convention_mine**
> ListWorldConventionMineResponse list_world_convention_mine()

Conventions you host and conventions you are exhibiting at.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_convention_mine_response import ListWorldConventionMineResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Conventions you host and conventions you are exhibiting at.
        api_response = api_instance.list_world_convention_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_convention_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldConventionMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_conventions**
> ListWorldConventionsResponse list_world_conventions()

Conventions open to sellers now or soon: title, room, dates, and how to get a table (invite, free, fee or revenue share).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_conventions_response import ListWorldConventionsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Conventions open to sellers now or soon: title, room, dates, and how to get a table (invite, free, fee or revenue share).
        api_response = api_instance.list_world_conventions()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_conventions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldConventionsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_cosm_cosmetics**
> ListCosmCosmeticsResponse list_world_cosm_cosmetics()

The active cosmetics catalogue, optionally by tier (premium | earned | stake_exclusive) or slot: sku, name, slot, tier, priceCents (premium only), priceBaseUnits (earned only, COSM base units string), supply, fusable, preview and what it unlocks. Read-only: cosmetics are bought on crossly.net. meta.available / meta.decimals.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_cosmetics_response import ListCosmCosmeticsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    tier = "premium" # str |  (optional)
    slot = "slot_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # The active cosmetics catalogue, optionally by tier (premium | earned | stake_exclusive) or slot: sku, name, slot, tier, priceCents (premium only), priceBaseUnits (earned only, COSM base units string), supply, fusable, preview and what it unlocks. Read-only: cosmetics are bought on crossly.net. meta.available / meta.decimals.
        api_response = api_instance.list_world_cosm_cosmetics(tier=tier, slot=slot)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_cosm_cosmetics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier** | **str**|  | [optional]
 **slot** | **str**|  | [optional]

### Return type

**ListCosmCosmeticsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_cosm_designs**
> ListWorldCosmDesignsResponse list_world_cosm_designs()

Your COSM designs in the world: popularity toward the free chain unlock a popular limited design earns, whether it is on chain, and your opt-out. Declare what a design does with chain cosm and the design id as the contract.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_cosm_designs_response import ListWorldCosmDesignsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your COSM designs in the world: popularity toward the free chain unlock a popular limited design earns, whether it is on chain, and your opt-out. Declare what a design does with chain cosm and the design id as the contract.
        api_response = api_instance.list_world_cosm_designs()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_cosm_designs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldCosmDesignsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_cosm_inventory**
> ListWorldCosmInventoryResponse list_world_cosm_inventory()

Cosmetics you hold, newest first: ownershipId, cosmeticId, sku, name, slot, tier, how it was acquired, bound, edition number, acquiredAt and what it unlocks. Pass a cosmeticId to POST /v1/world/avatar/equip to wear one. meta.available.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_cosm_inventory_response import ListWorldCosmInventoryResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cosmetics you hold, newest first: ownershipId, cosmeticId, sku, name, slot, tier, how it was acquired, bound, edition number, acquiredAt and what it unlocks. Pass a cosmeticId to POST /v1/world/avatar/equip to wear one. meta.available.
        api_response = api_instance.list_world_cosm_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_cosm_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldCosmInventoryResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_catalogue**
> ListWorldDecorCatalogueResponse list_world_decor_catalogue()

The Decor Shop: every active cosmetic grouped by surface (avatar | home | shop | stall | street) and slot -- name, tier, priceCents (premium: the dollar price, paid in CBX at spot) or priceBaseUnits (earned: COSM, base-unit string), edition supply and remaining, tint swatch, preview, what it unlocks, owned + your edition number, and buyWith. Read-only: buying and minting happen on crossly.net/shop/decor. meta.available, meta.mint {open, reason}, meta.cbx {open, reason} (CBX opens at mint), meta.balances (your COSM and CBX, base-unit strings), meta.surfaces. Never sold by card.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_decor_catalogue_response import ListWorldDecorCatalogueResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    surface = "avatar" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # The Decor Shop: every active cosmetic grouped by surface (avatar | home | shop | stall | street) and slot -- name, tier, priceCents (premium: the dollar price, paid in CBX at spot) or priceBaseUnits (earned: COSM, base-unit string), edition supply and remaining, tint swatch, preview, what it unlocks, owned + your edition number, and buyWith. Read-only: buying and minting happen on crossly.net/shop/decor. meta.available, meta.mint {open, reason}, meta.cbx {open, reason} (CBX opens at mint), meta.balances (your COSM and CBX, base-unit strings), meta.surfaces. Never sold by card.
        api_response = api_instance.list_world_decor_catalogue(surface=surface)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_catalogue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surface** | **str**|  | [optional]

### Return type

**ListWorldDecorCatalogueResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_designs**
> ListWorldDecorDesignsResponse list_world_decor_designs()

Your decor designs and their review state. available is false until COSM is provisioned.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_decor_designs_response import ListWorldDecorDesignsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your decor designs and their review state. available is false until COSM is provisioned.
        api_response = api_instance.list_world_decor_designs()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_designs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDecorDesignsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_inventory**
> ListWorldDecorInventoryResponse list_world_decor_inventory()

Your decor as an INVENTORY. Decor is a quantity: every copy is one unit -- a placed prop (home_prop, prop) uses one per placement, a finish (wallpaper, floor, theme, shopfront, facade, sign style, street lamp/banner/paving/arch, booth canopy/pattern/lights/counter) one per space it dresses; free values are unlimited. Per item: key, value, pair (key:value), name, sku, surface, placeable, tint, owned, placed, available, placements [{ space { kind: home | shop | stall | street, id, name }, count }], copies [{ ownershipId, editionNumber }]. meta.available, meta.spaces (every space you dress). Read-only: placing and retracting happen in the app or on crossly.net.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_decor_inventory_response import ListWorldDecorInventoryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your decor as an INVENTORY. Decor is a quantity: every copy is one unit -- a placed prop (home_prop, prop) uses one per placement, a finish (wallpaper, floor, theme, shopfront, facade, sign style, street lamp/banner/paving/arch, booth canopy/pattern/lights/counter) one per space it dresses; free values are unlimited. Per item: key, value, pair (key:value), name, sku, surface, placeable, tint, owned, placed, available, placements [{ space { kind: home | shop | stall | street, id, name }, count }], copies [{ ownershipId, editionNumber }]. meta.available, meta.spaces (every space you dress). Read-only: placing and retracting happen in the app or on crossly.net.
        api_response = api_instance.list_world_decor_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDecorInventoryResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_market**
> ListWorldDecorMarketResponse list_world_decor_market()

Decor copies other people are reselling (asks in COSM); optional pair filter. Read only: listing and buying stay on crossly.net.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_decor_market_response import ListWorldDecorMarketResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Decor copies other people are reselling (asks in COSM); optional pair filter. Read only: listing and buying stay on crossly.net.
        api_response = api_instance.list_world_decor_market()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_market: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDecorMarketResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_mine**
> ListWorldDecorMineResponse list_world_decor_mine()

Decor you hold AND decor you have minted to your wallet, newest first: ownershipId, cosmeticId, sku, name, surface, slot, tier, acquiredVia, bound, editionNumber of maxSupply, mintState (held | minting | minted), mintAddress, mintable, and what it unlocks. meta.available, meta.mint.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_decor_mine_response import ListWorldDecorMineResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Decor you hold AND decor you have minted to your wallet, newest first: ownershipId, cosmeticId, sku, name, surface, slot, tier, acquiredVia, bound, editionNumber of maxSupply, mintState (held | minting | minted), mintAddress, mintable, and what it unlocks. meta.available, meta.mint.
        api_response = api_instance.list_world_decor_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDecorMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_stalls**
> ListStallMineResponse list_world_decor_stalls()

Your stall bookings, to dress their booths.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.stall.list_stall_mine_response import ListStallMineResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your stall bookings, to dress their booths.
        api_response = api_instance.list_world_decor_stalls()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_stalls: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListStallMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_decor_streets**
> ListWorldDecorStreetsResponse list_world_decor_streets()

Streets you may dress.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_decor_streets_response import ListWorldDecorStreetsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Streets you may dress.
        api_response = api_instance.list_world_decor_streets()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_decor_streets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDecorStreetsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_dms**
> ListWorldDmsResponse list_world_dms()

Your friends (mutual follows) for direct messages: each with userId, name, the last line between you (text, at, mine) or null, and how many of theirs you have not read; most recent first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_dms_response import ListWorldDmsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your friends (mutual follows) for direct messages: each with userId, name, the last line between you (text, at, mine) or null, and how many of theirs you have not read; most recent first.
        api_response = api_instance.list_world_dms()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_dms: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldDmsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_following_rooms**
> ListWorldFollowingRoomsResponse list_world_following_rooms()

The public rooms of people you follow, to walk into.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_following_rooms_response import ListWorldFollowingRoomsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The public rooms of people you follow, to walk into.
        api_response = api_instance.list_world_following_rooms()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_following_rooms: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldFollowingRoomsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_follows**
> ListWorldFollowsResponse list_world_follows()

Everybody you follow in Crossly World, newest first, each with mutual: true when they follow you back (a friend).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_follows_response import ListWorldFollowsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Everybody you follow in Crossly World, newest first, each with mutual: true when they follow you back (a friend).
        api_response = api_instance.list_world_follows()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_follows: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldFollowsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_friend_here**
> ListWorldFriendsResponse list_world_friend_here()

Your friends in Crossly World right now, and where (when they share it).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_friends_response import ListWorldFriendsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your friends in Crossly World right now, and where (when they share it).
        api_response = api_instance.list_world_friend_here()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_friend_here: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldFriendsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_friends**
> ListWorldFriendsResponse list_world_friends()

Your friends (mutual follows), each with the PUBLIC room they are in right now when they chose to be seen by name there (else null), and their home address slug when they let friends visit. Invisible and anonymous friends are never located.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_friends_response import ListWorldFriendsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your friends (mutual follows), each with the PUBLIC room they are in right now when they chose to be seen by name there (else null), and their home address slug when they let friends visit. Invisible and anonymous friends are never located.
        api_response = api_instance.list_world_friends()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_friends: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldFriendsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_game_packages**
> ListWorldGamePackagesResponse list_world_game_packages()

Your game packages, each with its latest version and review state.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_game_packages_response import ListWorldGamePackagesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your game packages, each with its latest version and review state.
        api_response = api_instance.list_world_game_packages()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_game_packages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldGamePackagesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_game_rewards**
> ListWorldGameRewardsResponse list_world_game_rewards()

Rewards you won in games: granted, or recorded as unfunded for COSM and CBX (a game prints no value).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_game_rewards_response import ListWorldGameRewardsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rewards you won in games: granted, or recorded as unfunded for COSM and CBX (a game prints no value).
        api_response = api_instance.list_world_game_rewards()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_game_rewards: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldGameRewardsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_games**
> ListWorldGamesResponse list_world_games()

The Game Directory: every live, reviewed game package with its players, places, rewards, contests and the piece people place.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_games_response import ListWorldGamesResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Game Directory: every live, reviewed game package with its players, places, rewards, contests and the piece people place.
        api_response = api_instance.list_world_games()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_games: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldGamesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_home_building**
> ListWorldHomeBuildingResponse list_world_home_building()

Homes whose owner made you a co-builder.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_home_building_response import ListWorldHomeBuildingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Homes whose owner made you a co-builder.
        api_response = api_instance.list_world_home_building()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_home_building: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldHomeBuildingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_interactive_catalogue**
> ListWorldInteractiveCatalogueResponse list_world_interactive_catalogue()

Interactive objects: every piece that runs a shared script in a room (first-party and approved creator designs). Per item: model (the piece key a home layout or boutique prop stores), decorValue (the home_prop value its SKU claims), source (first_party | creator), name, blurb, size [x, z] metres, fallbackMesh, cosmeticId (the SKU on the Decor Shop, null when not on sale) and version (a creator design: the approved version every copy runs). Read-only: buying is on crossly.net/shop/decor.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_interactive_catalogue_response import ListWorldInteractiveCatalogueResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Interactive objects: every piece that runs a shared script in a room (first-party and approved creator designs). Per item: model (the piece key a home layout or boutique prop stores), decorValue (the home_prop value its SKU claims), source (first_party | creator), name, blurb, size [x, z] metres, fallbackMesh, cosmeticId (the SKU on the Decor Shop, null when not on sale) and version (a creator design: the approved version every copy runs). Read-only: buying is on crossly.net/shop/decor.
        api_response = api_instance.list_world_interactive_catalogue()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_interactive_catalogue: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldInteractiveCatalogueResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_interactive_designs**
> ListWorldInteractiveDesignsResponse list_world_interactive_designs()

Your interactive-object designs (MML documents you wrote), newest first: id, handle, name, footprint (s | m | l | f), tint, priceBaseUnits (COSM, base-unit string), maxSupply, model, decorValue, cosmeticId, liveVersion (the approved version every copy runs; null = none), withdrawnReason, archivedAt (you archived it: off sale, owned copies keep running; null = not archived), latestVersion { version, state: pending | approved | rejected | withdrawn | cancelled, decisionNote }, inReview. `archived`: exclude (default), include or only archived designs. Read-only: writing, previewing, submitting and archiving happen on crossly.net/shop/decor?tab=interactive.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_interactive_designs_response import ListWorldInteractiveDesignsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    archived = "exclude" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your interactive-object designs (MML documents you wrote), newest first: id, handle, name, footprint (s | m | l | f), tint, priceBaseUnits (COSM, base-unit string), maxSupply, model, decorValue, cosmeticId, liveVersion (the approved version every copy runs; null = none), withdrawnReason, archivedAt (you archived it: off sale, owned copies keep running; null = not archived), latestVersion { version, state: pending | approved | rejected | withdrawn | cancelled, decisionNote }, inReview. `archived`: exclude (default), include or only archived designs. Read-only: writing, previewing, submitting and archiving happen on crossly.net/shop/decor?tab=interactive.
        api_response = api_instance.list_world_interactive_designs(archived=archived)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_interactive_designs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archived** | **str**|  | [optional]

### Return type

**ListWorldInteractiveDesignsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_job_posted**
> ListJobShiftsResponse list_world_job_posted()

Shifts you posted for your rooms, with who claimed each and how it went.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.list_job_shifts_response import ListJobShiftsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Shifts you posted for your rooms, with who claimed each and how it went.
        api_response = api_instance.list_world_job_posted()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_job_posted: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListJobShiftsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_outfits**
> ListWorldOutfitsResponse list_world_outfits()

Your saved outfits (up to 6, oldest first): id, name, appearance (skin, hair, hairColour, eyes, build) and items -- each worn thing as the door it goes back on by (slot, door: cosmetic | receipt | stock, id, label). Put one on with POST /v1/world/outfits/:id/apply.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_outfits_response import ListWorldOutfitsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your saved outfits (up to 6, oldest first): id, name, appearance (skin, hair, hairColour, eyes, build) and items -- each worn thing as the door it goes back on by (slot, door: cosmetic | receipt | stock, id, label). Put one on with POST /v1/world/outfits/:id/apply.
        api_response = api_instance.list_world_outfits()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_outfits: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldOutfitsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_bans**
> ListWorldPlaceBansResponse list_world_place_bans(slug)

Who is banned from a place you own (your boutique or home).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_place_bans_response import ListWorldPlaceBansResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Who is banned from a place you own (your boutique or home).
        api_response = api_instance.list_world_place_bans(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_bans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceBansResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_bundles**
> ListWorldPlaceBundlesResponse list_world_place_bundles(slug)

The owner's bundle deals mapped onto this room's items (itemIds null = any N from the shop). The discount is decided at checkout.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_place_bundles_response import ListWorldPlaceBundlesResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The owner's bundle deals mapped onto this room's items (itemIds null = any N from the shop). The discount is decided at checkout.
        api_response = api_instance.list_world_place_bundles(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceBundlesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_collections**
> ListWorldPlaceCollectionsResponse list_world_place_collections(slug)

The owner's collection rooms: one per category, brand and model they collect.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_place_collections_response import ListWorldPlaceCollectionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The owner's collection rooms: one per category, brand and model they collect.
        api_response = api_instance.list_world_place_collections(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceCollectionsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_offers**
> ListWorldPlaceOffersResponse list_world_place_offers(slug)

What is for sale in a public room: price, condition and stock, with market references. 404 when no such room is shared.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_place_offers_response import ListWorldPlaceOffersResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What is for sale in a public room: price, condition and stock, with market references. 404 when no such room is shared.
        api_response = api_instance.list_world_place_offers(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_offers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceOffersResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_radar**
> ListWorldPlaceRadarResponse list_world_place_radar(slug)

What you have that someone here wants, and what is here that you want: matched on catalog ids.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_place_radar_response import ListWorldPlaceRadarResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What you have that someone here wants, and what is here that you want: matched on catalog ids.
        api_response = api_instance.list_world_place_radar(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_radar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceRadarResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_trade_tables**
> ListWorldPlaceTradeTablesResponse list_world_place_trade_tables(slug)

The open trade tables in a place: who is sitting and what is laid on the mat.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_place_trade_tables_response import ListWorldPlaceTradeTablesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The open trade tables in a place: who is sitting and what is laid on the mat.
        api_response = api_instance.list_world_place_trade_tables(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_trade_tables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceTradeTablesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_place_trades**
> ListWorldPlaceTradesResponse list_world_place_trades(slug)

Items in this room open to trades, each with its trade post path.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_place_trades_response import ListWorldPlaceTradesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Items in this room open to trades, each with its trade post path.
        api_response = api_instance.list_world_place_trades(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_place_trades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldPlaceTradesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_provenance**
> ListWorldProvenanceResponse list_world_provenance()

Provenance trails: where in Crossly World your purchases were found, newest first (optionally ?listingIds=a,b -- platform listing ids). data: [{ platformListingId, slug (the listing public slug), kind (room | window | stall | space | drop | auction | worn | agent), place (its name, or null when gone), at, line -- e.g. \"Found at The Sneaker Vault, Oct 2026\" }]. Yours only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_provenance_response import ListWorldProvenanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Provenance trails: where in Crossly World your purchases were found, newest first (optionally ?listingIds=a,b -- platform listing ids). data: [{ platformListingId, slug (the listing public slug), kind (room | window | stall | space | drop | auction | worn | agent), place (its name, or null when gone), at, line -- e.g. \"Found at The Sneaker Vault, Oct 2026\" }]. Yours only.
        api_response = api_instance.list_world_provenance()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_provenance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldProvenanceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_quests**
> ListWorldQuestsResponse list_world_quests()

Every world quest with your progress: key, the pin it earns, goal, target, count, done, colour. meta.wearing is the pin on your nameplate (or null); meta.streak your current and best daily visit streak. Progress only comes from what the server saw -- there is no write of it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_quests_response import ListWorldQuestsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Every world quest with your progress: key, the pin it earns, goal, target, count, done, colour. meta.wearing is the pin on your nameplate (or null); meta.streak your current and best daily visit streak. Progress only comes from what the server saw -- there is no write of it.
        api_response = api_instance.list_world_quests()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_quests: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldQuestsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_space_mine**
> ListWorldSpacesResponse list_world_space_mine()

Spaces you belong to.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_spaces_response import ListWorldSpacesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Spaces you belong to.
        api_response = api_instance.list_world_space_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_space_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldSpacesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_space_requests**
> ListWorldSpaceRequestsResponse list_world_space_requests(slug)

As host or co-host, who asked to join.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_space_requests_response import ListWorldSpaceRequestsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host or co-host, who asked to join.
        api_response = api_instance.list_world_space_requests(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_space_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListWorldSpaceRequestsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_space_whats_on**
> ListWorldSpaceWhatsOnResponse list_world_space_whats_on()

Live and upcoming events across Spaces (streets=1 and stage=1 add street and Main Stage events).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_space_whats_on_response import ListWorldSpaceWhatsOnResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Live and upcoming events across Spaces (streets=1 and stage=1 add street and Main Stage events).
        api_response = api_instance.list_world_space_whats_on()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_space_whats_on: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldSpaceWhatsOnResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_spaces**
> ListWorldSpacesResponse list_world_spaces()

The Spaces directory: seller-hosted clubs with a venue, members and events (optional venue filter).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_spaces_response import ListWorldSpacesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Spaces directory: seller-hosted clubs with a venue, members and events (optional venue filter).
        api_response = api_instance.list_world_spaces()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_spaces: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldSpacesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_streaks**
> ListWorldStreaksResponse list_world_streaks()

The longest current daily visit streaks (2+ days), top ten: name and days. Only people still choosing to be seen by name.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_streaks_response import ListWorldStreaksResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The longest current daily visit streaks (2+ days), top ten: name and days. Only people still choosing to be seen by name.
        api_response = api_instance.list_world_streaks()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_streaks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldStreaksResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_trade_mine**
> ListWorldTradeMineResponse list_world_trade_mine()

Your trades and each item progress through the authentication gate (verified or failed).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_trade_mine_response import ListWorldTradeMineResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your trades and each item progress through the authentication gate (verified or failed).
        api_response = api_instance.list_world_trade_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_trade_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldTradeMineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_trade_table_binder**
> ListWorldTradeTableBinderResponse list_world_trade_table_binder()

Your binder: unsold collection rows that are catalog items and may be laid on a trade mat -- key, variantId, condition, grade, portfolioId, name, image and valueCents (market value, cents).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_trade_table_binder_response import ListWorldTradeTableBinderResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your binder: unsold collection rows that are catalog items and may be laid on a trade mat -- key, variantId, condition, grade, portfolioId, name, image and valueCents (market value, cents).
        api_response = api_instance.list_world_trade_table_binder()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_trade_table_binder: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldTradeTableBinderResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_world_trade_table_listings**
> ListWorldTradeTableListingsResponse list_world_trade_table_listings()

Your open Trade Block trade listings a trade table can be opened on in the world, each with its items' names.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.list_world_trade_table_listings_response import ListWorldTradeTableListingsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your open Trade Block trade listings a trade table can be opened on in the world, each with its items' names.
        api_response = api_instance.list_world_trade_table_listings()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->list_world_trade_table_listings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldTradeTableListingsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_scene_cosmetic**
> UpdateSpatialSceneCosmeticResponse update_spatial_scene_cosmetic(id)

Redecorate one of your rooms (wall, floor, lighting, trim...). Unknown keys are dropped; the response is what survived. `clear` lists keys to reset.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.update_spatial_scene_cosmetic_response import UpdateSpatialSceneCosmeticResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Redecorate one of your rooms (wall, floor, lighting, trim...). Unknown keys are dropped; the response is what survived. `clear` lists keys to reset.
        api_response = api_instance.update_spatial_scene_cosmetic(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_scene_cosmetic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateSpatialSceneCosmeticResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_scene_node**
> UpdateSpatialSceneNodeResponse update_spatial_scene_node(id, node_id)

Move a rack in one of your warehouse rooms (position in metres).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.update_spatial_scene_node_response import UpdateSpatialSceneNodeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    node_id = "nodeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Move a rack in one of your warehouse rooms (position in metres).
        api_response = api_instance.update_spatial_scene_node(id, node_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_scene_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **node_id** | **str**|  |

### Return type

**UpdateSpatialSceneNodeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_scene_setting**
> SpatialSceneResponse2 update_spatial_scene_setting(id)

How one of your rooms is laid out and lit: grouping and sort keys, theme, overlay and the arrival camera. Cosmetics and the shop layout have their own writers.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.common.spatial_scene_response2 import SpatialSceneResponse2
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # How one of your rooms is laid out and lit: grouping and sort keys, theme, overlay and the arrival camera. Cosmetics and the shop layout have their own writers.
        api_response = api_instance.update_spatial_scene_setting(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_scene_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**SpatialSceneResponse2**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_scene_shop_layout**
> UpdateSpatialSceneShopLayoutResponse update_spatial_scene_shop_layout(id)

Save your shop room's sections and displays (validated server-side; the response is the stored layout).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.update_spatial_scene_shop_layout_response import UpdateSpatialSceneShopLayoutResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save your shop room's sections and displays (validated server-side; the response is the stored layout).
        api_response = api_instance.update_spatial_scene_shop_layout(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_scene_shop_layout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateSpatialSceneShopLayoutResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_scene_window**
> UpdateSpatialSceneWindowResponse update_spatial_scene_window(id)

Choose up to three of your live Crossly listings for the street window of your shop, in slot order. Picks that sell drop out and the newest fill in; an empty list goes back to newest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.spatial.update_spatial_scene_window_response import UpdateSpatialSceneWindowResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Choose up to three of your live Crossly listings for the street window of your shop, in slot order. Picks that sell drop out and the newest fill in; an empty list goes back to newest first.
        api_response = api_instance.update_spatial_scene_window(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_scene_window: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateSpatialSceneWindowResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_street_decor**
> GetSpatialStreetDecorResponse update_spatial_street_decor(slug)

Dress a street you own with decor you hold (validated against your inventory).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.spatial.get_spatial_street_decor_response import GetSpatialStreetDecorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dress a street you own with decor you hold (validated against your inventory).
        api_response = api_instance.update_spatial_street_decor(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_street_decor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetSpatialStreetDecorResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_spatial_street_owned**
> SpatialStreetResponse update_spatial_street_owned(id)

Who may open a shop on a street you own (open, apply or invite).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.spatial_street_response import SpatialStreetResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Who may open a shop on a street you own (open, apply or invite).
        api_response = api_instance.update_spatial_street_owned(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_spatial_street_owned: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**SpatialStreetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_auto_shop**
> GetWorldAutoShopResponse update_world_auto_shop(update_world_auto_shop_request)

Turn your automatic world shop off ({ enabled: false } -- an auto-created shop is made private, never deleted) or back on. Answers the new status.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_auto_shop_response import GetWorldAutoShopResponse
from crossly.model.world.update_world_auto_shop_request import UpdateWorldAutoShopRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    update_world_auto_shop_request = UpdateWorldAutoShopRequest(
        enabled=True,
    ) # UpdateWorldAutoShopRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Turn your automatic world shop off ({ enabled: false } -- an auto-created shop is made private, never deleted) or back on. Answers the new status.
        api_response = api_instance.update_world_auto_shop(update_world_auto_shop_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_auto_shop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_world_auto_shop_request** | **UpdateWorldAutoShopRequest**|  |

### Return type

**GetWorldAutoShopResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_avatar_identity**
> UpdateWorldAvatarIdentityResponse update_world_avatar_identity()

Choose named or anonymous. Rooms you are already in keep the old answer until you rejoin.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_avatar_identity_response import UpdateWorldAvatarIdentityResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Choose named or anonymous. Rooms you are already in keep the old answer until you rejoin.
        api_response = api_instance.update_world_avatar_identity()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_avatar_identity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**UpdateWorldAvatarIdentityResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_avatar_look**
> UpdateWorldAvatarLookResponse update_world_avatar_look()

Save your world look to the account, so every device starts from it. look: null stays anonymous.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_avatar_look_response import UpdateWorldAvatarLookResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Save your world look to the account, so every device starts from it. look: null stays anonymous.
        api_response = api_instance.update_world_avatar_look()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_avatar_look: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**UpdateWorldAvatarLookResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_avatar_nft_badge**
> GetWorldAvatarNftBadgeResponse update_world_avatar_nft_badge()

Wear an NFT you hold on your nameplate (null to take it off). Checked again each time you join a room.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_avatar_nft_badge_response import GetWorldAvatarNftBadgeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wear an NFT you hold on your nameplate (null to take it off). Checked again each time you join a room.
        api_response = api_instance.update_world_avatar_nft_badge()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_avatar_nft_badge: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldAvatarNftBadgeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_capability_wear**
> GetWorldCapabilityWearResponse update_world_capability_wear()

Wear a held token on an avatar slot (refId from GET /v1/world/capabilities), or pass refId null to take it off. Its collection must declare a wear capability for that slot.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_capability_wear_response import GetWorldCapabilityWearResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wear a held token on an avatar slot (refId from GET /v1/world/capabilities), or pass refId null to take it off. Its collection must declare a wear capability for that slot.
        api_response = api_instance.update_world_capability_wear()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_capability_wear: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldCapabilityWearResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_collection_capability**
> GetWorldCollectionCapabilityResponse update_world_collection_capability(chain, contract)

Declare what the tokens of a collection can do (the whole declaration, spec crossly.nft-capabilities/1). As its creator (launched on Crossly or claimed) any kind; as a holder, cosmetic kinds only. Replaces your previous declaration; pending if it names an uploaded asset or an always-reviewed kind.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.get_world_collection_capability_response import GetWorldCollectionCapabilityResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Declare what the tokens of a collection can do (the whole declaration, spec crossly.nft-capabilities/1). As its creator (launched on Crossly or claimed) any kind; as a holder, cosmetic kinds only. Replaces your previous declaration; pending if it names an uploaded asset or an always-reviewed kind.
        api_response = api_instance.update_world_collection_capability(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_collection_capability: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWorldCollectionCapabilityResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_convention_status**
> UpdateWorldConventionStatusResponse update_world_convention_status(id)

Open, start, end or cancel a convention you host.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_convention_status_response import UpdateWorldConventionStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Open, start, end or cancel a convention you host.
        api_response = api_instance.update_world_convention_status(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_convention_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWorldConventionStatusResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_cosm_design_chain_auto_unlock**
> CreateCosmDesignerChainAutoUnlockResponse update_world_cosm_design_chain_auto_unlock(id)

Opt one of your COSM designs in or out of the free chain unlock it earns when popular (on by default). Answers its popularity.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_designer_chain_auto_unlock_response import CreateCosmDesignerChainAutoUnlockResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Opt one of your COSM designs in or out of the free chain unlock it earns when popular (on by default). Answers its popularity.
        api_response = api_instance.update_world_cosm_design_chain_auto_unlock(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_cosm_design_chain_auto_unlock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmDesignerChainAutoUnlockResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_emote_wheel**
> UpdateWorldEmoteWheelResponse update_world_emote_wheel(update_world_emote_wheel_request)

Arrange your emote wheel: up to 8 slots, each an emote id, a moment slot or null. Returns the saved wheel (locked or unknown ids are dropped).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_emote_wheel_response import UpdateWorldEmoteWheelResponse
from crossly.model.world.update_world_emote_wheel_request import UpdateWorldEmoteWheelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    update_world_emote_wheel_request = UpdateWorldEmoteWheelRequest(
        wheel=[
            "wheel_example",
        ],
    ) # UpdateWorldEmoteWheelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Arrange your emote wheel: up to 8 slots, each an emote id, a moment slot or null. Returns the saved wheel (locked or unknown ids are dropped).
        api_response = api_instance.update_world_emote_wheel(update_world_emote_wheel_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_emote_wheel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_world_emote_wheel_request** | **UpdateWorldEmoteWheelRequest**|  |

### Return type

**UpdateWorldEmoteWheelResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_fit_value_share**
> UpdateWorldFitValueShareResponse update_world_fit_value_share()

Whether people in a room can see what your outfit is worth.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_fit_value_share_response import UpdateWorldFitValueShareResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether people in a room can see what your outfit is worth.
        api_response = api_instance.update_world_fit_value_share()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_fit_value_share: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**UpdateWorldFitValueShareResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_home**
> WorldHomeResponse update_world_home()

Your home: privacy (open, friends, private), theme, and wall, floor and mood decor you hold.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.world_home_response import WorldHomeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your home: privacy (open, friends, private), theme, and wall, floor and mood decor you hold.
        api_response = api_instance.update_world_home()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_home: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**WorldHomeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_home_builder**
> UpdateWorldHomeBuilderResponse update_world_home_builder(update_world_home_builder_request)

Set the co-builders of your home: { userIds } -- friends (mutual follows) only, at most 4, replacing the list ([] clears it). They may rearrange your home in the world with your things and add free furniture, never your bought pieces. New co-builders get a world notice.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_home_builder_response import UpdateWorldHomeBuilderResponse
from crossly.model.world.update_world_home_builder_request import UpdateWorldHomeBuilderRequest
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    update_world_home_builder_request = UpdateWorldHomeBuilderRequest(
        user_ids=[
            "user_ids_example",
        ],
    ) # UpdateWorldHomeBuilderRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set the co-builders of your home: { userIds } -- friends (mutual follows) only, at most 4, replacing the list ([] clears it). They may rearrange your home in the world with your things and add free furniture, never your bought pieces. New co-builders get a world notice.
        api_response = api_instance.update_world_home_builder(update_world_home_builder_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_home_builder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_world_home_builder_request** | **UpdateWorldHomeBuilderRequest**|  |

### Return type

**UpdateWorldHomeBuilderResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_home_layout**
> WorldHomeResponse update_world_home_layout()

Arrange your home: the full layout (up to 200 pieces you own), validated server-side.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.world_home_response import WorldHomeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Arrange your home: the full layout (up to 200 pieces you own), validated server-side.
        api_response = api_instance.update_world_home_layout()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_home_layout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**WorldHomeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_home_layout_by_slug**
> WorldHomeResponse update_world_home_layout_by_slug(slug)

Rearrange a home you co-build (never adding the owner bought pieces).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.world_home_response import WorldHomeResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Rearrange a home you co-build (never adding the owner bought pieces).
        api_response = api_instance.update_world_home_layout_by_slug(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_home_layout_by_slug: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**WorldHomeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_interactive_design_draft**
> UpdateWorldInteractiveDesignDraftResponse update_world_interactive_design_draft(id)

Save the draft MML source (up to 64 KB); the response carries its static check.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_interactive_design_draft_response import UpdateWorldInteractiveDesignDraftResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save the draft MML source (up to 64 KB); the response carries its static check.
        api_response = api_instance.update_world_interactive_design_draft(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_interactive_design_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWorldInteractiveDesignDraftResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_listing_holders_only**
> UpdateWorldListingHoldersOnlyResponse update_world_listing_holders_only(id)

Reserve one of your listings for holders of a collection you declared a holders_only perk for (or release it). Checkout refuses anybody else.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_listing_holders_only_response import UpdateWorldListingHoldersOnlyResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reserve one of your listings for holders of a collection you declared a holders_only perk for (or release it). Checkout refuses anybody else.
        api_response = api_instance.update_world_listing_holders_only(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_listing_holders_only: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWorldListingHoldersOnlyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_outfit**
> UpdateWorldOutfitResponse update_world_outfit(id, update_world_outfit_request)

Rename a saved look: { name (1-32 chars) }. 404 when it is not yours.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_outfit_request import UpdateWorldOutfitRequest
from crossly.model.common.error import Error
from crossly.model.world.update_world_outfit_response import UpdateWorldOutfitResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 
    update_world_outfit_request = UpdateWorldOutfitRequest(
        name="name_example",
    ) # UpdateWorldOutfitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Rename a saved look: { name (1-32 chars) }. 404 when it is not yours.
        api_response = api_instance.update_world_outfit(id, update_world_outfit_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_outfit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_world_outfit_request** | **UpdateWorldOutfitRequest**|  |

### Return type

**UpdateWorldOutfitResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_pet_active**
> UpdateWorldPetActiveResponse update_world_pet_active(update_world_pet_active_request)

Walk one of your pets with you in the world, or none (kind: null).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_pet_active_response import UpdateWorldPetActiveResponse
from crossly.model.world.update_world_pet_active_request import UpdateWorldPetActiveRequest
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    update_world_pet_active_request = UpdateWorldPetActiveRequest(
        kind="cat",
    ) # UpdateWorldPetActiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Walk one of your pets with you in the world, or none (kind: null).
        api_response = api_instance.update_world_pet_active(update_world_pet_active_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_pet_active: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_world_pet_active_request** | **UpdateWorldPetActiveRequest**|  |

### Return type

**UpdateWorldPetActiveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_quest_pin**
> UpdateWorldQuestPinResponse update_world_quest_pin(update_world_quest_pin_request)

Wear a pin you EARNED from a quest on your nameplate, or { pin: null } to wear none. 403 for a pin you have not earned. Shows from the next room you walk into.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_quest_pin_request import UpdateWorldQuestPinRequest
from crossly.model.world.update_world_quest_pin_response import UpdateWorldQuestPinResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    update_world_quest_pin_request = UpdateWorldQuestPinRequest(
        pin="pin_example",
    ) # UpdateWorldQuestPinRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Wear a pin you EARNED from a quest on your nameplate, or { pin: null } to wear none. 403 for a pin you have not earned. Shows from the next room you walk into.
        api_response = api_instance.update_world_quest_pin(update_world_quest_pin_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_quest_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_world_quest_pin_request** | **UpdateWorldQuestPinRequest**|  |

### Return type

**UpdateWorldQuestPinResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_room_holder_gate**
> UpdateWorldRoomHolderGateResponse update_world_room_holder_gate(id)

Make your room holders-only (its collection rooms follow). Send null to open it again. Returns `{ gate }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_room_holder_gate_response import UpdateWorldRoomHolderGateResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Make your room holders-only (its collection rooms follow). Send null to open it again. Returns `{ gate }`.
        api_response = api_instance.update_world_room_holder_gate(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_room_holder_gate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWorldRoomHolderGateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_space**
> UpdateWorldSpaceResponse update_world_space(slug)

As host, change a Space name, about or membership.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_space_response import UpdateWorldSpaceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # As host, change a Space name, about or membership.
        api_response = api_instance.update_world_space(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**UpdateWorldSpaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_space_holder_gate**
> UpdateWorldRoomHolderGateResponse update_world_space_holder_gate(slug)

Make your Space holders-only: only holders of an NFT collection join it (others can look in). Send null to open it again. Returns `{ gate }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.world.update_world_room_holder_gate_response import UpdateWorldRoomHolderGateResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Make your Space holders-only: only holders of an NFT collection join it (others can look in). Send null to open it again. Returns `{ gate }`.
        api_response = api_instance.update_world_space_holder_gate(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_space_holder_gate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**UpdateWorldRoomHolderGateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_world_stall_booking_booth**
> UpdateWorldStallBookingBoothResponse update_world_stall_booking_booth(id)

Dress the booth of a stall you booked (decor you hold).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import world_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_stall_booking_booth_response import UpdateWorldStallBookingBoothResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = world_api.WorldApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dress the booth of a stall you booked (decor you hold).
        api_response = api_instance.update_world_stall_booking_booth(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldApi->update_world_stall_booking_booth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWorldStallBookingBoothResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

