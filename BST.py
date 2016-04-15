'''
Created on Mar 2, 2016

@author: nayeem
'''


class TreeNode:
    def __init__(self, key, left_child, right_child, parent):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent


class BinSearchTree:
    def __init__(self):
        self.root = None

    def return_root(self):
        return self.root.key

    def add_child(self, key, n):
        if key < n.key:
            if n.left_child is not None:
                self.add_child(key, n.left_child)
            else:
                n.left_child = TreeNode(key, None, None, n)
        else:
            if n.right_child is not None:
                self.add_child(key, n.right_child)
            else:
                n.right_child = TreeNode(key, None, None, n)

    def add_node(self, key):
        if self.root is None:
            self.root = TreeNode(key, None, None, None)
        else:
            self.add_child(key, self.root)

    def print_tree(self):
        tree = []
        if self.root is None:
            print(tree)
            exit()
        lvl_to_go = [self.root]
        while len(lvl_to_go) > 0:
            num_lvl = []
            next_lvl = []
            for element in lvl_to_go:
                if element is '#':
                    num_lvl.append(element)
                else:
                    num_lvl.append(element.key)
                if element is not '#':
                    if element.left_child is not None:
                        next_lvl.append(element.left_child)
                    else:
                        next_lvl.append('#')
                    if element.right_child is not None:
                        next_lvl.append(element.right_child)
                    else:
                        next_lvl.append('#')
            print(num_lvl)
            lvl_to_go = next_lvl


    def inorder_tree_walk(self, n):
        if n is not None:
            self.inorder_tree_walk(n.left_child)
            print(n.key)
            self.inorder_tree_walk(n.right_child)

    def preorder_tree_walk(self, n):
        if n is not None:
            print(n.key)
            self.preorder_tree_walk(n.left_child)
            self.preorder_tree_walk(n.right_child)

    def postorder_tree_walk(self, n):
        if n is not None:
            self.postorder_tree_walk(n.left_child)
            self.postorder_tree_walk(n.right_child)
            print(n.key)

    def tree_walk(self, n):
        if n is not None:
            print(n.key)
            self.tree_walk(n.left_child)
            self.tree_walk(n.right_child)

    def tree_search(self, n, key, node_path=[]):
        if n is None or key == n.key:
            node_path.append(n.key)
            print(node_path)
            return n
        if key < n.key:
            node_path.append(n.key)
            return self.tree_search(n.left_child, key, node_path)
        else:
            node_path.append(n.key)
            return self.tree_search(n.right_child, key, node_path)

    def tree_min(self, n):
        while n.left_child is not None:
            n = n.left_child
        return n

    def tree_max(self, n):
        while n.right_child is not None:
            n = n.right_child
        return n

    def tree_successor(self, n):
        if n.right_child is not None:
            return self.tree_min(n.right_child)
        p_node = n.parent
        while p_node is not None and n == p_node.right_child:
            n = p_node
            p_node = p_node.parent
        return p_node

    def tree_predeccessor(self, n):
        if n.left_child is not None:
            return self.tree_max(n.left_child)
        p_node = n.parent
        while p_node is not None and n == p_node.left_child:
            n = p_node
            p_node = p_node.parent
        return p_node

    def tree_insert(self, tree, n):
        p = n.parent
        x = tree.root
        while x is not None:
            p = x
            if n.key < x.key:
                x = x.left_child
            else:
                x = x.right_child
        n.parent = p
        if p is None:
            tree.root = n  # Tree was empty
        elif n.key < p.key:
            p.left_child = n
        else:
            p.right_child = n
