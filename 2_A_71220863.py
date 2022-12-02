def buatKata(str):
    strLength = len(str)
    if strLength % 2 == 0:
       return str[0] + str[1]+str[2],"dan",str[-3]+ str[-2],str[1]
    else :
        midle = int(strLength/2)
        return str[midle - 1 ]+ str[midle]+str[midle+1]
word = input("Masukkan Kata ")
then = buatKata(word)
print("Huruf yang di ambil pada kata ", word,"adalah",then)