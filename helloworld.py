#creat account function
def CAC():
    username = str(input("Enter the username"))
    password = str(input("Enter the pasword"))
    print("Your account created suucessfully")
    Al(username,password)
# Account login function
def Al(username,password):
    id =  str(input("Enter the username"))
    pas = str(input("Enter the pasword"))
    if(id==username and pas==password):
      print("you logged in successfully")
    elif():
      print("Wrong id pass","\n Enter the details again")
      Al(username,password)
    else:
      CAC()
#Price function
def price(show,seat):
   if(show==1):
    prc=200*seat 
    print("The total Price of the ticket is", prc)    

   elif(show==2):
    prc=500*seat
    print("The total Price of the ticket is", prc) 

   elif(show==3):
    prc=100*seat
    print("The total Price of the ticket is", prc)  

# def bill():
         

#Booking function
def Bookshow():
    show = int(input("Choose the show Below \n1. Saiyara \n2. Narshima \n3. Dilbar\n"))
    seat = int(input("How many seats do you want to Book:\n"))
    price(show,seat)

#RUN THE CODE
username =None
password =None
print("HELLO WELCOME THE BOOKmySHOW","\n Do You Have an Account")
print("Enter the choice Below:","\n Y/N")
choice = str(input())
if(choice=="Y"):
   Al(username,password)
elif(choice=="N"):
   CAC()
   
Bookshow()