import random

names=str(input("Give me everbody's name separated by a comma? "))
name=names.split(", ")
drawn=random.choice(name)
print("Who will pay the bill is {}".format(drawn))

