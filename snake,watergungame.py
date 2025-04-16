choice = input("Enter the choice either a snake,gun or water")
computer  = input("Enter the choice for computer")
dict1={"snake":1,"water":-1,"gun":0}
comp=dict1[computer]
cnum = dict1[choice]
if cnum==1 and comp==-1:
    print("you win!")
elif cnum==1 and comp ==0:
    print("you loose")
elif cnum==1 and comp ==1:
    print("draw")
elif cnum==0 and comp ==1:
    print("you win")
elif cnum==0 and comp ==-1:
    print("you loose")
elif cnum==0 and comp ==0:
    print("draw")
elif cnum==-1 and comp ==0:
    print("you win")
elif cnum==-1 and comp == 1:
    print("you loose")
elif cnum==-1 and comp ==-1:
    print("draw")
else:
    print("something is wrong")

