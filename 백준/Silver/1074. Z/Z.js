const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputLines = [];
rl.on("line", (line) => {
  inputLines = line.split(" ").map((e) => Number(e));
});

rl.on("close", () => {
  const N = inputLines[0];
  const r = inputLines[1];
  const c = inputLines[2];

  let ans = 0;

  const recursion = (size, x, y) => {
    if (x === r && y === c) {
      console.log(ans);
      return;
    }

    if (size === 1) {
      ans += 1;
      return;
    }

    if (!(x <= r && r < x + size) && !(y <= c && c < y + size)) {
      ans += size * size;
      return;
    }
    recursion(size / 2, x, y);
    recursion(size / 2, x, y + size / 2);
    recursion(size / 2, x + size / 2, y);
    recursion(size / 2, x + size / 2, y + size / 2);
  };

  recursion(2 ** N, 0, 0);
});
