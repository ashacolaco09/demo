#1.[1,3,3]== true [1,3,4,3]=false
def asha(num):
    for i in range(0,len(num)-1):
        if num[i]==3  and num[i+1]==3:
            return True
        else:
            pass
    return False
z=asha([1,3,3,3])
print(z)

#2.HHHello... multiplying hello three times
def asha(str):
    a=str.split()
    result=a*3
    return result
z=asha("hello")
print(z)

#3.HHHello mutilplying H three times
def asha(str):
    a=str[0]
    b=str[1:]
    result=a*3
    return result+b
z=asha("Hello")
print(z)

#[9,9,9]= burst,[5,6,7]=18 [9,9,11]=19
def asha(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])>=21:
        return sum([a,b,c])-10
    else:
        return "bust"

z=asha(9,9,9)
print(z)


####### extra code from the starting wala concept
def asha(str):
    for i in str.split():
        if len(i)%2==0:
            print(i)
z=asha("my namee is ahsa")

def asha(str):
    result=[new for new in str if new%3==0]
    return result
z=asha([0,51])
print(z)








