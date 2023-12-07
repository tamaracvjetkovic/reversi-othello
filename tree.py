from queue import Queue

class TreeNode():
    
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []
    
    def is_root(self):
        return (self.parent is None)
    
    def is_leaf(self):
        return (len(self.children) == 0)
    
    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return (self.parent)
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return (self.data)
       
    def append_child(self, child):
        self.children.append(child)
           
    def get_children(self):
        return (self.children)
    
    def num_children(self):
        return (len(self.get_children()))
    
    def __str__(self):
        return (str(self.data))
    
    
    
class Tree():
    def __init__(self, root: TreeNode):
        self.root = root
        self.len = 1
        
    def __len__(self):
        return (self.len)
    
    def is_empty(self):
        return (self.len == 1)
    
    def get_root(self):
        return (self.root)
    
    def is_root(self, node: TreeNode):
        return (node == self.root)
    
    def is_leaf(self, node: TreeNode):
        return (len(node.get_children()) == 0)
    
    
    def set_parent(self, node: TreeNode, parent):
        node.set_parent(parent)
        
    def get_parent(self, node: TreeNode):
        return (node.get_parent())
    
    def add_child(self, node: TreeNode, child: TreeNode):
        node.append_child(child)
        child.set_parent(node)
        self.len += 1
    
    def get_children(self, node: TreeNode):
        return (node.get_children())
    
    def num_children(self, node: TreeNode):
        return (node.get_children())
   

    def replace(self, oldNode: TreeNode, newNode: TreeNode):
        newNode.set_parent(oldNode.get_parent())
        newNode.set_data(oldNode.get_data())
        for child in oldNode.get_children():
            child.set_parent(newNode)
            newNode.append_child(child)
        oldNode.set_parent(None)
        oldNode.set_data(None)
        oldNode.set_children(None)
    
    
    def get_depth(self, node: TreeNode):
        if node.is_root():
            return 0
        else:
            return 1 + self.get_depth(node.get_parent())
    
    def get_height(self, node: TreeNode):
        if node.is_leaf():
            return 0
        else:
            return 1 + max(self.get_height(child) for child in node.get_children())
        
    def get_tree_height(self):
        return self.get_height(self.get_root())
   
        
    def dfs_preorder(self, node: TreeNode):
        #print(node)
        if (not self.is_empty()):
            print(node)
            for child in node.get_children():
                self.dfs_preorder(child)
        
    def dsf_postorder(self, node):
        if (not self.is_empty()):
            for child in node.get_children():
                self.dsf_postorder(child)
            print(node.data)
            
    def bfs(self, node: TreeNode):
        to_visit = Queue()
        to_visit.put(node)
        while not to_visit.empty():
            e = to_visit.get()
            print(e.data)
            for child in e.get_children():
                to_visit.put(child)
   
    
   
'''
    
if __name__ == '__main__':
       
    root = TreeNode(1)
    n1 = TreeNode(4)
    n2 = TreeNode(3)
    n3 = TreeNode(2)
    n4 = TreeNode(5)
    n5 = TreeNode(6)
    n6 = TreeNode(7)
    
    tree = Tree(root)
    tree.add_child(root, n1)
    tree.add_child(root, n2)
    tree.add_child(root, n3)
    tree.add_child(n1, n4)
    tree.add_child(n4, n5)
    tree.add_child(n2, n6)
    
    #tree.bfs(root)
    #print(tree.get_depth(n5))
    
    '''