class _LRUCacheNode {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LRUCache {
  constructor(capacity) {
    /**
     * @type {number}
     */
    this.capacity = capacity;
    /**
     * @type {Map<number, _LRUCacheNode>}
     */
    this.cache = new Map();
    /**
     * @type {_LRUCacheNode}
     */
    this.head = new _LRUCacheNode(0, 0);
    /**
     * @type {_LRUCacheNode}
     */
    this.tail = new _LRUCacheNode(0, 0);

    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  /**
   * @param {number} key
   * @returns {number}
   */
  get(key) {
    const node = this.cache.get(key) ?? null;
    if (!node) {
      return -1;
    }
    this.updateLru(node);
    return node.value;
  }

  /**
   * @param {string} key
   * @param {string} value
   */
  put(key, value) {
    const node = this.cache.get(key) ?? null;

    if (!node) {
      const newNode = new _LRUCacheNode(key, value);
      const atCapacity = this.capacity === this.cache.size;

      if (atCapacity) {
        this.evictLru();
      }

      this.cache.set(key, newNode);
      this.updateLru(newNode);
    } else {
      node.value = value;
      this.updateLru(node);
    }
  }

  /**
   * @param {_LRUCacheNode} node
   */
  updateLru(node) {
    this.removeNode(node);
    this.addToHead(node);
  }

  /**
   * @param {_LRUCacheNode} node
   */
  removeNode(node) {
    const next = node.next;
    const prev = node.prev;

    if (prev) {
      prev.next = next;
    }

    if (next) {
      next.prev = prev;
    }
  }

  /**
   * @param {_LRUCacheNode} node
   */
  addToHead(node) {
    node.prev = this.head;
    node.next = this.head.next;

    this.head.next.prev = node;
    this.head.next = node;
  }

  /**
   * @returns {_LRUCacheNode}
   */
  evictLru() {
    const lru = this.tail.prev;

    if (lru) {
      this.removeNode(lru);
      this.cache.delete(lru.key);
    }

    return lru;
  }
}

module.exports = { LRUCache };
