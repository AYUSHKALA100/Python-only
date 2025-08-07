def main():
    Choice=input("WELCOME TO ZOMATO Your Food Buddy\nDO YOU HAVE AND ACCOUNT Y/N\n").strip().upper()
    if(Choice=="Y"):
     stored_username=input("Enter the Previous Username: \n")
     stored_password=input("Enter the Previous Password: \n")
     login(stored_username,stored_password)
    elif(Choice=="N"):
     Cac()


def Cac():
  Username=input("Create the Username: \n")
  Password=input("Create the Password: \n")
  print("Your account is created \n")
  login(Username,Password)

def Forgot(id,pas):  
  Cred=input("Enter one of the credential either Username or Password: \n")
   
  if(Cred==id or Cred==pas ):
    print("These are your Credentials: ", id, pas)
    return id,pas
  else:
        print("Credential not matched. Please try again.")
        return id, pas
  
def Menu():
   South_indian=["Dosa","Idli","Uttapam","Rasam"]
   Punjabi=["chole","Butter-chiken","chaanc"]
   North_indian=["Momo","Chomein","Chiken"]
   Garwali=["Bhatt","Rajma","faanu"]
   wholemenu=South_indian + Punjabi + North_indian + Garwali
   Option=int(input("Choose the Cusine Option from Menu below :\n1.South_indian\n2.Punjabi\n3.North_indian\n4.Garwali\n5.Whole menu \n"))  
   if(Option==1):
    print(",".join(South_indian))
   elif(Option==2):
     print(",".join(Punjabi))
   elif(Option==3):
     print(",".join(North_indian))
   elif(Option==4):
     print(",".join(Garwali))
   elif(Option==5):
     print("\n".join(wholemenu))
   else:
     print("Invalid Option/n Choose the Option Again")

   order(wholemenu)
   

def order(wholemenu):
    cart_items = []
    while True:
        choice = input("Enter your Dish choice (or type 'done' to finish): ").strip().lower()
        if choice == 'done':
            break
        elif choice in [item.lower() for item in wholemenu]:
            cart_items.append(choice)
            print(f"'{choice}' added to cart.")
        else:
            print("Item not found in menu. Try again.")
    
    if cart_items:
        price(cart_items)
    else:
        print("No items selected.")

def price(cart_items):
    food_prices = {
        "dosa": 50, "idli": 30, "uttapam": 60, "rasam": 40,
        "chole": 70, "butter-chiken": 150, "chaanc": 20,
        "momo": 60, "chomein": 80, "chiken": 120,
        "bhatt": 100, "rajma": 70, "faanu": 90
    }

    total = 0
    print("\nYour Bill:")
    for item in cart_items:
        item = item.lower()
        if item in food_prices:
            price = food_prices[item]
            total += price
            print(f"{item.capitalize()} - ₹{price}")
        else:
            print(f"{item.capitalize()} - Price not found")

    print(f"Total Bill: ₹{total}")
    print("Thank you for ordering with us!")

     
# def order(wholemenu,South_indian,Punjabi,North_indian,Garwali):
#     length=len(wholemenu)
#     choice=str(input("Enter your Dish choice Below: \n")).strip().lower()
#     for i in range(length):
#      if choice==wholemenu[i].lower():
#       opt=int(input("1.confirm your order And Pay \n 2. Add more items to the Cart"))
#       if(opt==1):
#        prc=price(wholemenu)
#       elif(opt==2):
#         prc=cart(wholemenu)
  
# def price(wholemenu):
    
     
# def cart():

def login(Username,Password):
  A=Username
  B=Password
  while True:
    id=input("Enter the Username \n")
    pas=input("Enter the Password \n")
    if(id==Username and pas==Password):
      print("You Logged In Successfully")
      Menu()
      break
    
    else:
     choice=int(input("You Have entered the wrong Credentials\n1.Have you Forgotten Either ID or PASS\n2.Create New Account\n"))
     
     if(choice==1):
      id,pas=Forgot(A,B)
      login(id,pas)
      break
     
     elif(choice==2):
       Cac()  

 


#runthecode
main()
  
