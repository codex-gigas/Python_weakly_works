def sumprimes(l):
    k=0
    for i in l:
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                      break
            else:
                k=k+i
    print(k)

sumprimes([-3,-5,3,5])
