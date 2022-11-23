def calculation(a, b):
    add =a + b
    sub =a - b 
    return add, sub    
res = calculation(40, 10)
print(res)

def my_func(numbers):
    numbers.append(0)
    print(f"inside my_func: {numbers}")
    

#  create a function that takes at least two number unknown number of arguments and returns the sum
#  Solve this ex by passing positional arguments and by keyword argument
def print_sum(a, b, *args, **kwargs):
   my_sum = a + b
   my_sum += sum(args)
   # for arg in args:
   #  my_sum += arg
   # for num in kwargs.values():
   #  my_sum += num
   my_sum += sum(list(kwargs.values()))
   print(my_sum)
# print_sum(1, 2, 10)
print_sum(1, 2, num1=10, num2=13)

def check(a,b,c):
    print(a,b,c)
    
