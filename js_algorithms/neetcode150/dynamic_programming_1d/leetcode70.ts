export function rec(n: number): number {
  if (n === 0 || n === 1) {
    return 1;
  }

  return rec(n - 1) + rec(n - 2);
}

function climbStairs(n: number): number {
  let a = 1;
  let b = 1;

  for (let i = 2; i <= n; i++) {
    [a, b] = [b, a + b];
  }

  return b;
}

export { climbStairs };
