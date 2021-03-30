1.#from a string if first word is "a" print the word
st= "asha is my Aame"
for word in st.split():
     if word[0]=="a" or word[0]=="A":
          print(word)
     

2. #from list of number print even number
a=list(range(0,11,2))
print(a)

for number in range(0,11,2):
     print(number)


#3.
a=list(range(0,50))
for asha in a:
     if asha%3==0:
          print(asha)

for number in range(0,50):
     if number%3==0:
          print(number)

#4.
st= "asha is my Aamea"
for word in st.split():
     if len(word) %2==0:
          print(word)

#5
for num in range(0,101):
     if num%3==0 and num%5==0:
          print("Frizzbuss")
     elif num%3==0:
          print("nano")
     elif num%5==0:
          print("tato")
     else:
          print(num)

#6
st= "asha is my Aame"
for word in st.split():
     print(word[0])
     
          
     
     

         

