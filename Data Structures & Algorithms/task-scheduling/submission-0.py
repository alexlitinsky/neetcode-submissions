class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        counts = Counter(tasks)
        maxH = [-cnt for cnt in counts.values()]
        heapq.heapify(maxH)
        cooldown = deque()

        while maxH or cooldown:
            time += 1
            if maxH:
                cnt = 1 + heapq.heappop(maxH)
                if cnt < 0:
                    cooldown.append((time + n, cnt))
            
            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(maxH, cnt)


        return time
        