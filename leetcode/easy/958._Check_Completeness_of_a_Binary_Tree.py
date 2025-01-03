# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Level order traversal:

This works but its memory inefficient.
'''
class LevelOrder:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        visited = []
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if len(visited) == depth:
                visited.append([])
            visited[depth].append(node)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        # check if all non-leaf nodes are full
        for depth, layer in enumerate(visited[:-1]):
            if len(layer) != 2**depth:
                return False

        for layer in visited:
            vals = [node.val for node in layer]
            print(vals)

        if len(visited) == 1:
            return True

        # check if all right-above-leaf nodes have left child
        should_be_empty = False
        for parent in visited[-2]:
            if not should_be_empty:
                if parent.right is not None:
                    # right filled before left, invalid!
                    if parent.left is None:
                        return False
                else:
                    should_be_empty = True
            else:
                if parent.right is not None or parent.left is not None:
                    return False

        return True

from collections import namedtuple

'''
Recursive approach where we spill out all the relations

The docstring would be self explainatory below
'''
class Recursive:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        FlatNode = namedtuple('FlatNode', ['depth'])
        UpDownNode = namedtuple('UpdownNode', ['deeper_depth'])
        '''
        Return the infomation about the the compleness of the subtree.
        '''
        def isCompleteTreeRec(root: TreeNode, depth: int) -> any:
            if root.left is None:
                # invalid complete tree
                if root.right is not None:
                    return None
                # trivial flat tree
                else:
                    return FlatNode(depth)

            next_depth = depth + 1
            match isCompleteTreeRec(root.left, next_depth):
                # Invalid tree
                case None:
                    return None
                # left tree is flat
                case FlatNode(left_depth):
                    if root.right is None:
                        if left_depth - depth > 1:
                            '''
                            This tree is invalid:
                                root
                              left
                            x    x
                            '''
                            return None
                        '''
                        This tree is valid:
                            root
                        left
                        '''
                        return UpDownNode(left_depth)

                    match isCompleteTreeRec(root.right, next_depth):
                        # right subtree is invalid
                        case None:
                            return None
                        case FlatNode(right_depth):
                            depth_diff = left_depth - right_depth
                            if depth_diff == 0:
                                '''
                                   root
                                left  right
                                x  x  x   x
                                '''
                                return FlatNode(right_depth)
                            elif depth_diff == 1:
                                '''
                                   root
                                left  right
                                x  x
                                '''
                                return UpDownNode(left_depth)
                            else:
                                '''
                                     root
                                  left  right
                                 x   x
                                x x x x

                                (or flipped)
                                '''
                                return None
                        case UpDownNode(right_depth):
                            if left_depth == right_depth:
                                '''
                                    root
                                left  right
                                x  x  x
                                '''
                                return UpDownNode(right_depth)
                            else:
                                '''
                                     root
                                  left  right
                                 x   x  x
                                x x x x
                                '''
                                return None
                case UpDownNode(left_depth):
                    if root.right is None:
                        '''
                            root
                        left
                        x
                        '''
                        return None
                    match isCompleteTreeRec(root.right, next_depth):
                        case None:
                            return None
                        case FlatNode(right_depth):
                            '''
                                root
                            left   right
                            x
                            '''
                            if left_depth == right_depth + 1:
                                return UpDownNode(left_depth)
                            '''
                                root
                            left   right
                            x      x   x
                            '''
                            return None
                        case UpDownNode(_):
                            '''
                                root
                            left   right
                            x     x
                            '''
                            return None

        return isCompleteTreeRec(root, 0) is not None

'''
BST:

This is basically a spin-off of the level-order traversal.
If we do a BST, whenever we start to see None, there should only be none.
'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        waiting_none = True

        queue = [root]
        while queue:
            current_node = queue.pop(0)

            if current_node is None:
                if waiting_none:
                    waiting_none = False
                elif waiting_none:
                    return False
            else:
                if not waiting_none:
                    return False

                queue.append(current_node.left)
                queue.append(current_node.right)
        return True
