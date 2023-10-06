# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44 * 1048576
pages = 100
strs = 50
sym = 25
one_sym = 4
res = volume//(pages*strs*sym*one_sym)
print("Количество книг, помещающихся на дискету:", int(res))
