import random

def generate_name():
    first_names=["Name1","Name2","Name3","Name4","Name5"]
    last_names=["Surname1","Surname2","Surname3","Surname4","Surname5"]
    
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

for i in range(5):
    print(generate_name())
