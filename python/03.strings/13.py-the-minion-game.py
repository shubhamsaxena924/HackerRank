def minion_game(string):
    n = len(string)
    total = (n*(n+1))//2
    vowel = 0
    for i in range(n):
        if(string[i] in 'AEIOU'):
            vowel = vowel+n-i
    conso = total-vowel
    if(vowel > conso):
        print('Kevin', vowel)
    elif(conso > vowel):
        print('Stuart', conso)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
