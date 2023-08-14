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
  const safeZone = [];
  for (let i = 1; i <= N; i++) {
    safeZone.push(inputLines[i].split(" ").map(Number));
  }

  const visited = new Array(N).fill(0).map(() => new Array(N).fill(0));

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  function dfs(x, y, rainfall) {
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (
        nx >= 0 &&
        nx < N &&
        ny >= 0 &&
        ny < N &&
        safeZone[nx][ny] > rainfall &&
        visited[nx][ny] === 0
      ) {
        visited[nx][ny] = 1;
        dfs(nx, ny, rainfall);
      }
    }
  }

  const rainfallArray = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      rainfallArray.push(safeZone[i][j]);
    }
  }

  const minRainfall = Math.min(...rainfallArray);
  const maxRainfall = Math.max(...rainfallArray);

  let count = 1;

  for (let rainfall = minRainfall; rainfall < maxRainfall; rainfall++) {
    let _count = 0;
    visited.forEach((row) => row.fill(0));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (safeZone[i][j] > rainfall && visited[i][j] === 0) {
          visited[i][j] = 1;
          dfs(i, j, rainfall);
          _count += 1;
        }
      }
    }
    count = Math.max(count, _count);
  }

  console.log(count);
});
