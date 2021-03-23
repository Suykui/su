import sys

class TreeNode(object):
    """bianry tree"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def form_before_build_tree(before,mid):
    if not before:
        return
    node = TreeNode(before[0])
    index = mid.index(before[0])
    node.left = form_before_build_tree(before[1:index+1],mid[:index])
    node.right = form_before_build_tree(before[index+1:],mid[index+1:])
    return node

def from_behind_build_tree(mid,behind):
    if not mid:
        return
    node = TreeNode(behind[-1])
    index = mid.index(behind[-1])
    node.left = from_behind_build_tree(mid[:index],behind[:index])
    node.right = from_behind_build_tree(mid[index+1:],behind[index:-1])
    return node

def print_tree(node):
    if node == None:
        return
    print_tree(node.left)
    print_tree(node.right)
    print(node.data)

def tree_to_before_str(node):
    tree_str = ''
    def tree_string(cur):
        nonlocal tree_str
        if cur == None:
            return
        tree_str += cur.data
        tree_string(cur.left)
        tree_string(cur.right)
    tree_string(node)
    return tree_str

def tree_to_behind_str(node):
    tree_str = ''
    def tree_string(cur):
        nonlocal tree_str
        if cur == None:
            return
        tree_string(cur.left)
        tree_string(cur.right)
        tree_str += cur.data
    tree_string(node)
    return tree_str

def bianry_tree(before=None, mid=None,behind=None):
    if not mid:
        print('Error Para')
        return False
    if before and mid:
        node = form_before_build_tree(before,mid)
        return tree_to_behind_str(node)
    if behind and mid:
        node = from_behind_build_tree(mid,behind)
        return tree_to_before_str(node)
    return False


def main():
    node = build_tree('abc','bac')
    print_tree(node)

if __name__ == '__main__':
    main()