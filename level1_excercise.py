#1.siddharth.. even in upper case and odd in lower case
def asha(str):
    for i in range(0, len(str)):
        if i%2==0:
            a=str[i].upper()
            print(a)
        else:
            b=str[i].lower()
            print(b)
z=asha("siddharth")
print(z)

2.#macdnald(M and D capital)
def word(myword):
    a=myword[0:3]
    b=myword[3]
    c=myword[4:]
    return a.capitalize()+b.capitalize()+c
z=word("macdnald")
print(z)

3.#revrse the string and join it back(i love you)
def word(myword):
    fee=myword.split()
    a = fee[::-1]
    c="".join(a)
    return c
z=word("i love you nanu")
print(z)

4#(2,4)=== both even then print the lesser number if (5,2)==any one odd print max number
def num(a,b):
        if a%2==0 and b%2==0:
            return min(a,b)
        else:
            return max(a,b)

z=num(2,4)
print(z)

#5
def makes_twenty(n1,n2):
    return n1==20 or n2==20 or (n1+n2)==20
z=makes_twenty(10,40)
print(z)