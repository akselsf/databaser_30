CREATE TABLE Teater (
    id INT PRIMARY KEY NOT NULL UNIQUE,
    navn TEXT NOT NULL,
    direktoer_id INT NOT NULL
);

CREATE TABLE Teaterstykke(
    navn TEXT PRIMARY KEY UNIQUE NOT NULL,
    teater_id INT NOT NULL,
  CONSTRAINT fk_teater_id  FOREIGN KEY (teater_id) REFERENCES Teater(id)
);

CREATE TABLE Akt (
    nummer INT NOT NULL,
    navn TEXT,
    teaterstykke_navn TEXT NOT NULL,
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    
    PRIMARY KEY (nummer, teaterstykke_navn)
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
    CONSTRAINT fk_ansatt_id FOREIGN KEY (ansatt_id) REFERENCES Ansatt(id),
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    PRIMARY KEY (ansatt_id, teaterstykke_navn)

);

CREATE TABLE Sal (

    navn TEXT NOT NULL,
    antallseter INT NOT NULL, 
    teater_navn TEXT NOT NULL,
    CONSTRAINT fk_teater_navn FOREIGN KEY (teater_navn) REFERENCES Teater(navn),

    PRIMARY KEY (navn, teater_navn)
);

CREATE TABLE Omraade (
    navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,
   CONSTRAINT fk_sal_navn  FOREIGN KEY (sal_navn) REFERENCES Sal(navn),
    CONSTRAINT fk_teater_navn FOREIGN KEY (teater_navn) REFERENCES Teater(navn),

    PRIMARY KEY (navn, sal_navn, teater_navn)


);

CREATE TABLE Sete (

    setenr INT NOT NULL, 
    radnr INT NOT NULL, 
    omraade_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,

   CONSTRAINT fk_omraade_navn FOREIGN KEY (omraade_navn) REFERENCES Omraade(navn),
    CONSTRAINT fk_sal_navn FOREIGN KEY (sal_navn) REFERENCES Sal(navn),
    CONSTRAINT fk_teater_navn FOREIGN KEY (teater_navn) REFERENCES Teater(navn),


    PRIMARY KEY (setenr, radnr, omraade_navn, sal_navn, teater_navn) 

);

CREATE TABLE Forestilling (
    tidspunkt DATETIME NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
   CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
   CONSTRAINT fk_sal_navn FOREIGN KEY (sal_navn) REFERENCES Sal(navn),

    PRIMARY KEY (tidspunkt, teaterstykke_navn)

);

CREATE TABLE Billett (
    pris INT NOT NULL,
    billettype TEXT NOT NULL,
    teaterstykke_navn TEXT NOT NULL,
    CONSTRAINT fk_teaterstykke_navn FOREIGN KEY (teaterstykke_navn) REFERENCES Teaterstykke(navn),
    
    PRIMARY KEY (billettype, teaterstykke_navn)
);

CREATE TABLE Rolle (
    navn TEXT NOT NULL,
    skuespiller_id INT NOT NULL,
    akt_id INT NOT NULL,
    CONSTRAINT fk_skuespiller_id FOREIGN KEY (skuespiller_id) REFERENCES Skuespiller(id),
    CONSTRAINT fk_akt_id FOREIGN KEY (akt_id) REFERENCES Akt(id),
    
    PRIMARY KEY (navn, skuespiller_id, akt_id),
 
);


CREATE TABLE Bestilling (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    forestilling_id INT NOT NULL,
    tidspunkt DATETIME NOT NULL,
    kunde_telefon TEXT NOT NULL,
  
    CONSTRAINT fk_forestilling_id FOREIGN KEY (forestilling_id) REFERENCES Forestilling(id),
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

    PRIMARY KEY (bestilling_id, forestilling_navn, billett_billettype)
);


CREATE TABLE SeterTilBestilling (
    
    bestilling_id INT NOT NULL,
    
    setenr INT NOT NULL,
    radnr INT NOT NULL,
    omraade_navn TEXT NOT NULL,
    sal_navn TEXT NOT NULL,
    teater_navn TEXT NOT NULL,

    CONSTRAINT fk_sete_key
        FOREIGN KEY (setenr, radnr, omraade_navn, sal_navn, teater_navn) 
            REFERENCES Sete(setenr, radnr, omraade_navn, sal_navn, teater_navn),

    PRIMARY KEY (bestilling_id, setenr, radnr, omraade_navn, sal_navn, teater_navn) 
);
