'''napisz funkcja która bedie wyliczać pierwiastek liczby, z zadaną dokłdnościa'''

def root(num, rnd):
    return round((num**(1/2)), rnd)

x = int(input("Oblicz pierwiastek z: "))
y = int(input("Z dokładnoscią: "))

print((root(x,y)))