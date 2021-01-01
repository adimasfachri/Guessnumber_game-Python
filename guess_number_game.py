'''Create By Adimas Fachri Ranunegoro
    Inpired from Python for Automation book (AI Sweigart) '''

from random import randint as acak 
from os import system, name 
from sys import exit


def game_tebak_angka():

    print("======Selamat Datang di Game Tebak Angka======")
    print("Silahkan tebak dari angka '1' sampai '20'\nKamu hanya punya kesempatan 5X ! ")

    Rahasia = acak(1, 20)
    i = 5

    while(i > 0):

        Angka = int(input("Masukan angka tebakan kamu : "))

        if (Angka < Rahasia):
            i -= 1
            print("Tebakan kamu terlalu rendah!")
            if(i != 0):
                print("Kamu masih punya " + str(i) + " kesempatan lagi\n")
                pause = input("Silahkan Tekan enter untuk lanjut")
                clear()
            else:
                fail_notif()
                lagi()

        elif (Angka > Rahasia):
            i -= 1
            print("Tebakan kamu terlalu tinggi!")
            if(i != 0):
                print("Kamu masih punya " + str(i) + " kesempatan lagi\n")
                pause = input("Silahkan Tekan enter untuk lanjut")
                clear()
            else:
                fail_notif()
                lagi()
            
    
        else :
            print("Selamat Tebakan kamu benar!")
            lagi()
            

def lagi():

    jwb = input("Mau main lagi ? (y/n) : ")

    if(jwb.upper() == "Y"):
        clear()
        game_tebak_angka()
    
    elif(jwb.upper() == "N"):
        print("Terima Kasih Telah memainkan game ini :)")
        exit()

    else:
        print("Input kamu salah!")
        lagi()



def clear():

    if name == 'nt': 
        _ = system('cls')
        

    else:
        _ = system('clear')

def fail_notif():
    print("Kesempatan kamu sudah habis\nSayang sekali kamu gagal buat nebak angkanya :(")
        

if __name__ == "__main__":
    game_tebak_angka()

        


