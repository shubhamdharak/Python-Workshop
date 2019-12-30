# Menu driven program for Fruit management
d = dict()
class fruit:
    
    def __init__(self,name):
        self.name = name

    def addFruit(self,name,quantity):
        # self.name = name
        # self.quantity = quantity
        if name in d.keys():
            print("Already Exist ..")
        
        else:
            d[name] = quantity
            
            
    
    def displayFruit(self):
        for item,value in d.items():
            print(item,": ",value,"KG")

    def sellFruit(self,name ,quantity):
        if name in d.keys():
            if quantity <= d[name]:
                print(f"{name} of {quantity}KG has selled ..")
                d[name] = d[name] - quantity
                
            else:
                print("Not Available")
        else:
            print("Fruit Not Found")

    def notification(self):
        for item,value in d.items():
            if d[name] < 5:
                print(item," : ",value,"KG")
                break
        else:
            print("No item ..")

    def updateQuantity(self,name, quantity):
        if name in d.keys():
            d[name] = quantity
            print("Updated")
        else:
            print("Not Updated")

    def deleteFruit(self,name):
        if name in d.keys():
            d.pop(name)
            print("Deleted")
        else:
            print("Not deleted")
    
while True:
    f = fruit("Fruiterra's Shop")
    print("#########################")
    print("   ",f.name)
    print("#########################")
    print("\n1.Add new Fruit")
    print("2.View All Fruit")
    print("3.Sell a Fruit")
    print("4.Notification")
    print("5.Update Quantity")
    print("6.Delete a Fruit")
    print("7.Exit")
    print("\n#########################")

    ch = int(input("Enter UR Choice : "))  

    if ch == 1:
        name = input("Enter Name of Fruit : ")
        quantity = int(input("Enter quantity of Fruit : "))
        f.addFruit(name,quantity)

    if ch ==2:
        f.displayFruit()

    if ch ==3:
        name = input("Enter Name of Fruit : ")
        quantity = int(input("Enter quantity of Fruit : "))
        f.sellFruit(name,quantity)
        
    if ch == 4:
        f.notification()
    
    if ch == 5:
        name = input("Enter Name of Fruit : ")
        quantity = int(input("Enter quantity of Fruit : "))
        f.updateQuantity(name,quantity)

    if ch == 6:
        name = input("Enter Name of Fruit : ")
        f.deleteFruit(name)
    if ch == 7:
        print("Bye .....!")
        break