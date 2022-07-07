const { encode, decode } = require('../leetcode271');

test.each([
  { encodeInput: ['Hello', 'World'], encodeOutput: '5/Hello5/World' },
])('encode(); output()', ({ encodeInput, encodeOutput }) => {
  expect(encode(encodeInput)).toBe(encodeOutput);
  expect(decode(encodeOutput)).toEqual(encodeInput);
});
