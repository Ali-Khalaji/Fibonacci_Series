""" This command calculates the Fibonacci series up to the desired number. """

def fibonacci_series():
    number = int(input('Enter the Number: '))
    a = 0
    b = 1
    while a < number:
        print(a)
        a, b= b, a+b

fibonacci_series() 


# Ali_Khalaji
