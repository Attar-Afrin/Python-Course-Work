# Sum Of The N Natural Numbers
def display(n):
    if n==0:
        return 0
    
    return n+display(n-1)
print(display(20))
