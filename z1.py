'''napisz funkcje która przyjmie jeden argument bedący listą stringów,
funkcja ma zwrócic liste intów która bedzie zawierała długość odpowiednich stringów'''

def func(list):
    length = []
    for x in range(len(list)):
        length.append(len(list[x]))
    return length

print(func(['ala', 'ma', 'piegi']))