data={
    'Apple':30,
    'Banana':10,
    'Orange':20,
    'Milk':50,
    'Bread':25,
    'Eggs':60,
    'Rice':40,
    'Tea':35,
    'Sugar':20,
    'Salt':15


}
AddToCart={}
while True:
    print("Available Products ".center(20,'='))
    for i,key in enumerate(data):
        print(f'{i+1} {key.ljust(10," ")}:{data[key]}')
    product=input("Enter the product name(Done-Exit): ").title()
    #Exit the bill generation logic
    if product=='Done':
        if AddToCart:
            totalbill=0
            for i in AddToCart:
                print(f'{i.ljust(10," ")}:{AddToCart[i]} *{data[i]}')
                totalbill=totalbill+AddToCart[i]*data[i]
                print(f'Total Bill :  {totalbill}')
        else:
            print("Thanks")
            break
    if product in data:
        qua=int(input("Enter the quantity of the product "))
        print(f'{product} is added to the cart')
        AddToCart[product]=qua
    else:
        print(f"{product} is not found")                
