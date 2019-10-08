import sys
#sys.path.append('../queue_and_stack')
#from dll_queue import Queue
#from dll_stack import Stack
from typing import Callable, Any, List

class BinarySearchTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int) -> None:
        # Insert the given value into the tree
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            pass
        pass

    def contains(self, target: int) -> bool:
        # Return True if the tree contains the value
        # False if it does not
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
           
    def get_max(self) -> int:
        # Return the maximum value found in the tree
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb: Callable[[int], Any]):
        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    @property
    def in_order(self) -> List[int]:
        """    """
        flattened = list()
        if self.left:
            flattened.extend(self.left.in_order)

        flattened.append(self.value)

        if self.right:
            flattened.extend(self.right.in_order)

        return flattened

    @property
    def pre_order(self) -> List[int]:
        """  """
        flattened = list()
        flattened.append(self.value)

        if self.left:
            flattened.extend(self.left.pre_order)
        if self.right:
            flattened.extend(self.right.pre_order)

        return flattened

    @property
    def post_order(self) -> List[int]:
        """    """
        flattened = list()
        if self.left:
            flattened.extend(self.left.post_order)
        if self.right:
            flattened.extend(self.right.post_order)

        flattened.append(self.value)

        return flattened
    
if __name__=='__main__':
    bst = BinarySearchTree(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(6)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)

    print(bst.in_order)
    print(bst.pre_order)
    print(bst.post_order)

    """
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
    """
