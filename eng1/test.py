# l = ["iio", "takamasa", "teacher"]
# for i, e in enumerate(l):
#     print(i, e)

# s = ["And", "Yodhwoe", "ANFOieoKHNfd"]
# a = [x.lower() for x in s]
# print(a)

# def func1():
#     print("aaa")

# def func2():
#     print("bbb")

# def func3():
#     print("ccc")

# s = ["func1()", "func2()", "func3()"]

# import random
# n = int(random.randint(0, len(s) - 1))


# eval(s[n])

DIALOG_1 = (
    "Hey",
    {
        ".*"        : "What are you doing now?",
    },
    {  
        ".*"      : "Don't you have to study?",
    },
    {
        ".*Yes.*"      : "huh? Why don't you study?",
        ".*No.*"      : "OK, but i think you waste time on using your phone.",
        ".*"      : "uh- huh, I see",
    },
    {
        ".*"      : "so, i want you to enjoy studing."
    },
    {   
        ".*"      : "and, if you have time to use your phone, come talk to me!",
    },
)

for i in range(len(DIALOG_1)):
    if isinstance(DIALOG_1[i], str):
        print(DIALOG_1[i])
        print(i)
    else:
        l= list(DIALOG_1[i].values())
        print(*l)