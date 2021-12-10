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
