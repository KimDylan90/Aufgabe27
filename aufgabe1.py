print("DATENABFRAGE")
print("============")

# Datenabfrage
name = input("Name: ")
vorname = input("Vorname: ")
alter = input("Alter: ")
plz = input("Postleitzahl: ")
wohnort = input("Wohnort: ")

# Ausgabe der eingegebenen Daten
print("\n" + vorname.capitalize() + " " + name.capitalize() + " ist " + alter + " Jahre alt und wohnt in " + plz + " " + wohnort.capitalize() + ".")
