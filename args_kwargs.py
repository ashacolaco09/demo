#args usging funtion
#1.
def tuple(*args):
    print(args)
    return args[1]
    return sum(args)
z=tuple(1,2,3)
print(z)

#kwargs using function
#2.
def asha(**kwargs):
    print(kwargs)
    if "mango" in kwargs:
        print("the fruit i like is {}".format(kwargs["fruit"]))
    else:
        print("the fruit that is like is" + kwargs["vegi"])  # one way of printing
z=asha(fruit=" apple",vegi=" tomato")
print(z)

#mixture of both args and kwargs
#kwargs using function
#3.
def asha(*args,**kwargs):
    print(args)
    print(kwargs)
    print("the fruit i like is {}{}".format(args[2],kwargs["fruit"]))

z=asha(10,20,30,fruit=" apple",vegi=" tomato")
print(z)