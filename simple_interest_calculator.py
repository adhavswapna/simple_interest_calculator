P = "Principal Amount"
r = "Rate of interest"
t = "Time period"

P = float(input("What is the Principal Amount? "))
r = float(input("What is the rate of interest? "))
t = int(input("What is the Time Period? "))

si = P * r * t

print("Simple Interest = ",si)