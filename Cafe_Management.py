menu={"Coffee":30,"Burger":60,"Pizza":110,"Pasta":35,"Tea":10}
menu_list=list(menu)
print("----------Menu----------")


for i in menu_list:
    print(f"{i}\t{menu[i]}")

order=input("Enter items you want to order :")

order=order.split(" ")

ans=input("Do you want to order anything else ?")

def place_order(order):
    total=0
    for i in order:
       total+=menu[i]
    return total

if ans.lower()=="yes":
    item=input("Enter the item you want to order : ")
    item=item.split(" ")
    order=order+item
   
    print("Your total bill is : " ,place_order(order))
else:
     print("Your total bill is : " ,place_order(order))




