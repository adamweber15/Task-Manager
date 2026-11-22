# Task Manager

Jednoduchá konzolová aplikace pro správu úkolů vytvořená v jazyce Python.

## Funkcionalita

Aplikace umožňuje:

- Přidávat nové úkoly s názvem a popisem.
- Zobrazovat seznam uložených úkolů.
- Odstraňovat vybrané úkoly.
- Ukončit program prostřednictvím hlavního menu.

Součástí aplikace je také validace uživatelských vstupů, která zabraňuje například přidání úkolu s prázdným názvem nebo popisem.

## Spuštění aplikace

Pro spuštění je potřeba mít nainstalovaný Python 3.

V terminálu otevřete složku projektu a spusťte:

```bash
python3 main.py
```

Aplikace následně zobrazí hlavní menu, ve kterém lze vybírat jednotlivé operace.

## Testování

Aplikace byla podrobena manuálnímu funkčnímu testování zahrnujícímu pozitivní, negativní a hraniční scénáře.

Celkem bylo provedeno **15 testovacích případů**, všechny s výsledkem **Pass**.

Podrobná dokumentace testovacích případů, jejich postupů a výsledků je dostupná v souboru `test_cases.md`.

## Struktura projektu

```text
Task-Manager/
├── main.py
├── test_cases.md
└── README.md
```

## Technologie

- Python 3
- Git a GitHub
- Visual Studio Code
