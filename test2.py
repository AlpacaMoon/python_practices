# class Fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("__iter__")
#         return self

#     def __next__(self):
#         print("__next__")				
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret


# for i in Fib(6):
#     print(i)



# def fun(n):
#     for i in range(n):
#         yield i
#         yield i

# for v in fun(5):
#     print(v)

# print([x for x in range(5)])




# def fun(x):
#     for i in range(x):
#         yield i * 3

# for k in fun(30):
#     print(k)

import random
for i in range(10):
    print(random.choice(['O', 'X']))