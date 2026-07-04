import random

#random() - returns random float between 0.0 and 1.0 (1.0 excluded)
print(random.random())

#randint(a,b) - returns random int between a and b(both included
print(random.randint(1,20))

#choice(sequence) - returns a random item from the sequence
l1=[1,2,3,4,5]
print(random.choice(l1))

#shuffel(sequence) - returns the element s shuffled in random order
random.shuffle(l1)
print(l1)