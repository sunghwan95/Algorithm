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
  const soldiers = inputLines.slice(1);

  const visited = new Array(M).fill(null).map(() => new Array(N).fill(0));

  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  const bfs = (x, y, soldier) => {
    let count = 1;
    const queue = [];
    queue.push([x, y]);
    visited[x][y] = 1;

    while (queue.length > 0) {
      [x, y] = queue.shift();

      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (nx >= 0 && ny >= 0 && nx < M && ny < N) {
          if (soldiers[nx][ny] === soldier && visited[nx][ny] === 0) {
            visited[nx][ny] = 1;
            queue.push([nx, ny]);
            count++;
          }
        }
      }
    }
    return count;
  };

  let white = 0;
  let blue = 0;

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (soldiers[i][j] === "W" && visited[i][j] === 0) {
        white += Math.pow(bfs(i, j, "W"), 2);
      } else if (soldiers[i][j] === "B" && visited[i][j] === 0) {
        blue += Math.pow(bfs(i, j, "B"), 2);
      }
    }
  }

  console.log(`${white} ${blue}`);
});
