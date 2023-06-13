# set menu value
import msvcrt



menu=[{"index":1,"name":"chicken nuggets", "price":8.5},
{"index":2,"name":"chicken strips", "price":9.5},
{"index":3,"name":"beef burgers", "price":12},
{"index":4,"name":"noodles", "price":8}]
#print table title
print("Menu Today:")
for i in range(30):
    print("=",end="")
print()
print("{:<4}{:<20}{:>6}".format("ID","Food Name","Price"))
for i in range(30):
    print("=",end="")
print()
#print menu
for x in menu:
    print("{:<4}{:<20}{:>6}".format(x["index"],x["name"],format(x["price"],'.2f')))

#print line to split title
for i in range(30):
    print("=",end="")
print()
#start to order
print("Please input your food name to order:")
for i in range(30):
    print("=",end="")
print()
amount=0
order=[]
order1={}
orderIndex=0
while True:
    orderIndex+=1
    order1["index"]=orderIndex
    print("{:<4}".format(order1["index"]),end="")
    order1["price"]=0
    order1["name"]=input()
    for x in menu:
        if order1["name"] == x["name"]:
            order1["price"]=x["price"]
    if order1["price"]==0:
        orderIndex-=1
        print("Sorry, we don't serv this food.")
        continue
    print(format(order1["price"],'.2f').rjust(30))
    order.append(order1)
    amount+=float(order1["price"] )
    if order1["name"]=="noodles":
        break
for i in range(30):
    print("=",end="")
print()
print("{:>20}{:>10}".format("Totle:",format(amount,'.2f')))
for i in range(30):
    print("=",end="")
print()
    

