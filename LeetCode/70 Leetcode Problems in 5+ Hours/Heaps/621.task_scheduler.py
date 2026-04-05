from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # We'll use a max heap solution to prioritize tasks that have higher count
        tasksCounted = Counter(tasks)
        # print(tasksCounted) # DEBUG
        tasksQueue = [tasksCounted[task] * -1 for task in tasksCounted]
        # print(tasksQueue) # DEBUG
        heapq.heapify(tasksQueue)

        coolDownQueue = deque()
        timer = 0

        while (coolDownQueue or tasksQueue):
            # print(tasksQueue, coolDownQueue) # DEBUG
            timer += 1
            
            if (tasksQueue):
                task = heapq.heappop(tasksQueue)
                task += 1
                if task < 0:
                    coolDownQueue.append((task, timer + n))
            
            if ((coolDownQueue) and (coolDownQueue[0][1] == timer)):
                heapq.heappush(tasksQueue, coolDownQueue.popleft()[0]) # FIFO for coolDownQueue

        return timer
