const generateCounter = require('../../utils/generateCounter');
const { PriorityQueue, PrioritizedItem } = require('../../utils/priorityQueue');

/**
 * 347. Top K Frequent Elements
 *
 * Given an integer array nums and an integer k, return the k most frequent elements.
 * You may return the answer in any order.
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
  const counter = generateCounter(nums);
  const priorityQueue = new PriorityQueue();

  for (const [key, value] of counter.entries()) {
    priorityQueue.insert(new PrioritizedItem(value, key));
    if (priorityQueue.size > k) {
      priorityQueue.remove();
    }
  }

  return priorityQueue.items;
};

module.exports = { topKFrequent };
