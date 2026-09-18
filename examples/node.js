// Zero-dependency — Node 18+. Prints: SYMBOL GRADE SCORE verdict
const url = 'https://hostdefi.com/api/v1/token-risk/solana/So11111111111111111111111111111111111111112';
const report = await (await fetch(url)).json();
console.log(report.token.symbol, report.risk.grade, report.risk.score, '-', report.risk.verdict);
