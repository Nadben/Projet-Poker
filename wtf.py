def occ(mot):
    d = {}
    for c in mot:
        d[c] = d.get(c,0) + 1
    return d

    dict2 = {"FIN": 330}
    d.update(dict2)
    print(d)

print(occ("bananeb tur"))
