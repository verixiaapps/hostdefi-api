# HostDeFi Token-Safety API

Public docs and client examples for **HostDeFi** — a free, keyless API that
grades any token A+–F from on-chain risk signals across Solana + 7 EVM
chains (Ethereum, BSC, Base, Arbitrum, Optimism, Polygon, Avalanche).

Hosted service — this repo contains docs and examples only.

## Quick start

```bash
curl https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112
```

Returns a JSON risk report: grade, score, mint/freeze authority state,
liquidity depth, holder concentration, contract flags. Keyless and free
(fair-use rate limit); no signup.

## Endpoints

| Surface | URL |
|---|---|
| REST API | `https://hostdefi.com/api/v1/token-risk/{chain}/{address}` |
| Batch | `POST https://hostdefi.com/api/v1/token-risk/batch` |
| Web scanner | https://hostdefi.com/scan |
| MCP server | `https://hostdefi.com/api/v1/mcp` |
| x402 (USDC-paid) | `https://hostdefi.com/api/v1/x402/*` |
| Machine index | https://hostdefi.com/llms.txt |
| OpenAPI spec | [`openapi.json`](./openapi.json) |

## Examples

- [`examples/curl.md`](./examples/curl.md) — one-liners
- [`examples/node.js`](./examples/node.js) — zero-dependency Node client
- [`examples/python.py`](./examples/python.py) — stdlib-only Python client

## Site

[hostdefi.com](https://hostdefi.com) — multi-chain DEX + the safety scanner
this API powers.
