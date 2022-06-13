a=34
b="Harry"
#b="Harry's"  -->#Use this if you have single quotes in your strings
print(type(b))

CATENATING:
greeting="good morning"
name="Harry"
#print(type(name))
#print(greeting+name)
c=greeting+name
print(c)

Axises the character:
name="Harry"
print(name[0])
#use only square brackett

STRING SLICING:
print(name[0:3])
#here 3 is not include only 0,1,2 is there
print(name[1:4])
print([:4])
#is same as [0:4]
print([1:])
#from 1st till end

name ="Harry"
c=name[-4:-1]
#same as name[1:4]

name="HARRY"
d=name[1:4:1]
print(d)
name="harryisgood"
d=name[0::2]
print(d)
#prints alternate characters

#parsing and extracting(pdf)
X="Reva cse@bangalore new"
Y=X.find('@')
print(Y)

A=X.find(' ',Y)
print(A)

B = X[Y+1 : A]
print(B)
