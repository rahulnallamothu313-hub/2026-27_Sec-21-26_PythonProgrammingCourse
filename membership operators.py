#membership operators.
a='area'
result='a' in 'area'
print("result of ",'a', "in",'area', "is :",result)

a=[1,2,3,4,5]
result=10 not in a
print("result of ",10, "not in",a, "is :",result)

a=[1,2,3,4,5]
result=4 in a
print("result of ",4, " in",a, "is :",result)

a=[1,2,3,4,5]
result=7  in a
print("result of ",7, " in",a, "is :",result)

a={1,2,3,4,5}
result=3 in a
print("result of ",3, " in",a, "is :",result)

a={1,2,3,4,5,6}
result=7 not in a
print("result of ",7, "not in",a, "is :",result)

a={'name':'city'}
result='name' in a
print("result of ",'name', "in",a, "is :",result)


a={'location':' name'}
result='location' not in a
print("result of ",'location', "not in",a, "is :",result)
