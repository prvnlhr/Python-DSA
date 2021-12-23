class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def findNext(temp, mapp):
    while temp:
        ele = temp.val
        if mapp[ele] == 1:
            # print('temp', temp.val)
            return temp
        temp = temp.next


# Self Solved 100% , Time complexity O(N) and Space complexity O(N)
def deleteDuplicates(head):
    ptr = head
    prev = head
    mapp = {}
    while ptr is not None:
        if ptr.val in mapp:
            ele = ptr.val
            mapp[ele] = mapp[ele] + 1
        else:
            ele = ptr.val
            mapp[ele] = 1
        ptr = ptr.next

    curr = head
    first = curr.val
    # Edge case if first node is duplicate
    if mapp[first] > 1:
        ans = findNext(curr.next, mapp)
        curr = ans
        head = curr

    while curr and curr.next:
        currnext = curr.next
        ele = currnext.val
        # print(ele)
        if mapp[ele] > 1:
            ans = findNext(curr.next, mapp)
            # print('ans', ans.val)
            curr.next = ans
        curr = curr.next

    # print(mapp)
    return head


# efficient O(N)
def deleteDuplicate(head):
    if head is None:
        return

    curr = head
    while curr:

        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head


# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for val in arr[1:]:
        last.next = ListNode(val)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
newll = deleteDuplicate(l)
# solve(l, n)
printll(newll)
