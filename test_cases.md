# Testovací případy – Task Manager

## 1. Funkce hlavni_menu()

### TC01 – Výběr platné možnosti z hlavního menu

- **Popis:** Ověření, že volba čísla 1 správně spustí funkci `pridat_ukol()`.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Spusťte program. 2. Ověřte zobrazení hlavního menu. 3. Zadejte `1` a potvrďte Enterem.
- **Očekávaný výsledek:** Program spustí funkci `pridat_ukol()`.
- **Skutečný výsledek:** Funkce byla spuštěna a zobrazila výzvu k zadání názvu úkolu.
- **Stav:** Pass
- **Poznámky:** Ověření základní navigace v hlavním menu.

### TC02 – Zadání neplatné možnosti v hlavním menu

- **Popis:** Ověření reakce programu na neplatnou volbu.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Spusťte program. 2. Zadejte `9`. 3. Potvrďte Enterem.
- **Očekávaný výsledek:** Program zobrazí upozornění na neplatnou volbu a znovu nabídne hlavní menu.
- **Skutečný výsledek:** Program zobrazil upozornění „Neplatná volba, zkuste to znovu.“ a hlavní menu.
- **Stav:** Pass
- **Poznámky:** Ověření ošetření neplatné volby.

### TC12 – Správné ukončení programu

- **Popis:** Ověření správného ukončení programu.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Zadejte `4`. 2. Potvrďte Enterem.
- **Očekávaný výsledek:** Program zobrazí „Konec programu.“ a ukončí se.
- **Skutečný výsledek:** Program zobrazil potvrzení a ukončil se.
- **Stav:** Pass
- **Poznámky:** Ověření korektního ukončení aplikace.

## 2. Funkce pridat_ukol()

### TC03 – Přidání nového úkolu

- **Popis:** Ověření přidání úkolu s platným názvem a popisem.
- **Vstupní podmínky:** Program je spuštěný a seznam úkolů je prázdný.
- **Kroky testu:** 1. Vyberte `1`. 2. Zadejte název `Nakoupit` a popis `Koupit mléko`. 3. Vyberte `2` a ověřte seznam.
- **Očekávaný výsledek:** Program uloží úkol a zobrazí jej v seznamu.
- **Skutečný výsledek:** Úkol byl přidán a správně zobrazen.
- **Stav:** Pass
- **Poznámky:** Ověření základní funkčnosti přidávání úkolů.

### TC04 – Přidání úkolu s prázdným názvem

- **Popis:** Ověření, že nelze přidat úkol bez názvu.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Vyberte `1`. 2. Název ponechte prázdný. 3. Zadejte popis `Testovací popis`.
- **Očekávaný výsledek:** Program zobrazí upozornění a vyžádá nové zadání.
- **Skutečný výsledek:** Program odmítl prázdný název a znovu vyzval k zadání.
- **Stav:** Pass
- **Poznámky:** Ověření povinného názvu úkolu.

### TC05 – Přidání úkolu s prázdným popisem

- **Popis:** Ověření, že nelze přidat úkol bez popisu.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Vyberte `1`. 2. Zadejte název `Uklidit`. 3. Popis ponechte prázdný.
- **Očekávaný výsledek:** Program zobrazí upozornění a vyžádá nové zadání.
- **Skutečný výsledek:** Program odmítl prázdný popis a znovu vyzval k zadání.
- **Stav:** Pass
- **Poznámky:** Ověření povinného popisu úkolu.

### TC13 – Zadání pouze mezer při přidávání úkolu

- **Popis:** Ověření odmítnutí názvu tvořeného pouze mezerami.
- **Vstupní podmínky:** Program zobrazuje hlavní menu.
- **Kroky testu:** 1. Vyberte `1`. 2. Do názvu zadejte tři mezery. 3. Zadejte popis `Testovací popis`.
- **Očekávaný výsledek:** Program odmítne název a vyžádá nové zadání.
- **Skutečný výsledek:** Program zobrazil upozornění a znovu vyzval k zadání názvu.
- **Stav:** Pass
- **Poznámky:** Ověření validace vstupu pomocí `strip()`.

## 3. Funkce zobrazit_ukoly()

### TC06 – Zobrazení prázdného seznamu úkolů

- **Popis:** Ověření zobrazení seznamu bez uložených úkolů.
- **Vstupní podmínky:** Program je nově spuštěný a seznam je prázdný.
- **Kroky testu:** 1. Spusťte program. 2. Vyberte `2`. 3. Ověřte výstup.
- **Očekávaný výsledek:** Program zobrazí „Seznam úkolů je prázdný.“
- **Skutečný výsledek:** Program správně zobrazil informaci o prázdném seznamu.
- **Stav:** Pass
- **Poznámky:** Ověření chování při nulovém počtu úkolů.

### TC07 – Zobrazení více uložených úkolů

- **Popis:** Ověření zobrazení více úkolů ve správném pořadí.
- **Vstupní podmínky:** Seznam úkolů je prázdný.
- **Kroky testu:** 1. Přidejte `Nakoupit – Koupit mléko`. 2. Přidejte `Uklidit – Vysát pokoj`. 3. Vyberte `2`.
- **Očekávaný výsledek:** Program zobrazí oba úkoly ve správném pořadí a s číslováním.
- **Skutečný výsledek:** Oba úkoly byly správně zobrazeny.
- **Stav:** Pass
- **Poznámky:** Ověření pořadí a číslování úkolů.

## 4. Funkce odstranit_ukol()

### TC08 – Úspěšné odstranění úkolu

- **Popis:** Ověření odstranění vybraného úkolu.
- **Vstupní podmínky:** Seznam obsahuje úkoly `Nakoupit` a `Uklidit`.
- **Kroky testu:** 1. Vyberte `3`. 2. Zadejte číslo `1`. 3. Vyberte `2` a ověřte seznam.
- **Očekávaný výsledek:** Úkol `Nakoupit` bude odstraněn a zůstane pouze `Uklidit`.
- **Skutečný výsledek:** Vybraný úkol byl odstraněn a seznam aktualizován.
- **Stav:** Pass
- **Poznámky:** Ověření správného odstranění úkolu.

### TC09 – Odstranění neexistujícího úkolu

- **Popis:** Ověření reakce na zadání neexistujícího čísla úkolu.
- **Vstupní podmínky:** Seznam obsahuje jeden úkol `Uklidit`.
- **Kroky testu:** 1. Vyberte `3`. 2. Zadejte číslo `9`. 3. Potvrďte Enterem.
- **Očekávaný výsledek:** Program upozorní na neexistující úkol a vyžádá nové číslo.
- **Skutečný výsledek:** Program zobrazil upozornění a umožnil opakované zadání.
- **Stav:** Pass
- **Poznámky:** Ověření neplatného čísla mimo rozsah seznamu.

### TC10 – Zadání nečíselné hodnoty při odstraňování úkolu

- **Popis:** Ověření reakce na textový vstup místo čísla úkolu.
- **Vstupní podmínky:** Seznam obsahuje úkol `Uklidit`.
- **Kroky testu:** 1. Vyberte `3`. 2. Zadejte `abc`. 3. Potvrďte Enterem.
- **Očekávaný výsledek:** Program zobrazí „Neplatný vstup. Zadejte číslo úkolu.“
- **Skutečný výsledek:** Program odmítl textový vstup a vyžádal číslo úkolu.
- **Stav:** Pass
- **Poznámky:** Ověření validace číselného vstupu.

### TC11 – Odstranění úkolu z prázdného seznamu

- **Popis:** Ověření odstranění úkolu při prázdném seznamu.
- **Vstupní podmínky:** Program je nově spuštěný a seznam je prázdný.
- **Kroky testu:** 1. Spusťte program. 2. Vyberte `3`. 3. Ověřte výstup.
- **Očekávaný výsledek:** Program zobrazí „Seznam úkolů je prázdný. Není co odstranit.“
- **Skutečný výsledek:** Program zobrazil upozornění a vrátil se do hlavního menu.
- **Stav:** Pass
- **Poznámky:** Ověření odstranění z prázdného seznamu.

### TC14 – Zadání čísla 0 při odstraňování úkolu

- **Popis:** Ověření odmítnutí čísla 0 jako neplatného čísla úkolu.
- **Vstupní podmínky:** Seznam obsahuje jeden úkol `Nakoupit`.
- **Kroky testu:** 1. Vyberte `3`. 2. Zadejte `0`. 3. Potvrďte Enterem.
- **Očekávaný výsledek:** Program zobrazí upozornění na neexistující úkol a vyžádá nové číslo.
- **Skutečný výsledek:** Program odmítl číslo 0 a znovu vyzval k zadání.
- **Stav:** Pass
- **Poznámky:** Ověření spodní hranice platného rozsahu.

### TC15 – Odstranění posledního úkolu

- **Popis:** Ověření odstranění posledního zbývajícího úkolu.
- **Vstupní podmínky:** Seznam obsahuje jediný úkol `Nakoupit`.
- **Kroky testu:** 1. Vyberte `3`. 2. Zadejte `1`. 3. Vyberte `2` a ověřte seznam.
- **Očekávaný výsledek:** Úkol bude odstraněn a program zobrazí prázdný seznam.
- **Skutečný výsledek:** Poslední úkol byl odstraněn a seznam byl prázdný.
- **Stav:** Pass
- **Poznámky:** Ověření odstranění posledního záznamu.

---

## Závěrečné vyhodnocení

Celkem bylo manuálně provedeno **15 testovacích případů** zaměřených na hlavní funkce programu, validaci vstupů a hraniční situace.

**Výsledek:** 15 Pass / 0 Fail.

Všechny provedené testy byly úspěšné. V testovaných scénářích nebyly zjištěny žádné chyby.