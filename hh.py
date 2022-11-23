import os

data = {
    "kamu": "been",
    "aku": "sengkok",
    "makan": "ngakan",
    "kemana": "kadimmah",
    "sekarang": "setiyah",
    "malam": "malem",
    "siang": "seang",
    "besok": "lagghuk",
    "cape": "lessoh"
}

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
    print(" ".join(translate))
    translate.clear()

def menu():
    print("""
Translator Sederhana Madura - Indonesia
---------------------------------------
[1]. Madura -> Indonesia
[2]. Indonesia -> Madura
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
        menu()
