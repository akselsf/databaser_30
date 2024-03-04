CREATE TABLE Kundeprofil (
    telefon VARCHAR(55) PRIMARY KEY,
    navn VARCHAR(55),
    adresse VARCHAR(55),
)

CREATE TABLE Skuespiller(
    id INT PRIMARY KEY,
    navn VARCHAR(55),
    epost VARCHAR(55),
)

CREATE TABLE Teaterstykke(
    id INT PRIMARY KEY,
    navn VARCHAR(55) PRIMARY KEY,
)

CREATE TABLE Akt (
    nummer INT,
    navn VARCHAR(55),
    FOREIGN KEY (teaterstykke) REFERENCES Teaterstykke(id),
)

CREATE TABLE Ansatt (
    id INT PRIMARY KEY,
    navn VARCHAR(55),
    epost VARCHAR(55),
    ansattstatus VARCHAR(55),
)

CREATE TABLE Ansattil (
    FOREIGN KEY (ansatt) REFERENCES Ansatt(id),
    FOREIGN KEY (teaterstykke) REFERENCES Teaterstykke(id),
    typejobb VARCHAR(55),
)

CREATE TABLE Teater (
    id INT PRIMARY KEY,
    navn VARCHAR(55),
    adresse VARCHAR(55),
)

CREATE TABLE Sal (
    navn VARCHAR(55) PRIMARY KEY,
)

/*
- Antagelser
    - En ansatt kan jobbe på flere teaterstykker  
*/