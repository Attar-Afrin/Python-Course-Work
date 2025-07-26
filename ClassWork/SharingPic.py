pics={
    1:'birthday.jpg',
    2:'childhood.png',
    3:'gradution.jpg',
    4:'beach.png',
    5:'family.jpg',
    6:'friends.png',
    7:'party.png',
    8:'sunset.jpg'
}
for i in pics:
    print(f"{i}. {pics[i]}")
selected_pics=set(map(int,input().split()))
for i in selected_pics:
    if 1<=i<=8:
        print(f"{pics[i]}")
    else:
        print("Unable to fetch photo for this id ",i)


'''
1. birthday.jpg
2. childhood.png
3. gradution.jpg
4. beach.png
5. family.jpg
6. friends.png
7. party.png
8. sunset.jpg
2 3 4 5 6 
childhood.png
gradution.jpg
beach.png
family.jpg
friends.png
'''