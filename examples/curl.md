# curl examples

```bash
# Grade a Solana token (free, keyless)
curl https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112

# Grade an Ethereum token
curl https://hostdefi.com/api/v1/token-risk/ethereum/0xdAC17F958D2ee523a2206206994597C13D831ec7

# Free-form query by name/ticker
curl -X POST https://hostdefi.com/api/v1/token-risk \
  -H 'Content-Type: application/json' \
  -d '{"query":"BONK"}'

# Health / plan table
curl https://hostdefi.com/api/v1/health
```
