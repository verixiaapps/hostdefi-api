# stdlib-only example
import json, urllib.request
u = 'https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112'
r = json.load(urllib.request.urlopen(u))
print(r['token']['symbol'], r['risk'].get('grade'), r['risk'].get('score'))
