def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    i: int = 0
    var: int = None
    for key in da_rimuovere:
        var = key
    while (i != da_rimuovere[var]):
        i += 1
        if (var not in lista):
            return lista
        lista.remove(var)
    return lista
#print(rimuovi_elementi([4, 5, 6], {1: 3}))

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    for key in voti:
        for value in key:
            None
                    

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))