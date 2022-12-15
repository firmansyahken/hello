import os
from dictionary import data

M = "\033[91m"
H = "\033[92m"
P = "\033[97m"

translate = []

def madurese_indonesian():
    words = input("Masukkan kalimat bahasa Madura: ")
    words = words.split(" ")
    for word in words:
        for x in data.items():
            if word in x:
                translate.append(x[0])
    print(" ".join(translate))
    translate.clear()
    
def indonesian_madurese():
    words = input("Masukkan kalimat bahasa Indonesia: ")
    words = words.split(" ")
    for word in words:
        if word in data.keys():
            translate.append(data[word])
            continue
        else:
            translate.append(word)
    print("Terjemahan: "+" ".join(translate))
    translate.clear()

def menu():
    print(f"""{M}   
    ______      ___     
   /    " \    /. ")    
  // ____  \  /:  /     
 /  /    ) :)//  /___   
(: (____/ //(   / _  \  
 \        / |:   /_) :) {P}Kelompok{M}
  \"_____/   \_______/  
                        
{P}Translator Sederhana {H}Madura {P}- {M}Indonesia{P}
---------------------------------------
[1]. {H}Madura {P}-> {M}Indonesia{P}
[2]. {M}Indonesia {P}-> {H}Madura{P}
""")

while True:
    menu()
    choice = int(input("Pilih No Menu: "))
    if choice == 1:
        os.system("cls")
        madurese_indonesian()
    elif choice == 2:
        os.system("cls")
        indonesian_madurese()
    else:
        os.system("cls")
        menu()