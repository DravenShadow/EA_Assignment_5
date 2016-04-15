"""
            BST_Test.py                             Author: Rowland DePree


            Runs the BST program.
"""
from BST import BinSearchTree


def main():
    """
    Main method
    :return:
    """
    bt = BinSearchTree()
    data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    for val in data:
        bt.add_node(val)

    print(
        'Welcome to the BST Program!\nIt will now run through a pre set of operations for you using pre created data.')
    print('(Note: If you want to change any value in the program you will need to modify the test file)\n')
    print('Data: ', end='')
    print(data)
    print('\nBinary Tree by Level (Question 1): ')
    bt.print_tree()
    print('\nBinary tree pre-order (Question 2): ')
    bt.preorder_tree_walk(bt.root)
    print('\nBinary tree post-order (Question 2): ')
    bt.postorder_tree_walk(bt.root)
    print('\nBinary tree search looking for the value 9 (Question 3): ')
    bt.tree_search(bt.root, 9)


"""
    Runs the main method
"""
if __name__ == '__main__':
    main()
