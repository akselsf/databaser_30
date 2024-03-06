CREATE TABLE Teater (
    navn TEXT NOT NULL PRIMARY KEY UNIQUE,
    direktoer_id INT NOT NULL,
    CONSTRAINT fk_direktoer_id FOREIGN KEY (direktoer_id) REFERENCES Ansatt(id)
);

CREATE TABLE Teaterstykke(
     navn TEXT NOT NULL PRIMARY KEY UNIQUE
);

CREATE TABLE Akt (
    nummer INT NOT NULL,
    navn TEXT,
    teaterstykke_navn TEXT NOT NULL,
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),

    PRIMARY KEY (nummer, teaterstykke_navn),
    UNIQUE (nummer, teaterstykke_navn)
);

CREATE TABLE Kundeprofil (
    telefon TEXT PRIMARY KEY UNIQUE,
    navn TEXT NOT NULL,
    adresse TEXT NOT NULL
);

CREATE TABLE Ansatt (
    id INTEGER PRIMARY KEY UNIQUE NOT NULL ,
    navn TEXT NOT NULL,
    epost TEXT NOT NULL,
    ansattstatus TEXT NOT NULL
);

CREATE TABLE Skuespiller(
    id INTEGER PRIMARY KEY UNIQUE NOT NULL ,
    navn TEXT NOT NULL,
    epost TEXT NOT NULL
);

CREATE TABLE AnsattTil (
    ansatt_id INT NOT NULL ,
    teaterstykke_navn TEXT NOT NULL,
    typejobb TEXT NOT NULL,

    CONSTRAINT fk_ansatt_id FOREIGN KEY (ansatt_id) REFERENCES Ansatt(id),
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    PRIMARY KEY (ansatt_id, teaterstykke_navn),
    UNIQUE (ansatt_id, teaterstykke_navn)

);

CREATE TABLE Sal (

    navn TEXT NOT NULL,
    antallseter INT NOT NULL, 
    teater_navn TEXT NOT NULL,
    CONSTRAINT fk_teater_navn FOREIGN KEY (teater_navn) REFERENCES Teater(navn),

    PRIMARY KEY (navn, teater_navn),
    UNIQUE (navn, teater_navn)
);

CREATE TABLE Omraade (
    navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,
    CONSTRAINT fk_sal_key FOREIGN KEY (sal_navn, teater_navn) REFERENCES Sal(navn, teater_navn),

    PRIMARY KEY (navn, sal_navn, teater_navn),
    UNIQUE (navn, sal_navn, teater_navn)


);

CREATE TABLE Rad (

    rad_nr INT NOT NULL, 
    omraade_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,

    CONSTRAINT fk_omraade_key FOREIGN KEY (omraade_navn,sal_navn, teater_navn) REFERENCES Omraade(navn, sal_navn, teater_navn),

    PRIMARY KEY (rad_nr, omraade_navn, sal_navn, teater_navn),
    UNIQUE (rad_nr, omraade_navn, sal_navn, teater_navn)


);

CREATE TABLE Sete (

    sete_nr INT NOT NULL, 
    rad_nr INT NOT NULL, 
    omraade_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,

    CONSTRAINT fk_rad_key FOREIGN KEY (rad_nr, omraade_navn, sal_navn, teater_navn) REFERENCES Rad(rad_nr, omraade_navn, sal_navn, teater_navn),

    PRIMARY KEY (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn),
    UNIQUE (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn)

);

CREATE TABLE Forestilling (
    tidspunkt DATETIME NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    
   CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
   CONSTRAINT fk_sal_navn FOREIGN KEY (sal_navn) REFERENCES Sal(navn),

    PRIMARY KEY (tidspunkt, teaterstykke_navn),
    UNIQUE (tidspunkt, teaterstykke_navn)

);

CREATE TABLE Billett (
    pris INT NOT NULL,
    billettype TEXT NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    
    PRIMARY KEY (billettype, teaterstykke_navn),
    UNIQUE (billettype, teaterstykke_navn)
);

CREATE TABLE Rolle (
    navn TEXT NOT NULL,
    skuespiller_id INT NOT NULL,
    teaterstykke_navn TEXT NOT NULL,

    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    CONSTRAINT fk_skuespiller_id FOREIGN KEY (skuespiller_id) REFERENCES Skuespiller(id),
    
    PRIMARY KEY (navn, skuespiller_id, teaterstykke_navn),
    UNIQUE (navn, skuespiller_id, teaterstykke_navn)
 
);

CREATE TABLE RolleIAkt (
    rolle_navn TEXT NOT NULL,
    skuespiller_id INT NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    akt_nummer INT NOT NULL,
    akt_teaterstykke_navn TEXT NOT NULL,

    CONSTRAINT fk_rolle_key FOREIGN KEY (rolle_navn, skuespiller_id, teaterstykke_navn) REFERENCES Rolle(navn, skuespiller_id, teaterstykke_navn),
    CONSTRAINT fk_akt_key FOREIGN KEY (akt_nummer, akt_teaterstykke_navn) REFERENCES Akt(nummer, teaterstykke_navn),
    
    PRIMARY KEY (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn),
    UNIQUE (rolle_navn, skuespiller_id, teaterstykke_navn, akt_nummer, akt_teaterstykke_navn)
);


CREATE TABLE Bestilling (
    id INTEGER PRIMARY KEY UNIQUE NOT NULL ,
    forestilling_navn INT NOT NULL,
    forestilling_tidspunkt DATETIME NOT NULL,
    tidspunkt DATETIME NOT NULL,
    kunde_telefon TEXT NOT NULL,

    CONSTRAINT fk_forestilling_key FOREIGN KEY (forestilling_navn, forestilling_tidspunkt) REFERENCES Forestilling(tidspunkt, teaterstykke_navn),
    CONSTRAINT fk_kunde_telefon FOREIGN KEY (kunde_telefon) REFERENCES Kundeprofil(telefon)
    
);

CREATE TABLE BilletterTilBestilling (
    bestilling_id INT NOT NULL,

    forestilling_navn INT NOT NULL,
    billett_billettype TEXT NOT NULL,
    
    antall INT NOT NULL, 
    CONSTRAINT fk_forestilling_navn FOREIGN KEY (forestilling_navn) REFERENCES Forestilling(tidspunkt),
    CONSTRAINT fk_billett_billettype FOREIGN KEY (billett_billettype) REFERENCES Billett(billettype),
    CONSTRAINT fk_bestilling_id FOREIGN KEY (bestilling_id) REFERENCES Bestilling(id),

    PRIMARY KEY (bestilling_id, forestilling_navn, billett_billettype),
    UNIQUE (bestilling_id, forestilling_navn, billett_billettype)
);


CREATE TABLE SeterTilBestilling (
    
    bestilling_id INT NOT NULL,
    
    sete_nr INT NOT NULL,
    rad_nr INT NOT NULL,
    omraade_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,

    CONSTRAINT fk_sete_key
        FOREIGN KEY (sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn) 
            REFERENCES Sete(sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn),

    PRIMARY KEY (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn),
    UNIQUE (bestilling_id, sete_nr, rad_nr, omraade_navn, sal_navn, teater_navn)
);
