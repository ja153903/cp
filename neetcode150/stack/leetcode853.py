from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.

        You are given two integer array position and speed, both of length n, where position[i] is the position of
        the ith car and speed[i] is the speed of the ith car (in miles per hour).

        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at
        the same speed. The faster car will slow down to match the slower car's speed.
        The distance between these two cars is ignored (i.e., they are assumed to have the same position).

        A car fleet is some non-empty set of cars driving at the same position and same speed.
        Note that a single car is also a car fleet.

        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

        Return the number of car fleets that will arrive at the destination.

        Solution:

        We should sort the elements by the position in reversed order.
        This is because we want to work from the car that will reach the target first.

        Let's model this as an equation of the line y = mx + b

        For every given pos and spd from the arrays, we know y, m, and b.
        Our job is to find unique values of x. Any value that doesn't have
        a unique value of x means that they will be in their own fleet
        otherwise we have to make sure that we keep track of the value.

        We then return the length of the stack since it should only contain
        unique values of x.

        :param target:
        :param position:
        :param speed:
        :return:
        """
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            # we're solving for x in y = mx + b where y ~ target, m ~ speed, b ~ pos
            # if the current x in the equation above is greater than the one on top of
            # the stack, then we can add it because there will be no collision happening
            dist = target - pos
            if not stack:
                stack.append(dist / spd)
            elif dist / spd > stack[-1]:
                stack.append(dist / spd)

        return len(stack)
