import poggyasz1
import math
print("II/A,B:")
csomag_lista=poggyasz1.fajlbeolvasas()
atlag=poggyasz1.poggyasz_atlagsuly(csomag_lista)
max_index=poggyasz1.legmagasabb(csomag_lista)
print("III/C:")
print(f"Az 51 cm-es pogyászok átlag súlyértéke: {round(atlag)}g")
print("III/D:")
print(f"A legmagasabb csomag méretei: {csomag_lista[max_index].a}x{csomag_lista[max_index].b}x{csomag_lista[max_index].c} és a súlya {csomag_lista[max_index].c}")