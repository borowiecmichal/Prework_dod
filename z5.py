'''napisz funkcje która przyjmie jako parametr liste list, każda z tych list bedzie składać sie ze stringów.
 Funkcja ma zwrócić ilosc wystopien litery p we wszystkich tych stringach'''

def how_many_p(list):
    count_p = 0
    for x in range(len(list)):
        sub_list = list[x]
        for y in range(len(sub_list)):
            word = sub_list[y]
            for z in range(len(word)):
                if word[z] == 'p':
                    count_p += 1
    return count_p

print(how_many_p([["sdsp","kper[[ds[pp","abcdss"],["abp","sss"],['ppp',"fff"]]))