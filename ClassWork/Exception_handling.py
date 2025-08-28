try:
    a=12/0
    print(a)
    b=int(input("Enter Number"))
    c=a+'de'
    d={1:2,2:3}
    i=d[5]
    l=[1,2,3,4]
    j=l[10]
    c=a+k

except ZeroDivisionError:
    print("cant divide with zero")
except ValueError:
    print("Enter the proper data type")
except TypeError:
    print("Different datatypes cant be add")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index out of range")
except NameError:
    print("undefined variable")

try:
    a=12/6
    print(a)
    b=int(input("Enter Number"))
    c=a+'de'
    d={1:2,2:3}
    i=d[5]
    l=[1,2,3,4]
    j=l[10]
    c=a+k
except (ValueError,ZeroDivisionError,TypeError,KeyError,IndexError,NameError) as e:
    print(f"Error Occured {e}")
#Note-->alias name shows the description of the error it dispalys in output without throwing the error

try:
    a=12/6
    print(a)
    b=int(input("Enter Number"))
    c=a+'de'
    d={1:2,2:3}
    i=d[5]
    l=[1,2,3,4]
    j=l[10]
    c=a+k
except Exception as e:
    print(f"Error Occured {e}")



#Try with else and finally keyword
try:
    a=12/6
    print(a)
    b=int(input("Enter Number"))
    c='rc'+'de'
    d={1:2,2:3}
    i=d[5]
    l=[1,2,3,4]
    j=l[10]
    c=a+k
except Exception as e:
    print(f"Error Occured {e}")
else:
    print("Code is free of exceptions")
finally:
    print("End of the program")

#Raise error explicitely
try:
    lst=['pfs_1','pfs_2','pfs_3']
    new='jfs_1'
    if not new.startswith("pfs"):
        raise Exception("New Member is not pfs batch")
    else:
        lst.append(new)

except Exception:
    print("Exception is Raised")
