class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def getDicimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num
    

if __name__ == "__main__":
    inp = [ListNode(1), ListNode(0), ListNode(1)]

    for i in range(len(inp) - 1):
        inp[i].next = inp[i + 1]
    s = Solution()

    print(s.getDicimalValue(inp[0]))