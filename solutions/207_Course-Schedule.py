class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        indegree_map = {i : 0 for i in range(numCourses)}
        adjacency_list = defaultdict(list)

        for course, prereq in prerequisites:
            indegree_map[course] += 1
            adjacency_list[prereq].append(course)

        for node, degree in indegree_map.items():
            if degree == 0:
                q.append(node)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1

            for dependant in adjacency_list[node]:
                indegree_map[dependant] -= 1
                if indegree_map[dependant] == 0:
                    q.append(dependant)

        return count == numCourses


