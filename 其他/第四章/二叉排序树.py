class BTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BTree:
    def __init__(self, root):
        self.root = root;

    def insert(self, value):
        self.insertNode(value, self.root)

    def insertNode(self, data, btnode):
        if btnode == None:
            btnode = BTNode(data, None, None)
        elif data < btnode.data:
            if btnode.left == None:
                btnode.left = BTNode(data, None, None)
                return

            self.insertNode(data, btnode.left)
        elif data > btnode.data:
            if btnode.right == None:
                btnode.right = BTNode(data, None, None)
                return

            self.insertNode(data, btnode.right)

    def printBTreeImpl(self, btnode):
        if btnode == None:
            return

        self.printBTreeImpl(btnode.left)
        print(btnode.data,end= ' ')
        self.printBTreeImpl(btnode.right)

    def printBTree(self):
        self.printBTreeImpl(self.root)


if __name__ == '__main__':

    root = BTNode(2, None, None)
    btree = BTree(root)
    for i in [5,4,7,2,6,1,3 ]:# 5,4,7,2,6,1,3
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,4,7,2,6,3,1 ]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,4,7,6,2,1,3 ]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,4,7,6,2,3,1]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,7,4,2,6,1,3]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,7,4,2,6,3,1]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,7,4,6,2,1,3]:
        btree.insert(i)
    btree.printBTree()
    print("")
    for i in [5,7,4,6,2,3,1]:
        btree.insert(i)
    btree.printBTree()
    print("")

'''
5,4,7,2,6,1,3 
5,4,7,2,6,3,1
5,4,7,6,2,1,3 
5,4,7,6,2,3,1
5,7,4,2,6,1,3 
5,7,4,2,6,3,1
5,7,4,6,2,1,3 
5,7,4,6,2,3,1

'''