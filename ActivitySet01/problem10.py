while true:
  inp = input('enter the numbers:')
  if inp== 'done' : break
    value = float(inp)
    total=total+value
    count=count+1
    average=total/count
   print('average:',average)