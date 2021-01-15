# napisz funkcja która wyznaczy wszystkie dzielniki liczby

def dzielniki(num):
    out = []
    for x in range(1, num+1):
        if num % x == 0:
            out.append(x)
    return out

print(dzielniki(60))