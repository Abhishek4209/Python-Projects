import random
option=["Snake","Water","Gun"]
print(option)
print("  ⬇️      "," ⬇️    ","  ⬇️      ")
print("  -1      ","  0     ","   1      ")
name=input("Pls enter your name➡️   ")
def Chek(comp,user):
  # print("comp=",comp,"user=",user)
  if(comp==user):
    return 0
  elif(comp==-1 and user==0):
    return -1
  elif(comp==0 and user==1):
    return -1
  elif(comp==1 and user==-1):
    return -1
  else:
    return 1      
comp=random.randint(-1,1)
user=int(input("pls enter the option:  "))  
print("computer is select➡️  ",comp)
print(name,"is select➡️ ",user)
score=Chek(comp, user)
if(score==0):
  print("Game Draw")
elif(score==-1):
  print("You lose")
elif(score==1):
  print(name,"is win😊😊")