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
  // 1. 큰 틀에서 1행 1열은 공백이다.
  // 2. 행 과 열을 3등분으로 나눈 후 각 사각형의 중앙도 공백이다.
  // 3. 큰 틀에서 작은 틀까지 똑같은 로직 -> 분할 정복
  // 4. 더 이상 쪼갤 수 없을 때 종료(== 변의 길이가 1)
  // 5. 재귀함수의 인자로 들어가는 건 변의 길이, 중앙을 공백으로 만들기 위한 기준점
  // 6. 3->1, 9->3, 27->9
  const starsArray = new Array(N).fill(null).map(() => new Array(N).fill("*"));

  const recursion = (size, standardRow, standardCol) => {
    if (size === 1) return;

    const emptyStartIdx = size / 3;
    const emptyEndIdx = (size / 3) * 2;

    for (let i = standardRow + emptyStartIdx; i < standardRow + emptyEndIdx; i++) {
      for (let j = standardCol + emptyStartIdx; j < standardCol + emptyEndIdx; j++) {
        starsArray[i][j] = " ";
      }
    }

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (i === 1 && j === 1) continue;
        recursion(
          size / 3,
          standardRow + i * (size / 3),
          standardCol + j * (size / 3)
        );
      }
    }
  };

  recursion(N, 0, 0);

  for (const elem of starsArray) {
    console.log(elem.join(""));
  }
});
