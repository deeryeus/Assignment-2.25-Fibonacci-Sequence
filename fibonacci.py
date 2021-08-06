# returns the first number of the Fibonacci sequence that has n digits

# function that returns # of digits in a #; used in fibonacci function
def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

def big_fibonacci(n):   
    firstnum = 1
    secondnum = 1
    result = 1
    while n > count_digits(result):
        result = firstnum + secondnum
        # add the result to the smaller of the two #'s to keep track of the last two #'s used
        if firstnum > secondnum:
            secondnum = result
        elif secondnum >= firstnum:
            firstnum = result 
    print(result)

big_fibonacci(30)
