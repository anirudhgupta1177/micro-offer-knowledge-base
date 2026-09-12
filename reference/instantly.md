# Instantly

Sequences, sending and replies. API v2.

```
BASE   https://api.instantly.ai/api/v2
AUTH   Authorization: Bearer <INSTANTLY_API_KEY>
KEY    Settings > Integrations > API
```

Lists page with **`starting_after`**, carrying the previous page's last id, not
with page numbers. `instantly_lib._page_all()` handles it.

## Routes used here

| Route | Method | For |
| --- | --- | --- |
| `/accounts` | GET | your connected sending addresses |
| `/accounts` | POST | add a mailbox (`provider_code: 2` for Google Workspace) |
| `/campaigns` | GET, POST | list and create. Created paused |
| `/campaigns/{id}` | PATCH | settings and sequence |
| `/leads/list` | POST | add leads to a campaign |
| `/leads/{id}` | GET, PATCH | custom variables live in the `payload` field |
| `/emails/test` | POST | send a test and read it in a real inbox |

## Traps

**`402 Payment Required`** means the workspace behind that key has no active paid
plan. The key is fine. Check which workspace it belongs to.

**Editing a sequence on a live campaign pauses the campaign.** Patch the sequence
before the leads go in.

**Spintax is `{{RANDOM | one | two}}`.** Uppercase, spaces around the pipes. The
`{one|two}` form used by other tools does nothing and sends literal braces.

**Merge tags are camelCase** and always want a fallback. A tag that is not set on
every lead renders empty on every send.

**Open tracking and link tracking are separate flags.** Turning one off does not
turn the other off. Both must be off before launch.

**Verify rendering in a real inbox, not the preview.** The preview is HTML only
and hides spacing problems. `POST /emails/test`, then read the delivered mail.

**Re-touching leads a campaign already contacted** needs a duplicate campaign
plus a move. Re-uploading the same addresses silently does nothing.
