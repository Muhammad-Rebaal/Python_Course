print("Welcome to python Course")
print("hello world")
print("Power"); print("Ranger")
name="M.Rebaal"
if name=="M.Rebaal":
    print(name)
def say_hello():
   print("hello There!")
   print(say_hello())
#In Order to add comment,Press("#")
a=1 
print(a)
#Ways of writing a var.
#snake_case
#camelCase
a=b=c=10 #means a,b & c have value of 10
print(a)
print(b)
print(c)
pure,good,nice=1,2,3
print(pure)
print(good)
print(nice)
#Works line by line
m=5
print(m)
m=10
print(m)

#del var_name means to delete the var if we run it the we get what var is not defined,so I'm commenting out to avoid any error.
# del n
# print(n)

#Basic Data Types

p=10
q=4.4
r="power"
s=[1,2,3,4]
v=True
example_et={1,'hello',4.5,"A"}
print(type(p))
print(type(q))
print(type(r))
print(type(s))
print(type(v))
print(type(example_et))

#Strings

#2 ways of writing string single or double quotation
w='by'
x="by"
print(w)
print(x)
print(w,x)

#In order to add mutiple line use  "\"
y="This is a single line code"
z="This is a mutiple \
   code"
print(z)
print(y)
 
#Concatination (joining of strings)
print(y+z)

ab="M.Rebaal"
print(ab[1])
print(len(ab))

#Input 

#When using an input_function the class u get is a string coz usually we use a string 
num1=input("Enter your 1st Numebr:")
num2=input("Enter your 2nd Numebr:")
print(num1,num2)
print(num1+num2)#combine given numbers coz they are in string
print(int(num1)+int(num2))
print(type(int(num1)))
str1=input("Enter your  first name:")
str2=input("Enter your second name:")
print("Hello",'',str1+str2)
print("Hello",str1+str2)
#format command get the value of var inside the (by_name) and put it into the string placeholder,the string placeholder is defined by a curly bracket{}
print('Hello {}{}'.format(str1,str2))

#Comparison Operator
print(10==10)

#Math & Logical Operator

#Airhmatic Operations

comparison_operator =3  
print(comparison_operator==3)
print(3**3)#yani 3 ki power 3

#Addition
print(2+2)
#Subraction
print(2-2)
#Multiplication
print(2*2)
#Division
print(35/5)

#Logical Operations
#(1)
#Correct
ba=True
bc=True
if ba and bc:
   print("All True!")
#Incorrect
cb=False
dc=True
if cb and dc:
   print("All True!") #Won't run

#(2)
#Correct
cd=True
de=False
if cd or de:
   print("All True!")
#Incorrect 
ed=False
ef=False
if ed or ef:
   print("All true!") 

#(3)
#Correct
ee=False
ff=False
if not(ee) or not(ff):
   print("All true!") 

#Incorrect
aa=True
bb=True
if not(aa) or not(bb):
   print("All true!")

#If ,Else and elif(else if)

#If
Bill_Total=115
discount1=10
if Bill_Total>100:
   print("Bill is Greater than 100!")
   total_bill=Bill_Total-discount1
print("Total_Bill:"+ str(total_bill))

Bill_Total1=95
discount2=10
if Bill_Total1>100:
   print("Bill is Greater than 100!")
   Bill_Total1=Bill_Total1-discount2
   
   
print("Total_Bill:"+ str(Bill_Total1))

#Else
Bill_Total2=95
discount3=10
if Bill_Total2>100:
   print("Bill is Greater than 100!")
   Bill_Total2=Bill_Total2-discount3
else:
   print("Bill is less than one!")
   
   
print("Total_Bill:"+ str(Bill_Total2))

#elif (else_if)
Bill_Total4=210
discount4=10
discount5=20
if Bill_Total4>100 and Bill_Total4<200:
   print("Bill is Greater than 100!")
   Bill_Total4=Bill_Total4-discount4
elif Bill_Total4>200:
   print("Bill is greater than 200!")
   Bill_Total4=Bill_Total4-discount5
else:
   print("Bill is less than one!")
   
   
print("Total_Bill:"+ str(Bill_Total4))

#Light is currently off
#The 1st cond. chks does the current is flowing  but the value of current is initially false,so the 1st cond. won't run.yani k agr cond. false hai to print kro lekin yaha to cond. same hai so isne print nhi kia
#The 2nd cond. chks the same but the cond. here not current means false  aur ye cond. true hai to isne print krdia
current = False #current nhi arha
#IF
if current:
    current = False #ye uper wale k opp. main bol rha hai.
    print('Turning light off')

if not current:
    current = True #ye uper wale k opp. main nhi bol rha hai.
    print('Turning light on')

#ELSE

current1 = False

if current1:
    current = False
    print('Turning light off')
else: 
    curren2t = True
    print('Turning light on')

#ELIF

loyalty_customer = True
total_bill = 124


if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

#If and Match statement
       
         #IF

http_status = 1000
if http_status ==200 or http_status == 201:
   print("Success")
elif http_status == 400:
   print("Bad Request")
elif http_status== 404:
   print("Not Found")
elif http_status == 500 or http_status == 501:
   print("Server Error")
else:
   print("Unknown")
   
#Looping


for ib in range(10):
   print("loading...",ib)

Profession=["Data-Scientist","Cyber-Expert","Software-Engineer","AI-Engineer"]

for  etc in Profession:
   print("I want to be a",etc ) 

#While loop
count=0
fav=["cake","apple","mango","grapes"]
while count<len(fav):
    print("I like this",fav[count])
    count+=1
    
#IF statement acts same by using enumerate()
for igx,item in enumerate(fav):
   print(igx,item)

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

