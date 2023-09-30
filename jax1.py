current=["bill","fill","james"]
current[1:2]=["jude","jane"]
print(current)
print(len(current))
print(current[2])

fox=["three","fish","read",]
fox[1:3]=["run"]
print(fox)
fox.insert(2,"orange")
print(fox)
fox.append("runner")
print(fox)
fox.extend(["flicky","judith"])
print(fox)
fox.remove("three")
print(fox)
fox.pop(1)
print(fox)
fox.clear()
print(fox)

blue=["rock","jass","range"]
for i in blue:
    print(i)
for i in range(len(blue)): 
    print("\n"+blue[i])   
z=0
while z<len(fox):
    print(blue[z])
    z=z+1 

name=["tree","rice","fall"]
[print(a) for a in name]
newlist=[]
for v in name:
    if "c"in v:
        newlist.append(v)
print(newlist)
newlist1=[t for t in name if "e" in t]
print(newlist1)
newlist2=[y for y in name if y !="fall"]
print(newlist2)
newlist3=[p for p in name]
print(newlist3)

scoress={"kristal":"100%", "henry":"90%", "praise":"30"}
print(scoress["kristal"])
print(list(scoress))
for k, v in scoress.items():
    print(f"{k} got {v}")
r=scoress.keys()
print(r)
u=scoress.values()
print(u)
