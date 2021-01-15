'''napisz funkcje która przyjmie dwa parametry, pierwszy słownik, drugi tuple.
 funkcja ma zazadanie dodanie do słownika klucza który znajdyje sie pod 0 indexem w tupli o wartość z indexu 1. '''

def func(dictionary, tuple):
    dictionary[tuple[0]] = tuple[1]

func({},("rok", 1844))
