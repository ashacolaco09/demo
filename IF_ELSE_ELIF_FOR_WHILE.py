#if else statment
a="asha colaco"
if a=="asha colaco":
    print("true")
else:
    print("false")


#elif is used when more condition needs to be validated
a="asha colaco"
if a=="asha is colaco":
    print("true")
elif a=="royeston":
     print("proper")
elif  a=="asha y colaco":
     print("perfect")
else:
    print("false"),

# for loop 1
list_new=[1,2,3]
for new in list_new:
     print("new")

# for loop 2
list_new=[1,2,3,4,5,6,7,8,9,10]
for new in list_new:
     if new%2==0:
          print(new)
     else:
          print(f"odd number is :{new}")
     
#for loop 3
happy=[1,2,3,4,5,6,7,8,9,10]
for new in happy:
      print(new)

# for loop 4
list_sum=0
mylist=[1,2,3,4,5]
for num in mylist:
     list_sum=list_sum+num
     print(list_sum)
print(list_sum)
     
# for loop 5
word="hello wordl"
for asha in word:
     print("asha")  #this will print asha 11 times
     print(asha)    #this will print hello world

# tuple ans list packed together
new=[(1,2),(3,4),(5,6)]
for data in new:  # this will print in the packed format
     print(data)
for (a,b) in new:   #this will print in the unpacked format
    
    print(a)
    print(b)

#for loop in case of dic
a={"k1":1, "k2":2, "k3":3}
for new in a: # this will only print the key
    print (new)



a={"k1" : 1, "k2" : 2, "k3" : 3}
for value in a.values():
    print(value)
for key in a.keys():
    print(key)

a={"k1" : 1, "k2" : 2, "k3" : 3}
for item in a.items(): # this will only print both
    print(item)

#while loop
i = 1
while i < 6:
  print(f"the value is: {i}")
  i =i+ 1
    
          
          
    
          
          
