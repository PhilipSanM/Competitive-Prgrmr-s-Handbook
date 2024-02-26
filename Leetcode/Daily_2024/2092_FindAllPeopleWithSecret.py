# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=2092. Find All People With Secret -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: February - 25- 2024
# URL: https://leetcode.com/problems/find-all-people-with-secret/
# ====================================================================


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        # adjency of adjency list
        time_map = {}
        people_with_secret = set([0, firstPerson])

        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)

            time_map[time][src].append(dst)
            time_map[time][dst].append(src)


        def dfs(src, adjency, visited):
            if src in visited:
                return 

            visited.add(src)
            people_with_secret.add(src)

            for dst in adjency[src]:
                dfs(dst, adjency, visited)
        
        times = sorted(time_map.keys())
        for time in times:
            visited = set()

            for src in time_map[time]:
                if src in people_with_secret and src not in visited:
                    dfs(src, time_map[time], visited)



        return list(people_with_secret)
        