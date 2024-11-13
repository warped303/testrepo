def fibonnaci(x):
    if x == 0 or x == 1:
        return x
    else:
        n1 = 0
        n2 = 1
        for i in range(x):
            next = n1 + n2
            n1 = n2
            n2 = next
        return n1
        
print(str(fibonnaci(10)))
