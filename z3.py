'''napisz funkcje która narysuje linie. Funkcja ma przyjmować dwa parametry,
 pierwsy to długość lini drugi to znaki z jakich ma funkcja wybierać symbol do rysowania lini.
  funkcja wybiera znaki losowo z równym prawdopodobieństwem'''
import random

def line(num, lancuch):
    str_len = len(lancuch)
    for x in range(num):
        rand = random.randint(0, len(lancuch) - 1)
        print(lancuch[rand])

line(5, "*#-")
