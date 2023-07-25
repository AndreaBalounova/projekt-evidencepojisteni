from pojisteny import Pojisteny
def vytvor_pojisteneho():
    jmeno = input('\nZadejte jméno: ')
    prijmeni = input('Zadejte příjmení: ')
    vek = int(input('Zadejte věk: '))
    telefon = input('Zadejte telefonní číslo: ')
    print("Data byla uložena.\n")

    pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
    pojisteni.append(pojisteny)

def vyhledat_pojisteneho():
    vyhledat_jmeno = input('Zadejte jméno: ')
    vyhledat_prijmeni = input('Zadejte příjmení: ')

    for pojisteny in pojisteni:
        if pojisteny.jmeno == vyhledat_jmeno and pojisteny.prijmeni == vyhledat_prijmeni:
            print(str(pojisteny))
            break
    else:
        print('Pojištěný nebyl nalezen, zkuste prosím znovu.')


def vypis_pojistenych():
    for pojisteny in pojisteni:
       print (str(pojisteny))


def main():
    while True:
        print('==========================\nEVIDENCE POJIŠTĚNÝCH\n==========================\n')
        volba = input('[1] Vytvořit nového pojištěného\n'
                      '[2] Vyhledat pojištěného\n'
                      '[3] Vypsat všechny pojištěné\n'
                      '[4] Konec\n'
                      '\n'
                      'Vyberte si akci: ')

        if volba == '1':
            vytvor_pojisteneho()
        elif volba == '2':
            vyhledat_pojisteneho()
        elif volba == '3':
            vypis_pojistenych()
        elif volba == '4':
            print('Konec aplikace.\n')
            break
        else:
            print('\nVaše volba je neplatná, zkuste prosím znovu.\n')


pojisteni = []
main()
