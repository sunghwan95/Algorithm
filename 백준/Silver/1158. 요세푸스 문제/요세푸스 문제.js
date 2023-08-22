const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputLines = [];
rl.on("line", (line) => {
  inputLines.push(line);
});

rl.on("close", () => {
  const [N, K] = inputLines[0].split(" ").map(Number);
  const ans = [];
  const arr = Array.from({ length: N }, (_, i) => i + 1);
  let num = 0;

  for (let i = 0; i < N; i++) {
    num += K - 1;
    if (num >= arr.length) {
      num %= arr.length;
    }
    ans.push(arr.splice(num, 1)[0].toString());
  }

  console.log("<" + ans.join(", ") + ">");
});
