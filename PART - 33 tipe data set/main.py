# set, himpunan : tidak punya urutan yang sama

# hero = {"batman",
#         "ultramen",
#         "lego betmen",
#         "spiderman"}

# hero.add("wiro sableng")
# hero.add("lord")

hero = set()

hero.add("lord")
hero.add("lego betmen")
hero.add("spider")
hero.add(122)
hero.add(True)
hero.add(3.14)

print(hero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(prima))
