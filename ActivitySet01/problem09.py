# Lists

filename = "dataset/romeo.txt"
fname=input('enter fname:')
fh=open(fname)
lst=list()
for line in fh:
  words=line.split()
  for word in words:
    lst.append(word)
    lst.sort()
print(lst)    