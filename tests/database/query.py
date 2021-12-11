CREATE_WEAPONS = '''CREATE TABLE Weapons (
                 weapon TEXT PRIMARY KEY,
                 reload_speed INT,
                 rotation_speed INT,
                 diameter INT,
                 power_volley INT,
                 count INT);'''
    
CREATE_HULLS = '''CREATE TABLE Hulls (
               hull TEXT PRIMARY KEY,
               armor INT,
               type INT,
               capacity INT);'''
    
CREATE_ENGINES = '''CREATE TABLE Engines (
                 engine TEXT PRIMARY KEY,
                 power INT,
                 type INT);'''
    
CREATE_SHIPS = '''CREATE TABLE Ships (
               ship TEXT PRIMARY KEY,
               weapon TEXT,
               hull TEXT,
               engine TEXT,
               FOREIGN KEY (weapon) REFERENCES Weapons (weapon),
               FOREIGN KEY (hull) REFERENCES Hulls (hull),
               FOREIGN KEY (engine) REFERENCES Engines (engine));'''

INSERT_WEAPONS = '''INSERT INTO Weapons ({}) VALUES ({});'''

INSERT_HULLS = '''INSERT INTO Hulls ({}) VALUES ({});'''

INSERT_ENGINES = '''INSERT INTO Engines ({}) VALUES ({});'''

INSERT_SHIPS = '''INSERT INTO Ships ({}) VALUES ({});'''

UPDATE_SHIPS = '''UPDATE Ships
               SET {} = {}
               WHERE ship = {};'''

UPDATE_WEAPONS = '''UPDATE Weapons
                 SET {} = {}
                 WHERE weapon = {};'''

UPDATE_HULLS = '''UPDATE Hulls
               SET {} = {}
               WHERE hull = {};'''

UPDATE_ENGINES = '''UPDATE Engines
                 SET {} = {}
                 WHERE engine = {};'''
            