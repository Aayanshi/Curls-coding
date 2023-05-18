'''3. Write a Python program to check whether a given binary tree is a valid binary search tree (BST) or not'''
'''    if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        slow = head
        fast = head.next
        while (fast.next != None)and (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        root.left  =  self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root'''


