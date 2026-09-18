// Zero-dependency example — Node 18+
const url = 'https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112';
const res = await fetch(url);
const report = await res.json();
console.log(report.token.symbol, report.risk.grade, report.risk.score);
