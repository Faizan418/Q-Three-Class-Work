# # Correct indentation
# if True:
#     print("Hello, World!")
#     print("This is a block of code")

# Incorrect indentation
# if True:
# print("Hello, World!")
#   print("This is a block of code")




# # Incorrect indentation
# def greet(name: str):
# print("Hello, " + name + "!")


# # Correct indentation
# def greet2(name: str):
#     print("Hello, " + name + "!")








# age: int = input("Enter your age: ")
#    print(f"Your age is {age}")
#    print("type(age) = ", type(age))









# # Basic Syntax
# x: int = 5
# y: str = "hello"






# Function Type Hints
# You can also add type hints to function parameters and return types using the following syntax:

# def greet(name: str) -> str:
#     return "Hello, " + name + "!"
# print(greet("faizan"))





# my_list: list[int] = [1, 2, 3]
# my_dict: dict[str, int] = {"a": 1, "b": 2}
# my_tuple: tuple[str, int] = ("hello", 5)








# # Example of integers as objects
# x: int = 10
# print(x.bit_length())  # Method call on an integer object




# def greet(name) -> str:
#     return f"Hello, {name}!"

# def call_function(func, name) -> str:
#     return func(name)

# print(call_function(greet, "Alice"))  # Passing a function as an argument









# class Animal:
#     def speak(self) -> str:
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self) -> str:
#         return "Woof!"

# class Lion(Animal):
#     def speak(self) -> str:
#         return "Roar!"


# dog: Dog = Dog()
# print("Dog:  ", dog.speak())  # Output: Woof!

# lion: Lion = Lion()
# print("Lion: ", lion.speak())  # Output: Roar!







# class Human:
#     def speak(self):
#         print("Human: I'm good, thanks!")

# class Parrot:
#     def speak(self):
#         print("Parrot: Polly wants a cracker!")

# def have_conversation(person: Human):
#     print("\nhave_conversation: Hello, how are you? ", type(person))
#     person.speak()


# human = Human()
# parrot = Parrot()

# have_conversation(human)   # I'm good, thanks!
# have_conversation(parrot)  # Polly wants a cracker!






# class Robot:
#     def speak(self):
#         print("Robot: Beep boop, I am functioning within normal parameters!")

# robot = Robot()
# have_conversation(robot)  # type: ignore # Beep boop, I am functioning within normal parameters!