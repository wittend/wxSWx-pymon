-- ACCOUNT
--------------
CREATE TABLE account
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    UserID          varchar(65) NOT NULL,       -- mandatory;  (email address) ex: ab4ej@arrl.net
    Password        varchar(65) NOT NULL,       -- mandatory; may combine with token
    Callsign        varchar(65),                -- optiomnal
    Role            varchar(65)                 -- mandatory; link to UserRoles table
);

-- Nodes
------------
CREATE TABLE node 
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    NodeNumber      varchar(127) NOT NULL,      -- mandatory
    Token           varchar(65) NOT NULL,       -- mandatory
    Grid            varchar(65) NOT NULL,       -- mandatory, must be valid Maidenhead grid
    Latitude        varchar(65) NOT NULL,       -- calculated(not entered by user)
    Longitude       varchar(65) NOT NULL,       -- calculated(not entered by user)
    Elevation       varchar(65) NOT NULL,       -- mandatory; in meters above sealevel
    Antenna1        varchar(65) NOT NULL,       -- mandatory; text up to 64 char.
    Antenna2        varchar(65),                -- optional; text up to 64 char.
    GPSDO           bit(1) NOT NULL,            -- mandatory; binary (0 or 1)
    StreetAddress   varchar(75),                -- Optional; text up to 75 char.
    City            varchar(75),                -- Optional; text up to 75 char.
    State           varchar(15),                -- Optional; text up to 15 char.
    PostalCode      varchar(65),                -- Optional; must support international values
    PhoneNumber     varchar(65)                 -- Optional
);

-- Instrument
--------------
CREATE TABLE Instrument 
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    SerialNumber    varchar(30),                -- mandatory, but the word "None" allowed; text up to 30 char
    InstrumentType  varchar(65) NOT NULL,       -- mandatory; link to instrumentType table
    Version         varchar(65),                -- optional
    InstallDate     varchar(65)                 -- optional
);

-- InstrumentType
-----------------
CREATE TABLE InstrumentType
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    InstrumentType  varchar(65) NOT NULL        -- mandatory; administrator created
);

-- UserRoles
-------------
CREATE TABLE UserRoles
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    Role            varchar(65),                -- mandatory; link to UserRoles table
    LastModified    Date                        -- mandatory; Calendar Date
);

-- UserRoles
-------------
CREATE TABLE Observation
(
    ID              bigserial PRIMARY KEY,      -- mandatory; 64-bit integer; system assigned
    DataType        varchar(65),                 -- mandatory
    DataRate        bigint,                     -- mandatory; 64-bit integer
    CenterFrequency bigint,                     -- optional; 64-bit integer; in Hz
    Node            bigint,                     -- mandatory; link to Node table
    Instrument      bigint,                     -- mandatory; link to Instrument table
    Band            bigint,                     -- optional; link to Band table
    Size            bigint,                     -- optional; computed based on data size
    FileName        varchar(128),               -- mandatory; computed from data file name
    Path            varchar(128)                -- mandatory; computed from path to stored data
);


--
--                                    List of relations
-- Schema |         Name          |   Type   | Owner  | Persistence |    Size    | Description 
----------+-----------------------+----------+--------+-------------+------------+-------------
-- public | account               | table    | hamsci | permanent   | 0 bytes    | 
-- public | account_id_seq        | sequence | hamsci | permanent   | 8192 bytes | 
-- public | instrument            | table    | hamsci | permanent   | 0 bytes    | 
-- public | instrument_id_seq     | sequence | hamsci | permanent   | 8192 bytes | 
-- public | instrumenttype        | table    | hamsci | permanent   | 0 bytes    | 
-- public | instrumenttype_id_seq | sequence | hamsci | permanent   | 8192 bytes | 
-- public | node                  | table    | hamsci | permanent   | 8192 bytes | 
-- public | node_id_seq           | sequence | hamsci | permanent   | 8192 bytes | 
-- public | observation           | table    | hamsci | permanent   | 0 bytes    | 
-- public | observation_id_seq    | sequence | hamsci | permanent   | 8192 bytes | 
-- public | userroles             | table    | hamsci | permanent   | 0 bytes    | 
-- public | userroles_id_seq      | sequence | hamsci | permanent   | 8192 bytes | 
--(12 rows)
--


