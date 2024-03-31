def funksiya(lst):
    natija = []
    qator = set()
    for element in lst:
        if element not in qator:
            qator.add(element)
        else:
            natija.append(element)
    return natija

# Misol
print(funksiya([2, 2, 1, 4, 5,4, 5, 8, 7, 7, 8]))