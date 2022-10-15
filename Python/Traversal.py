class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

def levelWise(root): # time: O(n) spce: O(n)
    traversals=[]
    que=[root]

    # O(x)== where x = nodes in each level so max could be T+1 where T is number of internal nodes i.e nodes which have max 2 childs.
    while len(que)>0:
        temp=que.copy()
        que=[]
        nodeList=[]
        for node in temp: # O(x)
            nodeList.append(node.data)
            if node.left!=None:
                que.append(node.left)
            if node.right!=None:
                que.append(node.right)
        traversals.append(nodeList)
    return traversals
def LeftView(root): # same as of levelWise traversal just took first element of each level traversal.
                    # similary for right View as well
    traversals=[]
    que=[root]
    while len(que)>0:
        temp=que.copy()
        que=[]
        nodeList=[]
        for node in temp:
            if node:
                nodeList.append(node.data)
                if node.left!=None:
                    que.append(node.left)
                if node.right!=None:
                    que.append(node.right)
        if len(nodeList)>0:
            traversals.append(nodeList[0])
    return traversals

def leftViewUtil(root): #recursive: TIME:O(N) Space: O(h) h=height which in worst case would be N
    que=[]
    def leftView(root,level): # pre order(root,left,right)
        if root==None:
            return
        if level==len(que):
            que.append(root.data)
        leftView(root.left,level+1)
        leftView(root.right,level+1)
    leftView(root,0)
    print(que)
leftViewUtil(root)

def rightViewUtil(root): #recursive: TIME:O(N) Space: O(h) h=height which in worst case would be N
    que=[]
    def rightView(root,level): # reverse of post order(left,right,root) => root,right,left
        if root==None:
            return
        if level==len(que):
            que.append(root.data)
        rightView(root.right,level+1)
        rightView(root.left,level+1)
    rightView(root,0)
    print(que)
rightViewUtil(root)

def ZigZag(root): # time: O(n) spce: O(n)  #same as of level wise
    traversals=[]
    que=[root]
    flag=True
    while len(que)>0:
        temp=que.copy()
        que=[]
        nodeList=[]
        for node in temp: # O(x)
            nodeList.append(node.data)
            if node.left!=None:
                que.append(node.left)
            if node.right!=None:
                que.append(node.right)
        if flag:
            traversals.append(nodeList)
            flag=False
        else:
            traversals.append(nodeList[::-1])
            flag=True
    return traversals

#similar below could be done iteratively using level order traversal
def height(root): #time O(logn)  but for worst O(n),space=recursion auxilary space of O(h)=log(n) and in worst: O(n)
    if root==None:
        return 0
    leftHeight=height(root.left)
    rightHeight=height(root.right)
    return max(leftHeight,rightHeight)+1

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # time:O(logn) for worst O(n) and space:auxilary O(n)
    dia=0
    def height(root):
        nonlocal dia
        if root==None:
            return 0
        leftHeight=height(root.left)
        rightHeight=height(root.right)
        dia=max(dia,leftHeight+rightHeight)
        return max(leftHeight,rightHeight)+1
    height(root)
    return dia

# balanced Tree is a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    flag=True
    def height(root):
        nonlocal flag
        if root==None:
            return 0
        leftHeight=height(root.left)
        rightHeight=height(root.right)
        if abs(leftHeight-rightHeight)>1:
            flag=False
        return max(leftHeight,rightHeight)+1
    height(root)
    return flag



