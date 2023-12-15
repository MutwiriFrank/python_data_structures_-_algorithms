# O(a+b)

def print_ites(a,b):
    for i in range (a):
        print(i);   

    for j in range (b):
        print(j);  

print_ites(2,10)


# O(a*b)
def print_items(a,b):
    for i in range (a):
        for j in range (b):
            print(i,j)


print_items(2,10)