import sys

input = sys.stdin.readline

N = int(input())

tree = dict()

for _ in range(N):
    parent, leftChild, rightChild = map(str, input().split())
    tree[parent] = (leftChild, rightChild)


# 전위순회
def preOrder(root):
    if root != ".":
        print(root, end="")
        preOrder(tree[root][0])
        preOrder(tree[root][1])


# 중위순회
def inOrder(root):
    if root != ".":
        inOrder(tree[root][0])
        print(root, end="")
        inOrder(tree[root][1])


# 후위순회
def postOrder(root):
    if root != ".":
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end="")


preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
