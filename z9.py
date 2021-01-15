''' napisz funkcja która wyznaczy wszystkie dzielniki pierwsze liczby'''

def dzielniki_pierwsze(num):
    out = []
    for x in range(1, num+1):
        if num % x == 0:
            out.append(x)
    return out

print(dzielniki(60))