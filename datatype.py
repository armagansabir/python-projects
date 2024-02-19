class User:
    totalbill=0
    def __init__(s,name,contact,email,password):
        s.name=name
        s.contact=contact
        s.email=email
        s.password=password

    def __str__(s):
        return s.name+"\t"+str(s.contact)+"\t"+s.email+"\t"+s.password

class Hotel:

    users=[]
    def register(s):
        print("Enter Name , Contact , Email , Password ")
        name=input("Enter Name : ")
        contact=input("Enter Contact : ")
        email=input("Enter Email : ")
        password=input("Enter Password : ")
        s.users.append(User(name,contact,email,password))

    def login(s):
        print("Enter Email & Password")
        email=input("Enter Email : ")
        password=input("Enter Password : ")
        for i in s.users:
            if email==i.email and password==i.password:
                return i

    def veg(s,u):
        print("+---------------------------------------+")
        print("|Sr No. |     Dish Name       | Price   |")
        print("+---------------------------------------+")
        print("|1      | Palak Paneer        |  250    |")
        print("+---------------------------------------+")
        print("|2      | Matar Paneer        |  150    |")
        print("+---------------------------------------+")
        print("|3      | Palak Tikka         |  200    |")
        print("+---------------------------------------+")
        print("|4      | Palak Masala        |  350    |")
        print("+---------------------------------------+")
        print("|5      | Paneer Masala       |  200    |")
        print("+---------------------------------------+")
        d=True
        pricelist=[250,150,200,200,350]
        veglist=["Palak Paneer","Matar Paneer","Palak Tikka","Paneer Masala","Palak Masala"]
        while(d):

            dname=input("Enter DishName : ")
            if dname.title() in veglist:
                qty=int(input("enter Quantity" ))
                u.totalbill=u.totalbill+(qty*pricelist[veglist.index(dname.title())])
                ys=input("Enter y For Order Another Dish\n    n for Main Menu" )
                if ys=="y":
                     s.veg(u)
                else:
                    s.menu(u)
                
                
                
            
    def nonveg(s,u):
        print("+---------------------------------------+")
        print("|Sr No. |     Dish Name       | Price   |")
        print("+---------------------------------------+")
        print("|1      | Palak Chikan        |  350    |")
        print("+---------------------------------------+")
        print("|2      | Matar Chikan        |  450    |")
        print("+---------------------------------------+")
        print("|3      | Chikan Tikka        |  250    |")
        print("+---------------------------------------+")
        print("|4      | Chikan Angara       |  350    |")
        print("+---------------------------------------+")
        print("|5      | Chikan MaraMari     |  200    |")
        print("+---------------------------------------+")

        d=True
        pricelist1=[250,150,200,200,350]
        nonveglist=["Palak Chikan","Matar Chikan","Chikan Tikka","Chikan Angara","Chikan MaraMari"]
        while(d):

            dname=input("Enter DishName")
            if dname.title() in nonveglist:
                qty=int(input("enter Quantity" ))
                u.totalbill=u.totalbill+(qty*pricelist1[nonveglist.index(dname.title())])
                ys=input("Enter y For Order Another Dish\n    n for Main Menu" )
                if ys=="y":
                     s.nonveg(u)
                else:
                    s.menu(u)
                


    
    def menu(s,u):
        print("------- Welcome To Armagan Hotel ------")
        c=True
        while(c):
            print("Enter 1 For Veg")
            print("      2 For Non-Veg")
            print("      3 For Bill")
            print("      4 For Exit")
            j=int(input("Enter Choice.."))
            if j==1:
                s.veg(u)
            elif j==2:
                s.nonveg(u)
            elif j==3:
                print("Your Name is : ",u.name,)
                print("Your Bill is : ",u.totalbill,)
            elif j==4:
                pass
            else:
                print("PLease Select Valid Choice...")
        
    def call(s):

        b=True
        while(b):
            print("Enter 1 For Register")
            print("      2 For Login")
            print("      3 For Exit")
            i=int(input("Enter Choice.."))
            if i==1:
                print("-----------------------------------------------------")
                s.register()
                print("-----------------------------------------------------")
            elif i==2:
                print("-----------------------------------------------------")
                u=s.login()
                if u is not None:
                    s.menu(u)
                else:
                    print("INvalid UserName , Password")
                print("-----------------------------------------------------")
            elif i==3:
                b=False
            else:
                print("-----------------------------------------------------")
                print("Please Select valid Choice.....")
                print("-----------------------------------------------------")



h=Hotel()
h.call()


