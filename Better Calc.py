a = str(input("Enter x For Multiplication And + For Addition, - For Subtraction And / For Division:"))
if(a == "x"):
    b = int(input("So, As For Multiplication Enter The First Number To Multiply: "))
    c = int(input("So, As For Multiplication Enter The Second Number To Multiply: "))
    d = b * c
    print(d)
if(a == "+"):
    e = int(input("So, As For Addition Enter The First Number To Add: "))
    f = int(input("So, As For Addition Enter The Second Number To Add: "))
    g = e + f
    print(g)
if(a == "-"):
    h = int(input("So, As For Subtraction Enter The First Number To Subtract: "))
    i = int(input("So, As For Subtraction Enter The Second Number To Subtract: "))
    j = h - i
    print(j)
if(a == "/"):
    k = int(input("So, As For Division Enter The First Number To Divide: "))
    l = int(input("So, As For Division Enter The Second Number To Divide: "))
    m = k / l
    print(m)