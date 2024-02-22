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
  const N = inputLines.shift();
  const queue = [];
  const result = [];
  let removed = false;

  for (let i = 1; i <= N; i++) {
    queue.push(i);
  }

  while (queue.length > 1) {
    if (removed == false) {
      const removedELe = queue.shift();
      result.push(removedELe);
      removed = true;
    } else {
      const movedEle = queue.shift();
      queue.push(movedEle);
      removed = false;
    }
  }

  const answer = result.concat(queue);

  console.log(answer.join(" "));
});
