const INF = Math.pow(2, 31) - 1;

/**
 * @param {number[][]} rooms
 * @return {void} Do not return anything, modify rooms in-place instead.
 */
const wallsAndGates = function (rooms) {
  const rows = rooms.length;
  const cols = rooms[0].length;

  const queue = [];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (rooms[i][j] === 0) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length) {
    const [x, y] = queue.shift();
    const currentValue = rooms[x][y];

    for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const [nx, ny] = [x + dx, y + dy];

      if (
        nx < 0 ||
        ny < 0 ||
        nx >= rows ||
        ny >= cols ||
        rooms[nx][ny] !== INF
      ) {
        continue;
      }

      rooms[nx][ny] = currentValue + 1;

      queue.push([nx, ny]);
    }
  }
};

/*
  You are given an m x n grid rooms initialized with these three possible values.

  * -1 A wall or an obstacle.
  * 0 A gate.
  * INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

  Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
*/

export default wallsAndGates;
