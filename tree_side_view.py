# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict() # depth -> node.val
        max_depth = -1

        stack = [(root, 0)]
        print("STACK = ", stack)
        while stack:
            node, depth = stack.pop()
            print("stack = ", node, depth)

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)
                print("max_depth = ", node, depth)
                # only insert into dict if depth is not already present.
                rightmost_value_at_depth.setdefault(depth, node.val)
                print("rightmost_value_at_depth = ", node, depth)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]