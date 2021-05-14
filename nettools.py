print("Hello World")

a,b=0,1
while a < 10000:
    print(a)
    a,b=b,a+b

c="Hello World"
print(c[1:4])
print(c.upper())
print(c.lower())
print(c.replace("H","J"))
x= "ello" in c
print(x)

thislist=["apple","bannana","cherry","orange","wiki","melon","mango"]
print(thislist)
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[2:5])
thislist[1]="Blackberry"
print(thislist)

for x in thislist:
    print(x)
    
if "apple" in thislist:
    print("Yep")
    
print(len(thislist))

thislist.insert(1,"blueberry")
print(thislist)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": "1964"
}

print(thisdict)

print(thisdict["Model"])

print(thisdict.get("Model"))

i=0
while i <6:
    i+=1
    if i == 3:
        continue
    print(i)
    
    
def my_function(fname,lname):
    print("Hello from function land" + fname + lname)
    return print("Im Back")
    
my_function(" Rob ", "Cantrell")

def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)