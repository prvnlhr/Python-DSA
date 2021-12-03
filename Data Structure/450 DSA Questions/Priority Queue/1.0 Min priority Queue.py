class priorityQueueNode:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class priorityQueue():

    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].val

    def percolateUp(self):
        childIndex = self.getSize() - 1
        parentIndex = childIndex - 1 // 2
        while childIndex > 0:
            if self.pq[parentIndex].priority > self.pq[childIndex]:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        pqNode = priorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.percolateUp()

    def percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2
        while leftChildIndex < self.getSize():

            minIndex = parentIndex
            # conditon 1
            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex
            # condition 2
            if rightChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightChildIndex].priority:
                minIndex = rightChildIndex
            # if condition 1 or condition 2 satisfies that means element still need to percolate down,
            # because we did got a minIndex from one of the above conditions.
            # But if heap order is satisfied and need to further percolate down, minIndex would have remain equal to parentIndex
            # in that case we need to break loop
            if minIndex == parentIndex:
                break

            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2

    def removeMin(self):
        ele = self.pq[0]
        lastIndex = self.getSize() - 1
        self.pq[0] = self.pq[lastIndex]
        self.pq.pop()
        self.percolateUp()
        return ele
