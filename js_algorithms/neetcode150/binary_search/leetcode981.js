class _TMNode {
  constructor(value, timestamp) {
    /**
     * @type {string}
     */
    this.value = value;
    /**
     * @type {number}
     */
    this.timestamp = timestamp;
  }
}

class TimeMap {
  constructor() {
    /**
     * @type {Map<string, _TMNode[]>}
     * @private
     */
    this._map = new Map();
  }

  /**
   * @param {string} key
   * @param {string} value
   * @param {number} timestamp
   * @return {void}
   */
  set(key, value, timestamp) {
    const node = new _TMNode(value, timestamp);
    if (this._map.has(key)) {
      this._map.get(key).push(node);
    } else {
      this._map.set(key, [node]);
    }
  }

  /**
   * @param {string} key
   * @param {number} timestamp
   * @return {string}
   */
  get(key, timestamp) {
    if (!this._map.has(key)) {
      return '';
    }

    const nodes = this._map.get(key);

    let left = 0;
    let right = nodes.length - 1;
    let result = 0;

    while (left <= right) {
      const mid = left + Math.floor((right - left) / 2);
      if (nodes[mid].timestamp <= timestamp) {
        // consistently update the result pointer
        // this makes it more intuitive to follow
        result = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    if (nodes[result].timestamp <= timestamp) {
      return nodes[result].value;
    }

    return '';
  }
}

module.exports = TimeMap;
