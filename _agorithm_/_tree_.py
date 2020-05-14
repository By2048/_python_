class Node(object):
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value


class Tree(object):
    def __init__(self):
        self.root = Node()


def preoder(root):
    '''
    先序遍历，递归方式
    '''
    if not isinstance(root, Node):
        return None
    preorder_res = []
    if root:
        preorder_res.append(root.value)
        preorder_res += preoder(root.left)
        preorder_res += preoder(root.right)

    return preorder_res


def pre_order_not_recursion(root):
    '''
    先序遍历，非递归方式
    '''

    if not isinstance(root, Node):
        return None

    stack = [root]
    result = []
    while stack:
        node = stack.pop(-1)
        if node:
            result.append(node.value)
            stack.append(node.right)
            stack.append(node.left)
    return result


def middle_order(root):
    '''
    中序遍历，递归方式
    '''
    if not isinstance(root, Node):
        return None
    middle_res = []
    if root:
        middle_res += middle_order(root.left)
        middle_res.append(root.value)
        middle_res += middle_order(root.right)
    return middle_res


def middle_order_bot_recursion(root):
    '''
    中序遍历，非递归方式
    '''
    if not isinstance(root, Node):
        return None

    result = []
    stack = [root.right, root.value, root.left]
    while stack:
        temp = stack.pop(-1)
        if temp:
            if isinstance(temp, Node):
                stack.append(temp.right)
                stack.append(temp.value)
                stack.append(temp.left)
            else:
                result.append(temp)
    return result


def post_order(root):
    '''
    后序遍历，递归方式
    '''
    if not isinstance(root, Node):
        return None
    post_res = []
    if root:
        post_res += post_order(root.left)
        post_res += post_order(root.right)
        post_res.append(root.value)
    return post_res


def post_order_not_recursion(root):
    '''
    后序遍历，非递归方式
    '''
    if not isinstance(root, Node):
        return None

    stack = [root.value, root.right, root.left]
    result = []

    while stack:
        temp_node = stack.pop(-1)
        if temp_node:
            if isinstance(temp_node, Node):
                stack.append(temp_node.value)
                stack.append(temp_node.right)
                stack.append(temp_node.left)
            else:
                result.append(temp_node)

    return result


def layer_order(root):
    '''
    分层遍历，使用队列实现
    '''
    if not isinstance(root, Node):
        return None

    queue = [root.value, root.left, root.right]
    result = []
    while queue:
        temp = queue.pop(0)
        if temp:
            if isinstance(temp, Node):
                queue.append(temp.value)
                queue.append(temp.left)
                queue.append(temp.right)
            else:
                result.append(temp)

    return result


def node_count(root):
    '''
    计算二叉树结点个数，递归方式
    NodeCount(root) = NodeCount(root.left_child) + NodeCount(root.right_child)
    '''
    if root and not isinstance(root, Node):
        return None

    if root:
        return node_count(root.left) + node_count(root.right) + 1
    else:
        return 0


def node_count_not_recursion(root):
    '''
    计算二叉树结点个数，非递归方式
    借用分层遍历计算
    '''
    if root and not isinstance(root, Node):
        return None

    return len(layer_order(root))


def tree_deep(root):
    '''
    计算二叉树深度，递归方式
    tree_deep(root) = 1 + max(tree_deep(root.left_child), tree_deep(root.right_child))
    '''
    if root and not isinstance(root, Node):
        return None

    if root:
        return 1 + max(tree_deep(root.left), tree_deep(root.right))
    else:
        return 0


def tree_deep_not_recursion(root):
    '''
    计算二叉树深度，非递归方法
    同理参考分层遍历的思想
    '''
    if root and not isinstance(root, Node):
        return None
    result = 0
    queue = [(root, 1)]
    while queue:
        temp_node, temp_layer = queue.pop(0)
        if temp_node:
            queue.append((temp_node.left, temp_layer + 1))
            queue.append((temp_node.right, temp_layer + 1))
            result = temp_layer + 1

    return result - 1


def kth_node_count(root, k):
    '''
    计算二叉树第k层节点个数，递归方式
    kth_node_count(root, k) = kth_node_count(root.left_count, k-1) + kth_node_count(root.right_count, k-1)
    '''
    if root and not isinstance(root, Node):
        return None

    if not root or k <= 0:
        return 0
    if k == 1:
        return 1
    return kth_node_count(root.left, k - 1) + kth_node_count(root.right, k - 1)


def kth_node_count_not_recursion(root, k):
    '''
    计算二叉树第K层节点个数，非递归方式
    '''
    if root and not isinstance(root, Node):
        return None

    if not root or k <= 0:
        return 0

    if k == 1:
        return 1

    queue = [(root, 1)]
    result = 0
    while queue:
        temp_node, temp_layer = queue.pop(0)
        if temp_node:
            if temp_layer == k:
                result += 1
            elif temp_layer > k:
                return result
            else:
                queue.append((temp_node.left, temp_layer + 1))
                queue.append((temp_node.right, temp_layer + 1))
    return result


def leaf_count(root):
    '''
    计算二叉树叶子节点个数，递归方式
    关键点是叶子节点的判断标准，左右孩子皆为None
    '''
    if root and not isinstance(root, Node):
        return None

    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    return leaf_count(root.left) + leaf_count(root.right)


def is_same_tree(root1, root2):
    '''
    判断两个二叉树是不是相同，递归方式
    isSame(root1, root2) = (root1.value == root2.value)
                        and isSame(root1.left, root2.left)
                        and isSame(root1.right, root2.right)
    '''
    if not root1 and not root2:
        return True

    if root1 and root2:
        return (root1.value == root2.value) and \
               is_same_tree(root1.left, root2.left) and \
               is_same_tree(root1.right, root2.right)
    else:
        return False


def is_bst_tree(root):
    '''
    判断是否为二分查找树BST，递归方式
    二分查找树的定义搞清楚，二分查找树的中序遍历结果为递增序列
    '''
    if root and not isinstance(root, Node):
        return None

    def is_asc(order):
        for i in range(len(order) - 1):
            if order[i] > order[i + 1]:
                return False
        return True

    return is_asc(middle_order_bot_recursion(root))


def test():
    tree = Tree(0)

    n1 = Node(value=1)
    n2 = Node(value=2)
    n3 = Node(value=3)

    tree.root.left = n1
    tree.root.right = n2


if __name__ == "__main__":
    tree = Tree(1)
    tree1 = Tree(1)
    node6 = Node(None, None, 7)
    node5 = Node(None, None, 6)
    node4 = Node(None, None, 5)
    node3 = Node(None, None, 4)
    node2 = Node(node5, node6, 3)
    node1 = Node(node3, node4, 2)
    tree.root.left = node1
    tree.root.right = node2
    tree1.root.left = node2
    tree1.root.right = node2
    print(is_bst_tree(tree.root))
