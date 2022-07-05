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

class AnotherLRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
    this.lru = new Set();
  }

  set(key, value) {
    if (this.cache.size === this.capacity && !this.cache.has(key)) {
      // evict LRU
      const lru = this.lru.values().next();
      this.cache.delete(lru.value);
      this.lru.delete(lru.value);
    }

    this.cache.set(key, value);
    this.lru.add(key);
  }

  get(key) {
    if (!this.cache.has(key)) {
      return -1;
    }

    const value = this.cache.get(key) ?? -1;

    this.updateLru(key);

    return value;
  }

  updateLru(key) {
    if (this.lru.has(key)) {
      this.lru.delete(key);
      this.lru.add(key);
    }
  }
}

const lru = new AnotherLRUCache(2);
lru.set(1, 1);
lru.set(2, 2);
console.log(lru.get(1));

lru.set(3, 3);
console.log(lru.get(2));

lru.set(4, 4);

console.log(lru.get(1));
