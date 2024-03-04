CREATE TABLE Teater (
    id INT PRIMARY KEY NOT NULL,
    navn TEXT,
    adresse TEXT
);

CREATE TABLE Teaterstykke(
    navn TEXT PRIMARY KEY,
    teater_id INT,
    FOREIGN KEY (teater_id) REFERENCES Teater(id)
);

CREATE TABLE Akt (
    nummer INT,
    navn TEXT,
    teaterstykke_navn TEXT,
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    PRIMARY KEY (nummer, teaterstykke_navn)
);

CREATE TABLE Kundeprofil (
    telefon TEXT PRIMARY KEY,
    navn TEXT,
    adresse TEXT
);

CREATE TABLE Ansatt (
    id INT PRIMARY KEY,
    navn TEXT,
    epost TEXT,
    ansattstatus TEXT
);

CREATE TABLE Skuespiller(
    id INT PRIMARY KEY,
    navn TEXT,
    epost TEXT
);

CREATE TABLE Ansattil (
    ansatt_id INT,
    teaterstykke_navn TEXT,
    typejobb TEXT,
    FOREIGN KEY (ansatt_id) REFERENCES Ansatt(id),
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    PRIMARY KEY (ansatt_id, teaterstykke_navn)
);

CREATE TABLE Sal (
    navn TEXT,
    antall INT, 
    teater_id INT,
    FOREIGN KEY (teater_id) REFERENCES Teater(id),
    PRIMARY KEY (navn, teater_id)
);

CREATE TABLE Omraade (
    navn TEXT,
    sal_navn TEXT,
    FOREIGN KEY (sal_navn) REFERENCES Sal(navn),
    PRIMARY KEY (navn, sal_navn)
);

CREATE TABLE Sete (
    setenr INT, 
    radnr INT, 
    omraade_navn TEXT,
    FOREIGN KEY (omraade_navn) REFERENCES Omraade(navn),
    PRIMARY KEY(setenr, radnr, omraade_navn)
);

CREATE TABLE Forestilling (
    tidspunkt DATETIME,
    teaterstykke_navn TEXT,
    sal_navn TEXT,
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    FOREIGN KEY (sal_navn) REFERENCES Sal(navn)
);

CREATE TABLE Billett (
    id INT PRIMARY KEY,
    pris INT
);

CREATE TABLE Bestilling (
    bestillings_id INT PRIMARY KEY
);
