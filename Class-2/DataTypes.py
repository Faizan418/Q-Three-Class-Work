# Data Types in Python
# Data types yeh define karte hain ke variable ka type kya hai aur hum uske saath kya operations perform kar sakte hain.

# Python mein multiple data types hain, jin ko hum 6 main categories mein divide kar sakte hain:

# Numeric Types (Numbers)
# Boolean Type (True / False)
# Sequence Types (Strings, Lists, Tuples, Range)
# Set Types (Set, Frozenset)
# Mapping Type (Dictionary)
# Binary Types (Bytes, Bytearray, Memoryview)
# Agar kisi variable ka koi value nahi hai, toh uska type NoneType hota hai, jo None keyword se represent hota hai.

# 1. Numeric Types (Numbers)
# Python mein 3 tarah ke numbers hote hain:

# # Integer (int) → Pura number (without decimal)
# num_int = 42
# print(type(num_int))  # Output: <class 'int'>





# # Floating-Point (float) → Decimal wala number
# num_float = 3.14
# print(type(num_float))  # Output: <class 'float'>




# # Complex (complex) → Numbers jinmein real aur imaginary part hota hai
# num_complex = 2 + 3j
# print(type(num_complex))  # Output: <class 'complex'>


# 2. Boolean Type (True / False)
# Boolean sirf do values leta hai:

# True
# False





# # is_python_fun = True
# print(type(is_python_fun))  # type: ignore # Output: <class 'bool'>


# Agar koi condition satisfy hoti hai, toh True return hota hai, warna False.


# 3. Sequence Types (Strings, Lists, Tuples, Range)
# (a) String (str)

# # String characters ka sequence hota hai, jo quotes mein likha jata hai:
# text = "Hello, Python!"
# print(type(text))  # Output: <class 'str'>






# 3 tarah se likh sakte hain:

# Single Quotes: 'Hello'
# Double Quotes: "Hello"
# Triple Quotes: '''Hello''' (Multi-line Strings)
# (b) List (list)




# List ek ordered collection hoti hai jo mutable (changeable) hoti hai.

# my_list = [1, 2, 3, "Python", 3.14]
# print(type(my_list))  # Output: <class 'list'>




# List mein different types ke elements store kar sakte hain.
# Indexing zero-based hoti hai (i.e., pehla element 0 index par hota hai).
# (c) Tuple (tuple)
# Tuple bhi list jaisa hota hai, lekin immutable hota hai (iska data change nahi hota).

# my_tuple = (1, 2, 3, "AI", 2.71, False)
# print(type(my_tuple))  # Output: <class 'tuple'>






# (d) Range (range)
# Range ka use loop ke andar numbers generate karne ke liye hota hai.

# num_range = range(1, 10, 2)  # (start, stop, step)
# print(type(num_range))  # Output: <class 'range'>

# for i in range(1, 10, 2):
#     print(i)
# Output:

# 1  
# 3  
# 5  
# 7  
# 9  







# 4. Set Types (Set, Frozenset)
# (a) Set (set)
# Unordered collection hoti hai.
# Duplicate values allow nahi hoti.
# Mutable (changeable) hoti hai.

# my_set = {1, 2, 33, 4, 4, 5}
# print(type(my_set))  # Output: <class 'set'>
# Output:


# <class 'set'> my_set = {1, 2, 33, 4, 5}
# (Note: Duplicate 4 hat gaya hai)

# (b) Frozen Set (frozenset)
# Immutable set hota hai. Iska data change nahi ho sakta.

# frozen_set = frozenset([11, 2, 3, 4, 4, 5])
# print(type(frozen_set))  # Output: <class 'frozenset'>




# 5. Mapping Type (Dictionary)
# Dictionary key-value pairs store karti hai.

# my_dict = {"name": "Alice", "age": 25, "language": "Python"}
# print(type(my_dict))  # Output: <class 'dict'>





# 6. Binary Types (Bytes, Bytearray, Memoryview)
# (a) Bytes (bytes)
# Immutable binary data store karta hai.

# byte_data = b"Hello"
# print(type(byte_data))  # Output: <class 'bytes'>






# (b) Bytearray (bytearray)
# Mutable version of bytes.

# byte_array = bytearray([65, 66, 67, 69])  # ASCII values
# print(type(byte_array))  # Output: <class 'bytearray'>
# Output:

# <class 'bytearray'>  byte_array =  bytearray(b'ABCE')



# (c) Memoryview (memoryview)
# Binary data ko manipulate karne ke liye use hota hai.

# mem_view = memoryview(b"Operation Badar")
# print(type(mem_view))  # Output: <class 'memoryview'>





# None Data Type
# Agar kisi variable ko koi value assign na karein, toh wo None hota hai:

# x = None
# print(type(x))  # Output: <class 'NoneType'>
# None is False in Boolean Context:

# if None:
#     print("This will not run")
# else:
#     print("None is False in boolean context")
# Output:

# None is False in boolean context
# Memory Management in Python (id function)
# Python har variable ke liye unique ID (memory address) assign karta hai.

# python
# Copy
# Edit
# x = 1
# y = 1
# print(id(x), id(y))  # Dono same memory address show karenge


# Integer Interning in Python
# Python -5 se 256 tak ke integers ko same memory space mein store karta hai.

# python
# Copy
# Edit
# x = 1
# y = 1
# print(id(x) == id(y))  # Output: True
# Lekin agar number is range se bahar ho, toh naye objects create hote hain:

# x = -6
# y = -6
# print(id(x) == id(y))  # Output: False






# Summary
# Python mein multiple data types hote hain, jisme numbers, sequences, sets, dictionaries, aur binary types shamil hain.
# Lists mutable hoti hain, tuples immutable hoti hain.
# Sets duplicate values nahi rakhti.
# Dictionary key-value pairs store karti hai.
# NoneType ek special type hai jo 'no value' ko represent karta hai.