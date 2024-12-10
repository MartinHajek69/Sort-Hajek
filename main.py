import random
#pole
arrayy = [-15, 54, 23, -69, 13, -89, 74, 7, 8, 15]
#funkce ktera zjistuje jestli je pole serazene
def is_sorted(arrayy):
    #kontroluje jestli jsou hodnoty ve spravnem poradi
    for i in range(1, len(arrayy)):
        if arrayy[i] < arrayy[i-1]:
            return False
    return True
#definice bogosortu
def bogosort(arrayy):
    count = 0
    #micha pole dokud nebude spravne sezarene
    while not is_sorted(arrayy):
        random.shuffle(arrayy)
        count += 1
        #vypise jaky to je pokus a pole
        print(f"Pokus {count}: {arrayy}")
    print(f"Seznam seřazen po {count} pokusech.")
    return arrayy

print("Bogo sort:", bogosort(arrayy))
#pole
pole = [48, 95, 21, 3, 35, 66, 69, 41, 33, 99]

def bubble_sort():
    n = len(pole)
    #prochazi pole a porovnava ho
    for i in range(n-1):
        for j in range(0, n-i-1):
            #vymeni hodnoty pokud je jedna hodnota vetsi nez druha
            if pole[j] > pole[j+1] :
                pole[j], pole[j+1] = pole[j+1],pole[j]
                #vypise serazene pole
            print(pole)
    return pole
#vypise bubble sort
print("bubble sort:", bubble_sort())
#funkce pro selection sort
def selection_sort(array):
    n = len(array)
    #prochazi cele pole
    for i in range(n):
        min_index = i
        #vyhleda nejmensi hodnotu
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                # vymeni aktualni prvek s nalezenym nejmensim
        array[i], array[min_index] = array[min_index], array[i]
        print(f"Po {i+1} pokusu: {array}")
    return array

# testovani selection sort
selection_array = [48, 95, 21, 3, 35, 66, 69, 41, 33, 99]
print("Selection sort:", selection_sort(selection_array))
# funkce pro Insertion sort
def insertion_sort(array):
        # prochazi seznam od druheho prvku
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Posouváme prvky, které jsou větší nez key o jedno misto doprava
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(f"Po {i} pokusu: {array}")
    return array

# Testování Insertion sort
insertion_array = [48, 95, 21, 3, 35, 66, 69, 41, 33, 99]
print("Insertion sort:", insertion_sort(insertion_array))



