class ListNode:
    def __init__(self, val, next_node=None):
        self.val=val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        #dummy node for edge cases in case head is empty
        self.head = ListNode(2)
        self.tail = self.head #assume our list is never empty

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr = curr.next
        return -1 # index out of bounds


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            # if list was empty before inserting
            self.tail =new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        #we want to remove not at speciefic index
        i = 0
        curr = self.head
        while i < index and curr:
            #trying to move curr to node before target node
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next ==self.tail:
                self.tail = curr
            curr.next = curr.next.next
            #this is how we reomove ^
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
