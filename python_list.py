# ======== Vytvoření seznamu ========
# Prázdný seznam
prazdny = []              # nic v seznamu
prazdny2 = list()         # alternativní zápis

# Seznam s prvky
cisla = [1, 2, 3, 4, 5]               # čísla
ovoce = ["jablko", "banán", "třešeň"] # texty
smisene = [1, "text", True, 3.14]     # smíšené typy

# Seznam s víc typy
komplet = [
    10,                 # číslo
    3.14,               # desetinné číslo
    "ahoj",             # text
    True,               # boolean
    [1, 2, 3],          # vnořený seznam
    ("a", "b"),         # n-tice
    {"klic": "hodnota"},# slovník
    None                # žádná hodnota
]

# ======== Přístup k prvkům ========
print(cisla[0])    # první prvek
print(cisla[-1])   # poslední prvek

# Řezání seznamu (slicing)
print(cisla[1:3])  # prvky od indexu 1 do 2
print(cisla[:2])   # první dva prvky
print(cisla[3:])   # od čtvrtého do konce

# ======== Přidávání prvků ========
cisla.append(6)               # přidá na konec
cisla.insert(2, 99)           # vloží 99 na index 2

# ======== Odstranění prvků ========
cisla.remove(2)               # odstraní první výskyt 2
del cisla[0]                  # odstraní prvek na indexu 0
prvek = cisla.pop(1)          # vyjme prvek na indexu 1 a vrátí ho

# ======== Základní operace ========
print(len(cisla))             # délka seznamu
print(cisla.count(99))        # kolikrát je 99
print(cisla.index(99))        # první index 99

# ======== Řazení a převracení ========
cisla.sort()                  # seřadí vzestupně
cisla.reverse()               # obrátí pořadí

# ======== Kopie a vymazání ========
novy_seznam = cisla.copy()    # vytvoří kopii
cisla.clear()                 # vymaže všechny prvky

# ======== Generátor seznamu (list comprehension) ========
ctverce = [x**2 for x in range(10)]          # čtverce čísel 0-9
suda_cisla = [x for x in range(20) if x % 2 == 0] # sudá čísla
texty = [f"prvek_{i}" for i in range(5)]    # textové prvky s čísly

# ======== Kombinace a opakování seznamů ========
seznam_1 = [1, 2, 3]
seznam_2 = ["a", "b"]
spojeny = seznam_1 + seznam_2                # spojení seznamů

opak = ["x"] * 5                             # ['x', 'x', 'x', 'x', 'x']

# ======== Smyčky a seznamy ========
for prvek in ovoce:
    print("Ovoce:", prvek)

# Podmínky se seznamem
if "jablko" in ovoce:
    print("Jablko je v seznamu")

# ======== Další užitečné metody ========
ovoce.append("hruška")       # přidání
ovoce.sort()                 # seřadí abecedně
ovoce.reverse()              # obrátí pořadí
ovoce.pop()                  # odstraní poslední prvek
ovoce.clear()                # vymaže všechny prvky

# ======== Seznamy uvnitř seznamů ========
matice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matice[1][2])  # prvek 6 (druhý řádek, třetí sloupec)

# ======== Vytvoření seznamu pomocí range ========
cisla_range = list(range(5))  # [0, 1, 2, 3, 4]

# ======== Převod mezi typy ========
text = "ahoj"
list_z_textu = list(text)     # ['a', 'h', 'o', 'j']

# ======== Kompletní seznam pro začátečníka ========
zacatecnik = [
    1, 2, 3, "text", True, 3.14,
    [10, 20], ("x","y"), None
]

print("Hotovo, seznam připraven!")


# Vytvoření seznamu s různými typy prvků
muj_seznam = [
    10,               # číslo
    3.14,             # desetinné číslo
    "ahoj",           # text
    True,             # boolean
    [1, 2, 3],        # vnořený seznam
    ("a", "b"),       # n-tice
    {"klic": "hodnota"}, # slovník
    None              # žádná hodnota
]

# Přístup k prvkům
print(muj_seznam[0])   # první prvek
print(muj_seznam[-1])  # poslední prvek

# Řezání seznamu (slicing)
print(muj_seznam[1:4]) # prvky od indexu 1 do 3
print(muj_seznam[:3])  # první tři prvky
print(muj_seznam[3:])  # od čtvrtého do konce

# Přidávání prvků
muj_seznam.append("novy prvek")       # přidá na konec
muj_seznam.insert(2, "vlozeny prvek") # vloží na index 2

# Odstranění prvků
muj_seznam.remove(True) # odstraní první výskyt True
del muj_seznam[0]       # odstraní prvek na indexu 0
prvek = muj_seznam.pop(1) # vyjme prvek na indexu 1 a vrátí ho

# Základní operace
print(len(muj_seznam))        # délka seznamu
print(muj_seznam.count("ahoj")) # kolikrát je "ahoj"
print(muj_seznam.index("ahoj")) # první index "ahoj"

# Řazení a převracení
cisla = [5, 2, 9, 1]
cisla.sort()      # seřadí vzestupně
cisla.reverse()   # obrátí pořadí

# Kopie a vymazání
novy_seznam = muj_seznam.copy() # vytvoří kopii
muj_seznam.clear()              # vymaže všechny prvky

# Generátor seznamu (list comprehension)
ctverce = [x**2 for x in range(10)]          # čtverce čísel 0-9
sudy = [x for x in range(20) if x % 2 == 0] # pouze sudá čísla
texty = [f"prvek_{i}" for i in range(5)]    # textové prvky s čísly

# Kombinace seznamů
seznam_1 = [1, 2, 3]
seznam_2 = ["a", "b"]
spojeny = seznam_1 + seznam_2                # spojení seznamů

# Opakování seznamu
opak = ["x"] * 5  # ['x', 'x', 'x', 'x', 'x']

# Iterace přes seznam
for prvek in muj_seznam:
    print(prvek)

# Kontrola přítomnosti prvku
if "ahoj" in muj_seznam:
    print("Prvek 'ahoj' je v seznamu")

