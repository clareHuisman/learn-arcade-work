class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        if self.weight < 10:
            print("Yip! says", self.name)
        else:
            print("Woof! says", self.name)


def main():
    my_dog = Dog()
    my_dog.name = "Spot"
    my_dog2 = Dog()
    my_dog2.name = "Rover"
    my_dog.bark()
    my_dog2.bark()


main()

