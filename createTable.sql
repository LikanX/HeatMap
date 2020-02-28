CREATE TABLE Kef_main (
    Timestamp           timestamp,
    Site                varchar(255),
    Workstation_name    varchar(255),
    Terminal            varchar(255),
    Checkpoint          varchar(255),
    Scanning_position   varchar(255),
    Flight_number       int,
    Airline             varchar(255),
    Destination         varchar(255),
    TravelDate          timestamp,
    STD                 time,
    Boardingpasshash    varchar(255),
    Gate                varchar(255)
);

CREATE TABLE Scanner_pos (
    Scanning_position   varchar(255),
    x_coord     int,
    y_coord     int
);