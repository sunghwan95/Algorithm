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
  const [N, M] = inputLines[0].split(" ").map(Number);
  const arr = [];

  const dfs = () => {
    if (arr.length === M) {
      console.log(arr.join(" "));
      return;
    }

    for (let i = 1; i <= N; i++) {
      if (!arr.includes(i)) {
        arr.push(i);
        dfs();
        arr.pop();
      }
    }
  };

  dfs();
});
