data={
    'FaceWash':{'discount':20,'brands':['Himalaya','Clean&Clear','Plix','ChemistAtPlay','Ponds']}
}

data.keys()

product=input("Enter the Category")

if product in data:
    print(f'{data[product]["discount"]}% discount is goint on this brands:{data[product]["brands"]}')
else:
    print(f" Product is out of stock . please check with our product : {data}")         