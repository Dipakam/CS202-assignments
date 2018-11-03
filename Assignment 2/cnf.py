fo = open('input.txt','r')
cont = fo.read()
lines = cont.split('\n')
firstRow = lines[0].split(' ')
literals = int(firstRow[2])
clauses = int(firstRow[3])
#print(literals)
#print(clauses)
Clause = []
for x in range(1,clauses+1):
    #print(x)
    row = lines[x]
    intLit = []
    literalRow = row.split(' ')
    for n in literalRow:
        intLit.append(int(n))
    intLit.pop()
    Clause.append(intLit)

#print(Clause)
p = [0 for i in range(literals)]
k = []

def recb(i):
    print (" i is"+str(i))
    print (p)
    if(i==clauses):
        print ("hi")
        k.append(p.copy())
        return -1


    for n in Clause[i]:
        j = p[abs(n)-1]
        if p[abs(n)-1]*n <0:
            continue
        else:
            p[abs(n)-1] = n/abs(n)
            q = recb(i+1)
            if q == -1:
                return -1
            p[abs(n)-1] = j


recb(0)
print (p)
#ans = recb(0)
"""print(ans)
        k =n
        if k*p[abs(k)-1]<0:
            continue
        else:
            if k >0:
                p[k-1]=1
                q= recb(i+1)
                if q==-1:
                    continue
                return q
            else:
                p[-k-1]=-1
                q= recb(i+1)
                if q==-1:
                    continue
                return q
    return -1"""
