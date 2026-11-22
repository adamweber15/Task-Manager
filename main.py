ukoly = []


def pridat_ukol():
    while True:
        nazev = input("\nZadejte název úkolu: ")
        popis = input("\nZadejte popis úkolu: ")

        if nazev.strip() == "" or popis.strip() == "":
            print("\nNázev ani popis úkolu nesmí být prázdný. Zkuste to znovu.")
        else:
            ukoly.append({"nazev": nazev, "popis": popis})
            print(f"\nÚkol '{nazev}' byl přidán.")
            break


def zobrazit_ukoly():
    print("\nSeznam úkolů:\n")

    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
    else:
        for cislo, ukol in enumerate(ukoly, start=1):
            print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    if len(ukoly) == 0:
        print("\nSeznam úkolů je prázdný. Není co odstranit.")
        return

    zobrazit_ukoly()

    while True:
        volba = input("\nZadejte číslo úkolu, který chcete odstranit: ")

        if not volba.isdigit():
            print("\nNeplatný vstup. Zadejte číslo úkolu.")
            continue

        cislo = int(volba)

        if 1 <= cislo <= len(ukoly):
            odstraneny_ukol = ukoly.pop(cislo - 1)
            print(f"\nÚkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
            break
        else:
            print("\nÚkol s tímto číslem neexistuje. Zkuste to znovu.")


def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu\n")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("\nVyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break
        else:
            print("\nNeplatná volba, zkuste to znovu.")


hlavni_menu()