# Compound interest is the interest on savings calculated on both the initial principal and the accumulated interest from previous periods.

P = "Principal Amount"
i = "annual interest rate"
n ="number of compounding periods"

p = float(input("Enter the principal amount : "))

t = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

# compute compound interest
ci = p * (pow((1 + r / 100), t))

print("Compound interest" , ci)






