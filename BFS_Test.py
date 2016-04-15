from BST import BinSearchTree

def main():
    bt = BinSearchTree()
    data_2 = [5, 4, 10, 3, 11, 12, 6, 7, 2, 1, 20, 8]
    data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    for val in data_2:
        bt.add_node(val)
    #print(bt.return_root())
    #bt.postorder_tree_walk(bt.root)
    #bt.tree_search(bt.root, 9)
    bt.print_tree()

if __name__ == '__main__':
    main()