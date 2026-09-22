#python program to calculate simple compound interest.
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest for annual (in %):"))
time=int(input("Enter the time duration (in years):"))
compoundinterest=principal*(1+(rate/100))**time-principal
print("compound interest in Rs:",compoundinterest)