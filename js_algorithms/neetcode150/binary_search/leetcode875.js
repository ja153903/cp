/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
const minEatingSpeed = function (piles, h) {
  let left = 1;
  let right = Math.max(...piles);

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);

    if (canFinish(piles, mid, h)) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }

  return right;
};

function canFinish(piles, k, h) {
  let result = 0;
  for (let pile of piles) {
    result += Math.floor(pile / k);
    if (pile % k > 0) {
      result++;
    }
  }

  return result <= h;
}

module.exports = { minEatingSpeed };
