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
    // graph 탐색을 위한 2중 배열 생성.
    this.matrix = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
    this.visitedDFS = Array(N + 1).fill(false);
    this.visitedBFS = Array(N + 1).fill(false);
  }

  // 간선 연결
  addEdge(a, b) {
    this.matrix[a][b] = 1;
    this.matrix[b][a] = 1;
  }

  dfs(V) {
    this.visitedDFS[V] = true;
    const result = [V];

    for (let i = 1; i <= this.N; i++) {
      // 간선이 연결되어있고 연결된 노드를 방문하지 않았다면 dfs 재귀호출
      if (this.matrix[V][i] === 1 && !this.visitedDFS[i]) {
        result.push(...this.dfs(i));
      }
    }

    return result;
  }

  bfs(V) {
    // 안접 노드부터 탐색하기 위한 큐 이용.
    const queue = [V];
    this.visitedBFS[V] = true;
    const result = [];

    while (queue.length >= 1) {
      const node = queue.shift();
      result.push(node);

      for (let i = 1; i <= this.N; i++) {
        // node와 연결된 인접한 정점을 방문하지 않았다면
        // for문을 돌면서 인접한 정점을 순차적으로 큐에 넣고 실행
        if (this.matrix[node][i] === 1 && !this.visitedBFS[i]) {
          queue.push(i);
          this.visitedBFS[i] = true;
        }
      }
    }

    return result;
  }
}
