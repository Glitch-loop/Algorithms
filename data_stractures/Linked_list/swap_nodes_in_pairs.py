# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        head = self.traverse_list(head, True)
        #print("head: ", head)
        return head

    def traverse_list(self, current_node, swap):
        
        if current_node is None: 
            # It is the last node
            return current_node
        else:
            if current_node.next is None:
                return current_node

            next_node = current_node.next

            if (swap):
                # It is needed a swap
                current_node.next = next_node.next
                next_node.next = current_node

                # The next node becomes the new head
                current_node = next_node
            
            current_node.next = self.traverse_list(current_node.next, not(swap))

            return current_node
