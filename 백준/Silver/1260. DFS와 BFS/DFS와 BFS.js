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
  const [N, M, V] = inputLines[0].split(" ").map(Number);
  const graph = new Graph(N);

  for (let i = 1; i <= M; i++) {
    const [a, b] = inputLines[i].split(" ").map(Number);
    graph.addEdge(a, b);
  }

  console.log(graph.dfs(V).join(" "));
  console.log(graph.bfs(V).join(" "));
});

class Graph {
  constructor(N) {
    this.N = N;
    this.adjacencyMatrix = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
    this.visitedDFS = Array(N + 1).fill(false);
    this.visitedBFS = Array(N + 1).fill(false);
  }

  addEdge(i, j) {
    this.adjacencyMatrix[i][j] = 1;
    this.adjacencyMatrix[j][i] = 1;
  }

  dfs(V) {
    this.visitedDFS[V] = true;
    const result = [V];

    for (let i = 1; i <= this.N; i++) {
      if (this.adjacencyMatrix[V][i] === 1 && !this.visitedDFS[i]) {
        result.push(...this.dfs(i));
      }
    }
    return result;
  }

  bfs(V) {
    let queue = [V];
    this.visitedBFS[V] = true;
    const result = [];

    while (queue.length > 0) {
      const node = queue.shift();
      result.push(node);

      for (let i = 1; i <= this.N; i++) {
        if (this.adjacencyMatrix[node][i] === 1 && !this.visitedBFS[i]) {
          queue.push(i);
          this.visitedBFS[i] = true;
        }
      }
    }
    return result;
  }
}
