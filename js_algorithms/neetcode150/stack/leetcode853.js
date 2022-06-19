/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
const carFleet = function (target, position, speed) {
  const cars = position
    .map((pos, i) => ({
      pos,
      spd: speed[i],
    }))
    .sort((a, b) => {
      return a.pos - b.pos;
    })
    .reverse();
  const stack = [];

  for (const car of cars) {
    // idea here is that we have y = mx + b where
    // y ~ target
    // m ~ car.spd
    // b ~ car.pos
    const x = (target - car.pos) / car.spd;
    if (!stack.length) {
      stack.push(x);
    } else if (stack[stack.length - 1] < x) {
      stack.push(x);
    }
  }

  return stack.length;
};

module.exports = { carFleet };
