import { assertEquals } from 'https://deno.land/std@0.147.0/testing/asserts.ts';

import { climbStairs } from './leetcode70.ts';

Deno.test('climbStairs', () => {
  assertEquals(climbStairs(2), 2);
});
