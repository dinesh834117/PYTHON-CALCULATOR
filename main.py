print("         *****Welcome******\n")
print("         ****simple calculator*****\n")
def add(a,b,c):
  return a+b+c
def sub(a,b,c):
  return a-b-c
def mul(a,b,c):
  return a*b*c
def div(a,b,c):
  return a/b/c
print("what opertation u wantwd to select\n")
print("the operations are (+-*/)")
while True:
  n=input("enter the operation")
  n1=int(input("enter the first number"))
  n2=int(input("enter the second number"))
  n3=int(input("enter the third number"))
  if n=="+":
      print(n1,"+",n2,"+",n3,"=",add(n1,n2,n3))
  elif n=="-":
      print(n1,"-",n2,"-",n3,"=",sub(n1,n2,n3))
  elif n=="*":
      print(n1,"*",n2,"*",n3,"=",mul(n1,n2,n3))
  elif n=="/":
      print(n1,"/",n2,"/",n3,"=",div(n1,n2,n3))
  else:
        print("You typed an invalid number please check the number")
  restart = input("Do you want to restart? (Y/N): ")
  if restart.lower() != "y":
        break
print("THANK FOR USING")


