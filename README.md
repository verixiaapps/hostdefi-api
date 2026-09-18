# HostDeFi Token-Safety API

Free, keyless token-safety grades (A+–F) for any token across **Solana + 7
EVM chains** — Ethereum, BSC, Base, Arbitrum, Optimism, Polygon, Avalanche.
Structured risk reads: mint/freeze authority, liquidity, holder
concentration, contract flags, and more.

This repo is **documentation and client examples only** — the hosted
service lives at [hostdefi.com](https://hostdefi.com).

- Web scanner: https://hostdefi.com/scan
- Machine-readable index: https://hostdefi.com/llms.txt
- Full OpenAPI 3.1 spec: [`openapi.json`](./openapi.json)
  (also served at `https://hostdefi.com/api/v1/openapi.json`)

## Quick start — free tier, no key, no signup

```bash
curl https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112
```

```jsonc
{
  "ok": true,
  "token": { "chain": "solana", "address": "So1111…", "name": "SOL", "symbol": "SOL" },
  "risk": {
    "graded": true,
    "score": 92,
    "grade": "A+",
    "tier": "low",
    "verdict": "Established, widely-held token."
  },
  "signals": { "authorities": { "mintDisabled": true, "freezeDisabled": true }, "…": "…" },
  "meta": { "plan": "free", "remaining": 98 }
}
```

Fair use: **100 checks/day per IP** (honest 429 beyond that). Responses are
cacheable for 60 s.

## Endpoint map

| Tier | Method + path | What it does |
|---|---|---|
| Free | `GET /api/v1/token-risk/{chain}/{address}` | Risk verdict by chain + address |
| Free | `POST /api/v1/token-risk` | Verdict by free-form query (address or name/ticker) |
| Free | `POST /api/scan` | Contract scanner — alias of `POST /api/analyze-token` |
| Free | `GET /api/v1/health` | Liveness + plan table |
| Keyed | `POST /api/v1/token-risk/batch` | Batch verdicts (Pro/Scale plans) |
| Keyed | `GET /api/v1/usage` | Quota for an API key (`Authorization: Bearer <key>`) |
| x402 | `GET/POST /api/v1/x402/*` | 20+ USDC-per-call resources — deep reports, history, radar, portfolio audits, swap quotes, datasets |
| x402 | `POST /api/v1/x402/keys` | Buy a 30-day API key with one USDC payment |

Chain ids: `solana`, `ethereum`, `bsc`, `base`, `arbitrum`, `optimism`,
`polygon`, `avalanche`.

## MCP server

Hosted MCP endpoint (streamable HTTP):

```
https://hostdefi.com/api/v1/mcp
```

Exposes `scan_token` — the same free scanner, callable from any MCP client.
Client config:

```json
{
  "mcpServers": {
    "hostdefi": { "url": "https://hostdefi.com/api/v1/mcp" }
  }
}
```

## x402

`GET https://hostdefi.com/.well-known/x402` describes the full paid surface.
Every x402 route answers `402 Payment Required` with payment instructions;
pay in USDC on the listed networks and retry with the `X-PAYMENT` header.
Price sheet: `GET /api/v1/x402/pricing`.

## Examples

- [`examples/curl.md`](./examples/curl.md) — one-liners
- [`examples/node.js`](./examples/node.js) — zero-dependency Node client
- [`examples/python.py`](./examples/python.py) — stdlib-only Python client

## Response fields

| Field | Type | Meaning |
|---|---|---|
| `ok` | bool | Call succeeded |
| `token.chain` / `token.address` / `token.name` / `token.symbol` | — | Resolved token identity |
| `risk.graded` | bool | False when the token couldn't be graded (`risk.notGradedReason` says why) |
| `risk.score` | int 0–100 | Higher is safer |
| `risk.grade` | `A+`…`F` | Letter grade derived from the score |
| `risk.tier` | `low`/`medium`/`high`/`extreme` | Risk tier |
| `risk.verdict` | string | One-line human verdict |
| `signals` | object | Raw on-chain/market signals behind the grade (shape varies by chain) |
| `meta.plan` | `free` or plan id | Caller's tier |
| `meta.remaining` | int | Calls left on the caller's tier |
| `meta.partial` | bool | True when an upstream source was unavailable |

## License

MIT — see [LICENSE](./LICENSE).
