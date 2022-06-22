function Node(val, next, random) {
  this.val = val;
  this.next = next;
  this.random = random;
}

/**
 * @param {Node} head
 * @return {Node}
 */
const copyRandomList = function (head) {
  const mp = new Map();
  mp.set(null, null);
  let curr = head;

  while (curr) {
    // keep track of node copies
    mp.set(curr, new Node(curr.val));
    curr = curr.next;
  }

  curr = head;

  while (curr) {
    const node = mp.get(curr);
    if (node) {
      node.next = mp.get(curr?.next);
      node.random = mp.get(curr?.random);
    }

    curr = curr.next;
  }

  return mp.get(head);
};

module.exports = { copyRandomList };
