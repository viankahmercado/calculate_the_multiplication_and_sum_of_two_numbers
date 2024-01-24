# Assignment 5 

# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


#function to calculate sum or product
def check_product_or_sum(first_number, second_number):
    product = first_number * second_number
#if-else statement for the condition
    if product <= 1000:
        return product
    else:
        return (first_number + second_number)

#assign variables for given 1 and given 2
first_given1 = 20
second_given1 = 30
first_given2 = 40
second_given2 = 30

#print the results