import collections

class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.locked = [None] * len(parent)
        self.child = {i:[] for i in range(len(parent))}

        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num, user):
        if self.locked[num]:
            return False
        self.locked[num]= user
        return True

    def unlock(self,num, user):
        if self.locked[num]!=user:
            return False
        self.locked[num]= None
        return True


    def upgrade(self,num, user):
        i = num
        while i!=-1:
            if self.locked[i]:
                return False
            i = self.parent[i]

        lockedCount, q = 0, collections.deque([num])

        while q:
            node = q.popleft()
            if self.locked[node]:
                self.locked[node] = None
                lockedCount +=1

            q.extend(self.child[node])

        if lockedCount >0:
            self.locked[num] = user

        return lockedCount>0

if __name__ == '__main__':
    obj = LockingTree(parent)
    param_1 = obj.lock(num,user)
    param_2 = obj.unlock(num,user)
    param_3 = obj.upgrade(num,user)

