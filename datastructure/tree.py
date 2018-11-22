class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left_child = left
        self.right_child = right
        
# create a tree        
n3 = TreeNode(3, None, None)
n2 = TreeNode(2, None, None)
n1 = TreeNode(1,n2, n3)

print(n1.data)
print(n1.left_child.data)
print(n1.right_child.data)
