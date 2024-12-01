#tupple1 = (34, 5.6, "hello")
address = ("12", "Brown Close", "Croydon", "London", "UK", "SM4 5R3")

#unpacking
houseNumber,street,town,city,country,pincode = address
print(houseNumber,street,town,city,country,pincode)

h = 5 #packing
s = "South Lane"
t = "Waddon"
ci = "London"
addr = (h,s,t,ci)

print(addr)

list=["a","b","c"]
# for i in range(3):
#   print(list[i])
# for i in list:
#   print(i)
  
# for i ,item in enumerate(list):
#   print(i,item)
  
  
# def fun():
#   print("h")
# fun()

a=(34,5.4,"abc",[34,54,65])

for i in range(len(list)):
  print(i,list[i])
  
for i in list:
  print(i)
for index,item in enumerate(a):
  print(index,item)

list[2]="abc"
print(list)
a[3][0]=78
print(a[3][0])

tupple2 = (1,2,3,4,5,6,7,8,9,10)
print(tupple2[0], tupple2[-1]) #all values
print(tupple2[:]) #all values
print(tupple2[3:6])
print(tupple2[1:-1])
print(tupple2[:-7])