def print_items(n):
    for i in range (n):
        print(i);

print_items(10);

#  O(n)


# drop constants

def print_items(n):
    for i in range (n):
        print(i);   

    for j in range (n):
        print(j);  

print_items(10);

