import operator

def find(L,k):
    i=0
    found=False
    while i<len(L) and not found:
        if L[i]==k:
            found=True
        else:
            i=i+1
    return found
def index(L,k):
    i=0
    found=False
    while i<len(L) and not found:
        if L[i]==k:
            found=True
        else:
            i=i+1
    return i
def onlytuple(L):
    L1=[]
    for i in range(0,len(L)):

        if isinstance(L[i],tuple)==True:
            L1.append(L[i])
        else:
            i=i+1
    return L1




lines = [] # initalise to empty list
with open('input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
M=[]
D=[]
L=[]
values=[]
variables=[]
Garbagelist=[]
for statement in lines: # each statement is on a separate line
    token_list = statement.split()
    # split a statement into a list of tokens



    for i in token_list:
      if i.isnumeric()==True and i not in L:
                    L.append(int(i))



    if find(token_list,'+')==True:

                    L.append(eval(token_list[index(token_list,'+')-1])+eval(token_list[index(token_list,'+')+1]))

    elif find(token_list,'-')==True:
        if token_list[index(token_list,'-')-1]!='=':

                    L.append(eval(token_list[index(token_list,'-') - 1]) - eval(token_list[index(token_list,'-') + 1]))

    elif find(token_list,'*')==True:

                    L.append((int(token_list[ index(token_list,'*')- 1]))  * (int(token_list[index(token_list,'*') + 1])))

    elif find(token_list,'/')==True:

                    L.append((eval(token_list[index(token_list,'/') - 1])) / (eval(token_list[index(token_list,'/') + 1])))
    elif find(token_list,'<')==True:
        if token_list[index(token_list,'<')-1]<token_list[index(token_list,'<')+1]:
                    L.append(str(True))
        else:
                    L.append('False')
    elif find(token_list,'>')==True:
        if token_list[index(token_list,'>')-1]>token_list[index(token_list,'>')+1]:
                    L.append(str(True))
        else:
                    L.append(str(False))

    elif find(token_list,'==')==True:
        if token_list[index(token_list,'==')-1]==token_list[index(token_list,'==')+1]:
                    L.append(str(True))
        else:
                    L.append(str(False))
#>=, <=
    for i in range(0,len(token_list)):

      if token_list[i].find('=')!=-1 :
            if len(token_list)==i+2:
                locals()[token_list[i-1]]=eval(token_list[i+1])
                if find(L,eval(token_list[i-1]))==True:
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))
                elif token_list[i-1].isalpha()==True and token_list[i+1].isalpha()==True:
                    locals()[token_list[i-1]]=eval(token_list[i+1])
                    L.append(eval(token_list[i+1]))
                    L.append((token_list[i-1],0))

            elif token_list[i+1].find('-')!=-1 and len(token_list)==i+3 :

                ops = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,  # use operator.div for Python 2
                    '%': operator.mod,
                    '^': operator.xor}
                locals()[token_list[i-1]]=ops['-'](0,eval(token_list[i+2]))
                L.append(eval(token_list[i-1]))
                L.append((-eval(token_list[i-1])))
                L.append((token_list[i-1],index(token_list,eval(token_list[i-1]))))
            elif token_list[i+2].find('<')!=-1 and len(token_list)==i+4:
                if token_list[index(token_list,'<')-1]<token_list[index(token_list,'<')+1]:
                    locals()[token_list[i-1]]=True

                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))
                else:
                    locals()[token_list[i-1]]=False
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))
            elif token_list[i+2].find('>')!=-1 and len(token_list)==i+4:
                if token_list[index(token_list,'>')-1]>token_list[index(token_list,'>')+1]:
                    locals()[token_list[i-1]]=True
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))
                else:
                    locals()[token_list[i-1]]=False
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))

            elif token_list[i+2].find('==')!=-1 and len(token_list)==i+4:
                if token_list[index(token_list,'==')-1]==token_list[index(token_list,'==')+1]:
                    locals()[token_list[i-1]]=True
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))
                else:
                    locals()[token_list[i-1]]=False
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))


            elif len(token_list)!= i+2  :
                ops = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,  # use operator.div for Python 2
                    '%': operator.mod,
                    '^': operator.xor}

                locals()[token_list[i-1]]=ops[token_list[i+2]](eval(token_list[i+1]),eval(token_list[i+3]))


                if find(L,eval(token_list[i-1]))==True:
                    L.append((token_list[i-1],index(L,eval(token_list[i-1]))))


#>=, <=

for i in L:
    if isinstance(i,int)==True and i not in M:
        M.append(i)
    elif isinstance(i,tuple)==True and eval(i[0]) in M and i[0].isnumeric()==False :
        M.append((i[0],index(M,eval(i[0]))))
print(M)

for i in M:
    if isinstance(i,tuple)==True :
      print(i[0],eval(i[0]), sep="=")

for i in M:
    if isinstance(i,tuple)==True:
        values.append(eval(i[0]))

for i in M:
    if isinstance(i,int)==True and i not in D:
        D.append(i)
for i in M:
    if isinstance(i,tuple)==True:
        variables.append(i[0])


for i in D:
    if i not in values:
          Garbagelist.append(i)
print('Garbagelist is',Garbagelist,sep='=')



#x = 1 + 3
#y = x - x
#z = - 1
#g = - z
#f = 3 > 5
#h = 8 < 0
#q = 3 * 4
#s = 12 / 4















