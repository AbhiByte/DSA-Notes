#Binary Search Trees, Traversals, and balancing
'''Goals of problem: Backend problem with 4 functions:
1. Insert profile info
2. Find profile info given username
3. Update profile info given username
4. List all the users sorted by username'''

#Create user class
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















