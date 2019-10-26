#Ab lot of times when dealing with iterators, we also get a need to keep a count of iterations.
#python program to illustrate
#Enumerate function

l1 =["eat","sleep","repeat"]
s1= "geek"

#creating enumerete objects
obj1= enumerate(l1)
obj2= enumerate(s1)

print(list(obj1))
print(list(enumerate(l1)))

print(list(obj2))
print(list(enumerate(s1)))
#changing start index to 2 from 0

print(list(enumerate(s1,2)))

data1 =[44.000,46.400,43.600,35.000,35.000,32.600]
data2 =[24.800,36.450,23.660,35.124,35.343,12.600]

for i,c in enumerate(data1):
    print("{} > {} ={}".format(i, c, data2[i]))