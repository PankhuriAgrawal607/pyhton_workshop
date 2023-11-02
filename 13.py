d={'x':10,'y':20,'z':30}                     #1 question
for key,value in d.items():
    print(f"{key}:{value}")



b={num:num*num  for num in range(0,6)}                 #2 question
print(b)


a={num:num*num for num in range(1,16)}              #3 question 
print(a)



d1={1:10,2:20,3:30,4:40,5:50}
a=int(input("enter key:"))
if a in d1:
    print("present")
else:
    print("not present")
