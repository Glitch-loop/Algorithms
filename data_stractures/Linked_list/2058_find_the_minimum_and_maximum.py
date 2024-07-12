# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        arr_node = []
        node1 = head
        node2 = head.next
        index_node = 1
        critical_points_distance = [-1,-1]
        minDistance = sys.maxsize


        while node2.next != None:
            if (node1.val < node2.val and node2.next.val < node2.val # Local maxima
            or  node1.val > node2.val and node2.next.val > node2.val): # Local minima
                arr_node.append(index_node)
            
            node1 = node2
            node2 = node2.next
            index_node += 1

        len_arr_node = len(arr_node)


        
        if len_arr_node == 0 or len_arr_node == 1:
            return critical_points_distance
                
        first_item = arr_node[0]
        last_item = arr_node[len_arr_node - 1]
        
        

        maxDistance = abs(first_item - last_item) 

        for i in range(0, len_arr_node - 1):
            minDistance = min(minDistance, abs(arr_node[i] - arr_node[i + 1]))
            
        
        critical_points_distance[0] = minDistance
        critical_points_distance[1] = maxDistance

        return critical_points_distance
        