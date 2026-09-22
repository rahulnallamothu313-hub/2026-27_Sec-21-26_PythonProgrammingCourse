#python program to calculate simple interest.
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest for annual (in %):"))
time=int(input("Enter the time duration (in years):"))
simpleinterest=(principal * rate * time) / 100
print("simpleinterest in Rs.",simpleinterest)