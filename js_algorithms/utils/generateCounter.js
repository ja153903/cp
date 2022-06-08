/**
 * generateCounter creates a frequency counter for any generic array of items
 *
 * @param {any[]} items
 * @return {Map<any, number>}
 */
function generateCounter(items) {
  const counter = new Map();

  for (const item of items) {
    const count = counter.get(item) ?? 0;
    counter.set(item, count + 1);
  }

  return counter;
}

module.exports = generateCounter;
