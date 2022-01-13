class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        # we storing it as array but we visualize it as Binary Heap
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value

    # In insert operation,to maintain the heap order property,
    # we will have to Up Heapify or percolate up
    def insert(self, value, priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.percolateUp()

    # percolate up or upHeapify to maintain Heap order property
    # O(logN)
    def percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            # to get a parent of any child we can use this formula,
            parentIndex = (childIndex - 1) // 2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    # In remove operation,to maintain the heap order property,
    # we will have to downHeapify or percolate down
    def removeMin(self):
        lastIndex = len(self.pq) - 1
        lastIndexEle = self.pq[lastIndex]
        # replacing the top removed element with last element,
        self.pq[0] = lastIndexEle
        self.downheapify()

    def downheapify(self):
        parentIndex = 0
        while parentIndex < (len(self.pq) - 1):
            childIndex1 = parentIndex + 1
            childIndex2 = parentIndex + 2
            if self.pq[parentIndex].priority > (self.pq[childIndex2].priority or self.pq[childIndex1].priority):
                if self.pq[childIndex1].priority < self.pq[childIndex2].priority:
                    self.pq[childIndex2], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex2]
                    parentIndex = childIndex2

                else:
                    self.pq[childIndex1], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex1]
                    parentIndex = childIndex1
            else:
                break
