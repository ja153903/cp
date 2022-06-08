class PrioritizedItem {
  /**
   *
   * @param {number} priority
   * @param {any} item
   */
  constructor(priority, item) {
    this.priority = priority;
    this.item = item;
  }
}

/**
 * By default, PriorityQueue is a min-heap.
 * Flipping the priority of the item with a negative sign is how
 * we'll achieve max-heap implementation.
 */
class PriorityQueue {
  constructor() {
    /**
     *
     * @type {PrioritizedItem[]}
     * @public
     */
    this.nodes = [];
  }

  /**
   *
   * @param {PrioritizedItem} prioritizedItem
   */
  insert(prioritizedItem) {
    this.nodes.push(prioritizedItem);
    this.moveUp();
  }

  /**
   *
   * @param {PrioritizedItem} prioritizedItem
   * @returns {PrioritizedItem | null}
   */
  remove() {
    if (!this.nodes.length) {
      return null;
    }

    // when we remove an item from the heap, we have to maintain
    const minPriorityItem = this.nodes[0];
    const end = this.nodes.pop();

    if (this.nodes.length > 0) {
      // Set the last item as the new head of the queue
      this.nodes[0] = end;

      let index = 0;
      let length = this.nodes.length;
      let node = this.nodes[index];

      while (true) {
        let leftChildIndex = this.getLeftChildIndex(index);
        let rightChildIndex = this.getRightChildIndex(index);
        let leftChild,
          rightChild,
          swap = null;

        if (leftChildIndex < length) {
          leftChild = this.nodes[leftChildIndex];
          if (leftChild.priority < node.priority) {
            swap = leftChildIndex;
          }
        }

        if (rightChildIndex < length) {
          rightChild = this.nodes[rightChildIndex];
          if (
            (swap === null && rightChild.priority < node.priority) ||
            (swap !== null && rightChild.priority < leftChild.priority)
          ) {
            swap = rightChildIndex;
          }
        }

        if (swap === null) {
          break;
        }

        this.nodes[index] = this.nodes[swap];
        this.nodes[swap] = node;
        index = swap;
      }
    }

    return minPriorityItem;
  }

  /**
   *
   * @returns {void}
   */
  moveUp() {
    let index = this.nodes.length - 1;
    const node = this.nodes[index];

    while (index > 0) {
      const parentIndex = this.getParentIndex(index);
      const parentNode = this.nodes[parentIndex];

      // if parent priority is greater than node priority,
      // then we swap
      if (parentNode.priority > node.priority) {
        this.nodes[parentIndex] = node;
        this.nodes[index] = parentNode;
        index = parentIndex;
      } else {
        break;
      }
    }
  }

  /**
   *
   * @param {number} index
   * @returns {number}
   */
  getLeftChildIndex(index) {
    return index * 2 + 1;
  }

  /**
   *
   * @param {number} index
   * @returns {number}
   */
  getRightChildIndex(index) {
    return index * 2 + 2;
  }

  /**
   *
   * @param {number} index
   * @returns {number}
   */
  getParentIndex(index) {
    return (index - 1) >> 1;
  }

  /**
   * @returns {any}
   */
  get front() {
    if (!this.nodes.length) {
      return null;
    }

    return this.nodes[0].item;
  }
}

module.exports = { PrioritizedItem, PriorityQueue };
