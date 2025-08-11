def fun(numbers):
    res=[]
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            res.append(numbers[i])
    return res
print(fun([1,2,3,4,6,8]))

def create_email(first,last,domain):
    update_str=print(f"{first}.{last}@{domain}.com")
    return update_str
print(create_email('afreen','attar','gmail'))