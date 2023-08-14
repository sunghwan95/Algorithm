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
  const N = parseInt(inputLines[0]);
  const papers = [];
  for (let i = 1; i <= N; i++) {
    const row = inputLines[i].split(" ").map(Number);
    papers.push(row);
  }

  const ans = [];

  function recursion(x, y, size) {
    const color = papers[x][y];
    for (let i = x; i < x + size; i++) {
      for (let j = y; j < y + size; j++) {
        if (color !== papers[i][j]) {
          recursion(x, y, size / 2);
          recursion(x + size / 2, y, size / 2);
          recursion(x, y + size / 2, size / 2);
          recursion(x + size / 2, y + size / 2, size / 2);
          return;
        }
      }
    }

    if (color === 1) {
      ans.push(1);
    } else {
      ans.push(0);
    }
  }

  recursion(0, 0, N);

  const countZeroes = ans.filter((val) => val === 0).length;
  const countOnes = ans.filter((val) => val === 1).length;
  console.log(countZeroes);
  console.log(countOnes);
});
