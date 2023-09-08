import heapq
import collections

def task_schedule(tasks, n):
     freqmap = {}
     for i in range(len(tasks)):
         freqmap[tasks[i]] = 1 + freqmap.get(tasks[i],0)

     maxHeap = [-c for c in freqmap.values()]
     heapq.heapify(maxHeap)

     time= 0
     q = collections.deque()

     while q or maxHeap:
         #nonlocal time
         time +=1
         if maxHeap:
             cnt = 1 + heapq.heappop(maxHeap)
             if cnt:
                 q.append([cnt, time +n])
         if q and q[0][1]==time:
             heapq.heappush(maxHeap,q.popleft()[0])

    return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    val = task_schedule(tasks, n)
    print(val)