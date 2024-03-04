CREATE TABLE Teater (
    id INT PRIMARY KEY NOT NULL UNIQUE,
    navn TEXT NOT NULL,
    direktoer_id INT NOT NULL
);

CREATE TABLE Teaterstykke(
    navn TEXT PRIMARY KEY UNIQUE NOT NULL,
    teater_id INT NOT NULL,
    FOREIGN KEY (teater_id) REFERENCES Teater(id)
);

CREATE TABLE Akt (
    id int PRIMARY KEY NOT NULL UNIQUE,
    nummer INT NOT NULL,
    navn TEXT,
    teaterstykke_navn TEXT NOT NULL,
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn)
);

CREATE TABLE Kundeprofil (
    telefon TEXT PRIMARY KEY UNIQUE,
    navn TEXT NOT NULL,
    adresse TEXT NOT NULL
);

CREATE TABLE Ansatt (
    id INT PRIMARY KEY UNIQUE,
    navn TEXT NOT NULL,
    epost TEXT NOT NULL,
    ansattstatus TEXT NOT NULL
);

CREATE TABLE Skuespiller(
    id INT PRIMARY KEY UNIQUE NOT NULL,
    navn TEXT NOT NULL,
    epost TEXT NOT NULL
);

CREATE TABLE AnsattTil (
    ansatt_id INT NOT NULL ,
    teaterstykke_navn TEXT NOT NULL,
    typejobb TEXT NOT NULL,
    FOREIGN KEY (ansatt_id) REFERENCES Ansatt(id),
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    PRIMARY KEY (ansatt_id, teaterstykke_navn),
    UNIQUE (ansatt_id, teaterstykke_navn)
);

CREATE TABLE Sal (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    navn TEXT NOT NULL,
    antallseter INT NOT NULL, 
    teater_id INT NOT NULL,
    FOREIGN KEY (teater_id) REFERENCES Teater(id),
    UNIQUE (navn, teater_id)
);

CREATE TABLE Omraade (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    navn TEXT NOT NULL,
    sal_id TEXT NOT NULL,
    FOREIGN KEY (sal_id) REFERENCES Sal(id),
    UNIQUE (navn, sal_id) 
);

CREATE TABLE Sete (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    setenr INT NOT NULL, 
    radnr INT NOT NULL, 
    omraade_id INT NOT NULL,
    FOREIGN KEY (omraade_id) REFERENCES Omraade(id),
    UNIQUE (setenr, radnr, omraade_id)

);

CREATE TABLE Forestilling (
    id INT PRIMARY KEY UNIQUE,
    tidspunkt DATETIME NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    sal_id TEXT NOT NULL,
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    FOREIGN KEY (sal_id) REFERENCES Sal(id),
    UNIQUE (tidspunkt, teaterstykke_navn)
);

CREATE TABLE Billett (
    id INT PRIMARY KEY UNIQUE,
    pris INT NOT NULL,
    billettype TEXT NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    UNIQUE (billettype, teaterstykke_navn)
);

CREATE TABLE Rolle (
    navn TEXT NOT NULL,
    skuespiller_id INT NOT NULL,
    akt_id INT NOT NULL,
    FOREIGN KEY (skuespiller_id) REFERENCES Skuespiller(id),
    FOREIGN KEY (akt_id) REFERENCES Akt(id),
    PRIMARY KEY (navn, skuespiller_id, akt_id),
    UNIQUE (navn, skuespiller_id, akt_id)
);


CREATE TABLE Bestilling (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    forestilling_id INT NOT NULL,
    tidspunkt DATETIME NOT NULL,
    kunde_telefon TEXT NOT NULL,
  
    FOREIGN KEY (forestilling_id) REFERENCES Forestilling(id),
    FOREIGN KEY (kunde_telefon) REFERENCES Kundeprofil(telefon)
    
);

CREATE TABLE BilletterTilBestilling (
    bestilling_id INT NOT NULL,
    billett_id INT NOT NULL,
    antall INT NOT NULL, 
    FOREIGN KEY (bestilling_id) REFERENCES Bestilling(id),
    FOREIGN KEY (billett_id) REFERENCES Billett(id),

    PRIMARY KEY (bestilling_id, billett_id),
    UNIQUE (bestilling_id, billett_id)
);


CREATE TABLE SeterTilBestilling (
    sete_id INT NOT NULL, 
    bestilling_id INT NOT NULL,
    FOREIGN KEY (sete_id) REFERENCES Sete(id),
    FOREIGN KEY (bestilling_id) REFERENCES Bestilling(id),
    PRIMARY KEY (sete_id, bestilling_id),
    UNIQUE (sete_id, bestilling_id)
);
