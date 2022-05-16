from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        This problem is a classic application for Khan's algorithm

        There are a total of numCourses courses you have to take,
        labeled from 0 to numCourses - 1. You are given an array prerequisites
        where prerequisites[i] = [ai, bi]
        indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return true if you can finish all courses. Otherwise, return false.

        :param num_courses:
        :param prerequisites:
        :return:
        """
        queue = deque()
        graph = defaultdict(list)
        indegree = [0 for _ in range(num_courses)]

        for course, prerequisite in prerequisites:
            indegree[course] += 1
            graph[prerequisite].append(course)

        for i, num_prerequisites in enumerate(indegree):
            if num_prerequisites == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()

            # since the course we have here has no indegree
            # we should go through each course that needs to be taken
            # after this one and subtract their indegree
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return all([value == 0 for value in indegree])
