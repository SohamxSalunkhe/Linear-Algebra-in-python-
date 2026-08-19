def sum_list_elements(lst):
    result = 0
    count= 0

    for x in lst:
        result = result+x

        if x > 10 :
            count = count +1

    
    print("the sum is ",result)
    print("the count is",count)

    return result,count

r=[3,11,15,7,2,18]
sum_list_elements(r)
