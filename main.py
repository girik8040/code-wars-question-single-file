'''p1 = "rock"
p2 = "paper"
def wot(p1,p2):
    rock1 =  p1 == "rock"
    paper1 =  p1 == "paper"
    scissors1 = p1 == "scissors"

    rock2 =  p2 == "rock"
    paper2 =  p2 == "paper"
    scissors2 = p2 == "scissors"

    if rock1 == True and rock2 == True:
        return "Draw"#
    if rock1 == True and paper2 == True:
        return "player 2 won!"
    if rock1 == True and scissors2 == True:
        return "player 1 won!"
    if paper1 == True and rock2 == True:
        return "player 2 won!"
    if paper1 == True and paper2 == True:
        return "Draw"#
    if paper1 == True and scissors2 == True:
        return "player 1 won!"
    if scissors1 == True and rock2 == True:
        return "player 2 won!"
    if scissors1 == True and paper2 == True:
        return "player 1 won!"
    if scissors1 == True and scissors2 == True:
        return "Draw"#operator'''

'''
operator = '/'
value1 = 4
value2 = 7
def basic_op(operator, value1, value2):
    min = operator == '-'
    sum = operator == '+'
    div = operator == '/'
    mul = operator == '*'
    if min == True :
        return value1-value2
    if sum == True :
        return value1+value2
    if mul == True :
        return value1*value2
    if div == True :
        return value1/value2
'''
'''n= int(6)
x = (n)**(1/2)
y = x*x == n
print(x," ", y)
'''
'''
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = list(a) #boogie man 
revs  = 0
z = ''
nolen = 0
leng  = len(lst)
while revs < leng : 
    y = ord(lst[nolen]) >= 65 and ord(lst[nolen])<= 90
    print(y)
    if y == True :
        lst.insert(nolen, " ")
        nolen += 1
#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
    revs +=1
    nolen +=1
end = "".join(lst)
print(end)'''
'''
text = "hello world"
slt = text.split()
x = 0
y = "ay"
revs = 0

while revs<'''
'''numbers = [1,4,8,2,5,9,3]
numbers.sort()
print(numbers)'''
'''
revs = 0
x = 0
num = 5
revs2 = 0
middle = int(num/2)
space = ""
l = 0
r = -1
while revs2<num :
    space = space.insert("□")
    revs2+=1
    print(space)
space.split()
print(space)
while revs<num :
    space.append(l,"o")
    space.append(r,"o")
    l += 1
    r -= 1
    revs+=1
    print(space)

'''
'''
num  = 5
arr = [" "]
mi = arr*num
mm = int(5/2)
revs =  0
l = 0
r = 0
while revs <= num :
    l -= 1
    r += 1  
    mi.insert()
    print ()
    revs +=1 
'''
'''
s = "ai"
vo = ["a","e","i","o","u"]
x = False 
revs = 0
if s[0] in vo :
    x =  True
if x == True:
    s += "yay"

    


x = beast.split
y = dish.split
bfir = x[0]
blst = x[-1]
yfir = y[0]
ylst = y[-1]
ft = bfir == yfir
lt = blst == ylst
if ft and lt == True :
    print( True)
else :      #it works:)
    print(False)
'''
    
'''
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num = "("+str(n[0])+str(n[1])+str(n[2])+")" + " "+str(n[3])+str(n[4])+str(n[5])+"-"+str(n[6])+str(n[7])+str(n[8])+str(n[9])
print(n)
print(num)
'''
'''
1660 TI
#here is the kata https://www.codewars.com/kata/59c7e477dcc40500f50005c7/train/python
arr =   [-1]
revs = 0
b = 0
while revs< len(arr):
    nota = arr[revs]%2
    if nota != 0: 
        b += 1
    revs += 1
print(b)
if len(arr)-b <= b :
    print("true")
else :
    print('false')''''''
#add 0.1+0.2 and prove it is equal to 0.3 
sum = float(0.1+0.2)
print(sum)
if sum == 0.3 :
    print('True')
if sum != 0.3:
    print('False')#it will return false :)
#refer this link  https://gauravkk22.medium.com/why-0-1-0-2-0-3-is-false-in-js-mystery-unsolved-with-solution-4f7db2755f18#:~:text=For%20example%2C%200.1%20and%200.2,an%20infinite%20number%20of%20digits.'''

'''
x = 7
i=0
j=0
str=""
min=0
max=x-1
var = ""
for i in range (0,(int(x/2)+1)):
    for j in range (0,x):
            if min==max:
                 var+= (int(x/2))*" " +"x"+(int(x/2))*" " +"\n"
                 break
            if min!=max:
                if((j==min) or (j==max)):
                    var+="x"
                else:
                    var+=" "
    str+="\n"+var
    max-=1 
    min+=1
    var=""

min=int(x/2)-1
max=int(x/2)+1
i=0
j=0
for i in range(0,(int(x/2))):
     for j in range(0,x):
          if((j==min) or (j==max)):
            var+="x"
          else:
            var+=" " 
     str+=var+"\n"
     max+=1 
     min-=1
     var="" 
print (str)
        '''
'''
a = [0, 1, 3, 6, 10]
i=0
j=0
b=[]
sum=0
for i in range(0,len(a)):
    k=i
    for j in range(i,len(a)):
        sum=a[k]+sum
        k+=1
    b[i].append(sum)
    sum=0
b[-1]=0
print (b)'''

arr = []
nos = 5
revs = 0
num = 0
num2 = 1
while revs<= nos :
    
        
    revs+=1
