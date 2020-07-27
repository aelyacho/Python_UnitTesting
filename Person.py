class Person:
    def __init__(self, first_name, last_name, age, friends=None):
        if friends is None:
            friends = []
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__friends = friends

    def __repr__(self):
        return f'This is {self.first_name} {self.last_name}'

    def hello(self):
        print(f'Hello, my name is {self.first_name} {self.last_name}  and I\'m  {str(self.age)} years old')

    @property
    def friends(self):
        return self.__friends

    def add_friend(self, name):
        self.__friends.append(name)
        print(f'{name} added as friend!')

    def remove_friend(self, name):
        if name in self.__friends:
            self.__friends.remove(name)
            print(f'{name} removed as friend')
        else:
            print(f'{name} is not a friend')

    # p1 = Person("Be", "Code", 4, ["alex", "mike", "dave"])
    # p2 = Person('su', 'shi', 22)
