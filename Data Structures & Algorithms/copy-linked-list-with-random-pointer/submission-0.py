"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp_map = {None: None} # Old node : New node

        curr = head
        while curr:
            tmp_node = Node(curr.val)
            tmp_map[curr] = tmp_node
            curr = curr.next
        
        curr = head
        while curr:
            tmp_node = tmp_map[curr]
            tmp_node.next = tmp_map[curr.next]
            tmp_node.random = tmp_map[curr.random]
            curr = curr.next
        return tmp_map[head]



        