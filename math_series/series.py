
def fibonacci(n):

    fibonacci_series = []
    first_number, second_number = 0 , 1

    fibonacci_series.append(first_number)
    fibonacci_series.append(second_number)

    while n > 1:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
        n-=1
        
    return fibonacci_series


print(fibonacci(5))

### ------------------ Second One ------------------ 

def lucas(n):
    lucas_numbers_list = []
    first_number, second_number = 2 , 1

    lucas_numbers_list.append(first_number)
    lucas_numbers_list.append(second_number)

    while n > 1:
        lucas_numbers_list.append(lucas_numbers_list[-1] + lucas_numbers_list[-2])
        n-=1
        
    return lucas_numbers_list

    
print(lucas(5))