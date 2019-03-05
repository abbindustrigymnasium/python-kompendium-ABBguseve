import math

VanligKorv2 = int(input("Hur många elever ville ha 2 vanliga korvar?" " " ))
VanligKorv3 = int(input("Hur många elever ville ha 3 vanliga korvar?" " " ))
VegKorv2 = int(input("Hur många elever ville ha 2 vegetariska korvar?" " " ))
VegKorv3 = int(input("Hur många elever ville ha 3 vegetariska korvar?" " " ))

AntalElever = VanligKorv2 + VanligKorv3 + VegKorv2 + VegKorv3
AntalDrickor = AntalElever

SummaVanligKorv2 = VanligKorv2 * 2
SummaVanligKorv3 = VanligKorv3 * 3

SummaVegKorv2 = VegKorv2 * 2
SummaVegKorv3 = VegKorv3 * 3

TotaltVanligKrov = SummaVanligKorv2 + SummaVanligKorv3
TotaltVegKrov = SummaVegKorv2 + SummaVegKorv3

PackVanligKorv = TotaltVanligKrov/8
PackVegKorv = TotaltVegKrov/4

PackVanligKorv = math.ceil(PackVanligKorv)
PackVegKorv = math.ceil(PackVegKorv)

Sum1 = PackVanligKorv * 20.95 
Sum2 = PackVegKorv * 34.95
Sum3 = AntalDrickor * 13.95

AntalPeng = Sum1 + Sum2 + Sum3
AntalPeng = round(AntalPeng)

print(".: UTFLYKTSLISTA :.")
print("----------------------")
print("Såhär många elever vill ha:")
print("2 vanliga korvar  >", VanligKorv2)
print("3 vanliga korvar  >", VanligKorv3)
print("2 veganska korvar  >", VegKorv2)
print("3 veganska korvar  >", VegKorv3)
print("-----------------------")
print("-    INKÖPSLISTA      -")
print("-----------------------")
print("| Vanlig korv:", PackVanligKorv, "förpackningar")
print("| Vegansk korv:", PackVegKorv, "förpackningar")
print("| Dryck:       ", AntalDrickor, "drickor")
print("-----------------------")
print("| ", AntalPeng, "SEK")
print("-----------------------")
