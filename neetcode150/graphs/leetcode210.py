from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
        you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return the ordering of courses you should take to finish all courses.
        If there are many valid answers, return any of them.
        If it is impossible to finish all courses, return an empty array.

        :param num_courses:
        :param prerequisites:
        :return:
        """
        result = []
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

            result.append(course)

            # since the course we have here has no indegree
            # we should go through each course that needs to be taken
            # after this one and subtract their indegree
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == num_courses else []
