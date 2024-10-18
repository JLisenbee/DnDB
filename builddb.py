import sqlite3

# TODO read in names by parsing until a '(' or '.' character
# TODO read each file from the 'sheets' directory. Not very useful until we can parse for a name, but it would help with automation eventually.
# TODO Learn to parse PDFs to also get races, classes, and level info automatically

db = sqlite3.connect("DnDB.db")

cur = db.cursor()

names = list()
names.append("Aesir Kohtas")
names.append("Gardain Weaselbane")
names.append("Jord")
names.append("Otar Steelwater")

races = list()
races.append("Half Elf")
races.append("Mountain Dwarf")
races.append("Earth Genasi")
races.append("Human")

classes = list()
classes.append("Paladin")
classes.append("Bard")
classes.append("Druid")
classes.append("Wizard")

subclasses = list()
subclasses.append("Devotion")
subclasses.append("Valor")
subclasses.append("Land")
subclasses.append("Transmutation")

levels = list()
levels.append(12)
levels.append(7)
levels.append(11)
levels.append(5)

sheets = list()
sheets.append(open("sheets/Aseir Kohtas (L12).pdf", "rb").read())
sheets.append(open("sheets/Gardain Weaselbane.pdf", "rb").read())
sheets.append(open("sheets/Jord (L11).pdf", "rb").read())
sheets.append(open("sheets/Otar Steelwater (L5).pdf", "rb").read())

# Initiate the table
cur.execute(
    """CREATE TABLE characters (
           name TEXT NOT NULL,
           race TEXT NOT NULL,
           class TEXT NOT NULL,
           subclass TEXT,
           level INTEGER NOT NULL,
           sheet BLOB,
           PRIMARY KEY (name, race, class)
    );
    """
)

query = ""

# Build query to add characters
for i in range(0,len(sheets)):
    query = "INSERT INTO characters (name, race, class, subclass, level, sheet) VALUES (\'{?}\', \'{?}\', \'{?}\', \'{?}\', {?}, {?});".format(names[i], races[i], classes[i], subclasses[i], levels[i], sqlite3.Binary(sheets[i]))
    cur.execute(query)
    

# Add the Characters
cur.execute("SELECT * FROM characters")

db.close()