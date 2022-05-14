from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a characters array tasks, representing the tasks a CPU needs to do,
        where each letter represents a different task. Tasks could be done in any order.
        Each task is done in one unit of time. For each unit of time, the CPU could complete
        either one task or just be idle.

        However, there is a non-negative integer n that represents the cooldown period between
        two same tasks (the same letter in the array), that is that there must be at least n
        units of time between any two same tasks.

        Return the least number of units of times that the CPU will take to finish all the given tasks.

        Approach:

        * First count the number of occurrences of each element.
        * Let the max frequency seen be M for element E
        * We can schedule the first M-1 occurrences of E, each E will be followed by at least N CPU cycles
          in between successive schedules of E
        * Total CPU cycles after scheduling M-1 occurrences of E = (M-1) * (N + 1) // 1 comes for the CPU cycle for E itself
        * Now schedule the final round of tasks. We will need at least 1 CPU cycle of the last occurrence of E.
          If there are multiple tasks with frequency M, they will all need 1 more cycle.
        * Run through the frequency dictionary and for every element which has frequency == M, add 1 cycle to result.
        * If we have more number of tasks than the max slots we need as computed above we will return
          the length of the tasks array as we need at least those many CPU cycles.

        :param tasks:
        :param n:
        :return:
        """
        counter = Counter(tasks)
        _, max_freq = counter.most_common(1)[0]

        # initial M - 1 cycles. Fill in whatever necessary
        result = (max_freq - 1) * (n + 1)

        # We have to iterate over the end one more time
        # to account for the last cycle
        for key, val in counter.items():
            if val == max_freq:
                result += 1

        return max(result, len(tasks))
