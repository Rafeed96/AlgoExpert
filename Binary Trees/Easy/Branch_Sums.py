# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    calculateBranchSums(root, 0, sums)
    
    return sums


def calculateBranchSums(node, currentSum, sums):
    newVal = currentSum + node.value

    if node.left == None and node.right == None:
        sums.append(newVal)
        return
    
    calculateBranchSums(node.left, newVal, sums)
    calculateBranchSums(node.right, newVal, sums)