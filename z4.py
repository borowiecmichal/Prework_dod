'''napisz funkcje która przyjmuje jeden argument. Ten argument bedzie listą stringów,
 funkcja ma zliczyć ilośc wystąpień stringów o długość większej niż 2 które zaczynają
 sie i konczą na tą samą litere'''

def check_list(str_list):
    count=0
    for x in range(len(str_list)):
        word = str_list[x]
        word_len = len(word)
        if word[0] == word[word_len-1]:
            count += 1
    return count

print(check_list(['ala', 'ma', 'ipiegi']))