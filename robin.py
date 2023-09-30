list_food=["rice","yam","amala","beans","egg"]
list_food[2]
print("\n\nBefore shuffling list_food")
for i in range(2,len(list_food)):
    print(list_food[i])

print("\n\nAftershuffling list_food")
print(random.shuffle(list_food))
for item in list_food:
    print(item)
