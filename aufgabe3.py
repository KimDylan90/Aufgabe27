# Preise für jede Weinsorte
preis_rot = 12.99
preis_rose = 9.98
preis_weiss = 11.99

# Anzahl der verkauften Flaschen für jede Weinsorte abfragen
anzahl_rot = int(input("Anzahl Rotwein: "))
anzahl_rose = int(input("Anzahl Rosewein: "))
anzahl_weiss = int(input("Anzahl Weißwein: "))

# Gesamtkosten berechnen
gesamtkosten = anzahl_rot * preis_rot + anzahl_rose * preis_rose + anzahl_weiss * preis_weiss

# Ausgabe der Gesamtkosten
print("\nDie Gesamtkosten betragen: %.2f Euro." % gesamtkosten)
