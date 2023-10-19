class Node:
    def __init__(self, data, father=None, left=None, right=None, is_left=False):
        self.data = data
        self.father = father
        self.left = left
        self.right = right
        self.is_left = is_left

    def set_left(self, data):
        self.left = Node(data, father=self, is_left=True)

    def set_right(self, data):
        self.right = Node(data, father=self)


class BinaryTree:
    def __init__(self, data_root=None):
        if data_root:
            self.root = Node(data_root)
        else:
            self.root = None

    def pre_order(self, root):
        if root is None:
            return
        print(root.data, end=' -> ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=' -> ')
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=' -> ')

    def print(self, root, depth=0, is_left=None):
        if root is None:
            return None
        if depth == 0:
            print(f'{root.data}')
        else:
            if is_left:
                prefix = '└─L─'
            else:
                prefix = '└─R─'
            print('    ' * (depth - 1) + prefix + str(root.data))
        if root.left or root.right:
            self.print(root.left, depth + 1, is_left=True)
            self.print(root.right, depth + 1, is_left=False)