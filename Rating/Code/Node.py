class Node:
    def __init__(self, data, checked=False, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        self.checked = checked

    def add_child(self, node):
        if self.left is None:
            self.left = node
            return True
        else:
            self.right = node
            return True

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def set_checked(self, flag):
        self.checked = flag

    def is_checked(self):
        return self.checked

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
