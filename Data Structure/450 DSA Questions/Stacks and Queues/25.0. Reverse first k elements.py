# Input : Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#         k = 5
# Output : Q = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]

# Create an empty stack.
# One by one dequeue first K items from given queue and push the dequeued items to stack.
# Enqueue the contents of stack at the back of the queue
# Dequeue (size-k) elements from the front and enqueue them one by one to the same queue.


def reverseKelements(arr, k):
    stack = []
    for i in arr:
        a = arr.pop(0)
        stack.append(a)
    while stack:
        x = stack.pop()
        arr.append(x)
    for j in range(len(arr) - k):
        ele = arr.pop(0)
        arr.append(ele)
    return arr


k = int(input())
arr = [int(i) for i in input().strip().split()]
ans = reverseKelements(arr, k)
print(ans)
