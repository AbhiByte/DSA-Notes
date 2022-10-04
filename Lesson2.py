#Binary Search Trees, Traversals, and balancing
'''Goals of problem: Backend problem with 4 functions:
1. Insert profile info
2. Find profile info given username
3. Update profile info given username
4. List all the users sorted by username'''

#Create user class
from platform import node
from select import KQ_EV_SYSFLAGS


class User:
    #Constructor method
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    #Helper functions
    def __repr__(self) -> str:
        return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
    def __str__(self) -> str:
        return self.__repr__()   


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    
    def list_all(self):
        return self.users

abhinav = User('abhi', 'Abhinav R', 'abhi@example.com')
john = User('johnny', 'John Doe', 'John123@gmail.com')
don = User('don', 'Don Don', 'Don123@hotmail.com')

database = UserDatabase()
database.insert(abhinav)
database.insert(john)
database.insert(don)

print(database.find('abhi'))

'''1. O(n), 2. O(n), 3. O(n), 4. O(1)
Quite inefficient for large number of users''' 

'''^^^quite inefficient for large databases with linear time
Therefore we can use a BST organized lexographically'''

"1. Implementing a Binary Tree"
class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)















