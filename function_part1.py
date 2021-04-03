# #1. adding and subtract two number using function
def add(num1,num2):
    a=num1+num2
    b=num1-num2
    return a,b
z=add(10,20)
print(z)


#2. if 1st word and 2nd word letter are same print true else false
def myfn(text):
    word=text.split()
    a=word[0]
    b=word[1]
    return a[0]==b[0]
z=myfn("asha agnelo")
print(z)


# 3.#with paranthecis is left blank(default needs to be set)
def printing(asha="default"):
    print(f"hello {asha}")
z=printing()
print(z)

# #4. if number is divisible by 2 print true else print false
def even(num):
    for i in num:
        if i%2==0:
            print(True)
        else:
            print(False)
z=even([1,2,5,6])
print(z)

# #5 instead of printing return the true or false(if any of number in the list is even o/p will be true):
def dad(num):
     for i in num:
         if i % 2 == 0:
             return True
         else:
             pass
     return False
z=dad([1,2,9])
print(z)

#6. add all the even number in the place holder provided
def even(num):
    new=[]
    for i in num:
        if i % 2 == 0:
            c=new.append(i)
        else:
            pass
    return new
z=even([6,7,8])
print(z)

#7 suffle inside funtion
import random
def shuff(mynum):
    for i in mynum:
        random.shuffle(mynum)
        return mynum
z=shuff([6,7,8])
print(z)

