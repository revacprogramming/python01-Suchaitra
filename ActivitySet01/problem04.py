# Conditional Execution

X="Reva cse@bangalore new"
Y=X.find('@')
print(Y)

A=X.find(' ',Y)
print(A)

B = X[Y+1 : A]
print(B)
