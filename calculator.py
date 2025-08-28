#Hello everyone Today we are see about simple calculator program that takes by the arthmetic operation like +,-,*,/
#Lets start a Program

#To take the two input from the user like num1,num2
num1=int(input("Enter the 1st Integer:"))
num2=int(input("Enter the 2nd Integer:"))

#Then Print What are the operator are used in the calculator

print("+,-,*,/")


#Similarly to do like the which operator can be perform Its is done by the user decision so we get the User Input
user=input()
  #If the user give + means add to num like that if the user give - means subract to num, similarly user give * means to perform multiply operation like that divition

if user == "+":
     ans=num1+num2
     print(ans)
elif user == "-":
    ans=num1-num2
    print(ans)
elif user == "*":
    ans=num1*num2
    print(ans)
elif user == "/":
    ans=num1/num2
    print(ans)
else:
    print("The User cannot be mention other operation")


    
Thank you
