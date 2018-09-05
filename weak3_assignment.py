def descending(l):
  lis=sorted(l)[::-1]
  if lis == l:
    return True
  else:
    return False
def valley(l):
  if(len(l)==0):
    return(True)
  if(len(l)==1):
    return(False)
  if(l[0]<l[1]):
    return(False)
  for i in range(0,len(l)-1):
    if(l[i]<l[i+1]):
      pos=i
      break
    if(l[i]==l[i+1]):
      return(False)
  else:
    return(False)
  for i in range(pos,len(l)-1):
    if(l[i]>=l[i+1]):
      return(False)
  return(True)
def transpose(l):
  return [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
