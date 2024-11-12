a = int(input("ค่า: ")) 
b = []
for i in range(a):
    num1=int(input("ใส่ค่า: "))
    b.append(num1)
value=(sum(b)//len(b))     
print(value)    

