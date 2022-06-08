const { PrioritizedItem, PriorityQueue } = require("../priorityQueue");

describe("PriorityQueue", () => {
  test("it should properly create priority queue", () => {
    const items = [
      new PrioritizedItem(1, 1),
      new PrioritizedItem(2, 2),
      new PrioritizedItem(3, 3),
      new PrioritizedItem(4, 4),
      new PrioritizedItem(5, 5),
    ];

    const priorityQueue = new PriorityQueue();
    for (const item of items) {
      priorityQueue.insert(item);
    }

    expect(priorityQueue.front).toBe(1);

    priorityQueue.remove();

    expect(priorityQueue.front).toBe(2);

    priorityQueue.remove();

    expect(priorityQueue.front).toBe(3);
  });
});
