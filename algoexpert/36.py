class Node:
    def __init__(self, val: int, ancestor) -> None:
        self.ancestor = ancestor
        self.val = val    

root = Node(5)

# find the depths of both the nodes and go up the difference in depths for the lowest node and then keep on going up for both
