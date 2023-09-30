Name_fish= "blue graysom"
Fish_colour="light green"
num_fish= input("what is the nmuber of fish")
size_fish=input("what is the size of the fish")
num_fish=int(num_fish)
size_fish=int(size_fish)
demand= num_fish*size_fish
if demand>num_fish:
    print("more profit")
else:
    print("less proft")
if demand<size_fish:
    print("more interest")
else:
    print("no interest")         
    
note=f"The name of my fish  {Name_fish} and the colour  {Fish_colour}"
print(note)
print(len (note))
print(note.lower()+"\n")
print(note.upper()+"\n")
