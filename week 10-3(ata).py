def range_sum_for(n):
    add=0
    for i in range(n):
        add = add+i
    
    print("total with for loop",add)


def range_sum_while(n):
    add=0
    x=0
    while x<n:
        add = add+x
        x+1
    
    print("Sum with while loop",add)


def bottom_check_sum(n):
    add=0
    t = 0
    while True:
        if t>n:
            break
        
        add=add+t   
        t+1

    print("this is the sum with the bottom check ",add)



num(6)
range_sum_for(num)
range_sum_while(num)
bottom_check_sum(num)
        



