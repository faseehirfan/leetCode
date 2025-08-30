class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        indegree_map = {i : 0 for i in range(numCourses)}
        adjacency_list = defaultdict(list)

        for course, prereq in prerequisites:
            indegree_map[course] += 1
            adjacency_list[prereq].append(course)

        for node, degree in indegree_map.items():
            if degree == 0:
                q.append(node)
        
        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for dependant in adjacency_list[node]:
                indegree_map[dependant] -= 1
                if indegree_map[dependant] == 0:
                    q.append(dependant)

        return result if len(result) == numCourses else []