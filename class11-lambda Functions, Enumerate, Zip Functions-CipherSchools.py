def func():
    return 1+4

lambda a,b: a+b

print("Hello World")

show = print

show("something")

names=["Meehir","Tanishq","Parnish","Prakhar"]
for name in enumerate(names):
    print(name)


a=5
b=9

a,b = b,a
print(a,b)


a=[1,2]
b,c=a
print(b,c)


names=["Meehir","Tanishq","Parnish","Prakhar"]
scores=[50,80,90,70]

for name,score in zip(names,scores):
    print(name,"-",score)
