a=10
result= a > 15 and a < 20 #and operator
print("result of",a,"> 15 and",a,"<20:",result)

result= a < 15 and a > 5 #and operator for both statements true
print("result of",a,"< 15 and",a,">5:",result)

result= a > 15 or a < 20 #or operator for true
print("result of",a,"> 15 or",a,"<20:",result)

result= a > 15 or a > 20 #or operator for false
print("result of",a,"> 15 or",a,">20:",result)

result= not(a < 15 and a > 5) #not operator for false
print("result of not(",a,"<15 not",a,">5) is:",result)

result= not(a >15 and a > 5) #not operator for true
print("result of not(",a,">15 not",a,">5) is:",result)