# # #[1,0,2,4,0,5,7]
# # def asha(nums):
# #     for i in range (0,len(nums)):   #0-7 range
# #         if nums[i]==0:
# #             for x in range(i + 1, len(nums)):
# #                 if nums[x] == 0:
# #                     for y in range(i + 1, len(nums)):
# #                         if nums[y] == 7:
# #                             return True
# #     else:
# #         return False
# #
# #
# # a=asha([1,0,2,4,0,5,7])
# # print(a)
# #
# # #[1,0,2,4,0,5,7]
# # def asha(nums):
# #     for i in range (0,len(nums)):   #0-7 range
# #         if nums[i]==0:
# #             for i in range(i + 1, len(nums)):
# #                 if nums[i] == 0:
# #                     for x in range(i + 1, len(nums)):
# #                         if nums[i] == 0:
# #                             return True
# #     else:
# #         return False
#
# #69 start(stop= False)---stop at 6(stop=True)---start at 9(stop= False)
# def summer_69(arr):
#     stop=False
#     sum=0
#     for num in arr:
#         if num==6:
#             stop=True
#             print(sum)
#         elif num==9:
#             stop=False
#         elif stop is False:
#             sum=sum+ num
#     return sum
#
# z=summer_69([2,1,6,7,8,9,1])
# print(z)
#
# #number of upper case and lower case n
#
# def case(s):
#     lower=0
#     upper=0
#     for char in s:
#         if char.isupper():
#             upper=upper+1
#         elif char.islower():
#             lower=lower+1
#         else:
#             pass
#
#     return(lower,upper)
#
# z=case("AsHaH")
# print(z)
#
# # def case(s):
# #
# #     d={"lower": 0 ,"upper": 0}
# #
# #     for char in s:
# #         if char.isupper():
# #             d["upper"]+=1
# #         elif char.islower():
# #             d["lower"]+=1
# #         else:
# #             pass
# #
# #     return (upper,lower)
# #
# #
# # z=case([1,6,9,9,6,5,5,4])
# # print(z)
#
# def case(s):
#     #return set(s) either this or if statment
#     asha=[]
#     for number in s:
#         if number not in asha:
#             asha.append(number)
#     return asha
#
# z=case([1,6,9,9,6,5,5,4])
# print(z)
#
# # def mutilply(numbers):
# #     asha=1
# #     for num in numbers:
# #         asha=asha*num
# #     return asha
# #
# # z=mutilply([1,6,9,4])
# # print(z)
#
# def palindrome(s):
#     new=s.replace(" ","")
#     return new==new[::-1]
#
# z=palindrome("nurses run")
# print(z)
#
# import string
# def ispangram(new,alphabet=string.ascii_lowercase):
#     alphabet=set(alphabet)
#     new=new.replace(" ","")
#     new=new.lower()
#     new=set(new)
#     return new==alphabet
# z=ispangram("the Quick rown fox jumps over the lazy dog")
# print(z)


#local enclosing global and built in

#
# name="asha"   ### global
# def z():
#     name="rose" ###enclosing
#     def b():
#         name ="i am local" ###local
#         print("helloe "+name)
#     old = b()
#
#
# new=z()
# print(name)



import smtplib
import getpass
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("asha.colaco09@gmail.com","Franita@09")
server.sendmail("asha.colaco09@gmail.com","franita.colaco@yahoo.com","I love you")
server.quit()


