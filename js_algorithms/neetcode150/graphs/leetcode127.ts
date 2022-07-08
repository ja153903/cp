function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
  if (beginWord.length !== endWord.length) {
    return 0;
  }

  // we can do a BFS here to make sure that we get the shortest possible change
  const words: Set<string> = new Set(wordList);

  const queue: Array<{ word: string; count: number }> = [];
  queue.push({ word: beginWord, count: 1 });

  while (queue.length) {
    const front = queue.shift() ?? null;

    if (!front) {
      break;
    }

    const { word, count } = front;

    if (word === endWord) {
      return count;
    }

    for (let j = 0; j < word.length; j++) {
      for (let i = 97; i <= 122; i++) {
        const replacement = `${word.substring(0, j)}${String.fromCharCode(i)}${
          word.substring(j + 1)
        }`;
        if (words.has(replacement)) {
          words.delete(replacement);
          queue.push({ word: replacement, count: count + 1 });
        }
      }
    }
  }

  return 0;
}

let beginWord = 'hit';
let endWord = 'cog';
let wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog'];

console.log(ladderLength(
  beginWord,
  endWord,
  wordList,
));

// beginWord = 'hit';
// endWord = 'cog';
// wordList = ['hot', 'dot', 'dog', 'lot', 'log'];
//
// console.log(ladderLength(
//   beginWord,
//   endWord,
//   wordList,
// ));
