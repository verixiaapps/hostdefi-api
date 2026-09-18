# stdlib-only. Prints: SYMBOL GRADE SCORE verdict
import json, urllib.request
u = 'https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112'
req = urllib.request.Request(u, headers={'User-Agent': 'hostdefi-api-example/1.0'})
r = json.load(urllib.request.urlopen(req))
print(r['token']['symbol'], r['risk']['grade'], r['risk']['score'], '-', r['risk']['verdict'])
