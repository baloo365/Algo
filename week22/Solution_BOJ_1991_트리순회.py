N = int(input()) # 이진 트리의 노드 개수
nodes = [[] for _ in range(N)]
nodes = {}

for i in range(N):
    node, left, right = map(str, input().split())
    nodes[node] = [left, right]
# print(nodes)

stack = ['A']

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(nodes[root][0])  # left
        preorder(nodes[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(nodes[root][0])  # left
        print(root, end='')  # root
        inorder(nodes[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(nodes[root][0])  # left
        postorder(nodes[root][1])  # right
        print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')
