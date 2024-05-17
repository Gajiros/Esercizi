import math
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    
    print('Tempo: 0 Altezza: 0.0')
    altezza += velocita
    velocita -= 96 
    tempo = 1
    
    while (rimbalzi < 5):
        
        if (altezza > 0.0):
            print(f'Tempo: {tempo} Altezza: {altezza}')
            altezza += velocita
            velocita -= 96
            #print(altezza)
        else:
            velocita *= (-0.5)
            altezza *= (-0.5)
            rimbalzi += 1
            print(f'Tempo: {tempo} Rimbalzo!')
            #print(altezza)
        
        tempo += 1

#rimbalzo()

def integerPower(base: int, exp: int) -> int:
    i: int = 1
    result: int = base
    while (i < exp):  
        
        base *= result
        i += 1
        
    return base

#print(integerPower(3, 4))

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    file_compresso: float = 0
    sum_file_size: int = 0
    blocchi_usati: int = 0
    
    for file in files:
        file_compresso = ((file * 80) / 100)
        if (file > (spazio_totale_blocchi * 512)):
            print(f'Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.')
            break
        else:
            if ((sum_file_size + file_compresso) >=512) and ((sum_file_size + file) < 1024):
                blocchi_usati = math.ceil(file_compresso / 512)
                spazio_totale_blocchi = spazio_totale_blocchi - blocchi_usati
                print(f'File di {file} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: {blocchi_usati}. Blocchi rimaneneti: {spazio_totale_blocchi}.')
                file_compresso = 0
                sum_file_size = 0

            elif (file_compresso < 512) and (spazio_totale_blocchi == 1000):
                sum_file_size += file_compresso
                print(f'File di {file} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: 0. Blocchi rimaneneti: {spazio_totale_blocchi}.')
                file_compresso = 0
            else:
                blocchi_usati = math.ceil(file_compresso / 512)
                spazio_totale_blocchi = spazio_totale_blocchi - blocchi_usati
                print(f'File di {file} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: {blocchi_usati}. Blocchi rimaneneti: {spazio_totale_blocchi}.')
                file_compresso = 0
                blocchi_usati = 0


#memorizza_file([1100, 20000, 1048576, 512, 5000])
memorizza_file([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])