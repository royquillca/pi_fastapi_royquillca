CREATE DATABASE  IF NOT EXISTS `pidb`;
USE `pidb`;

DROP TABLE IF EXISTS `circuits`;
CREATE TABLE IF NOT EXISTS `circuits` (
  `circuitId`		INTEGER NOT NULL,
  `circuitRef` 		VARCHAR(50),
  `name`			VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `location`		VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `country`			VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `lat`				VARCHAR(8) NOT NULL,
  `lng`				VARCHAR(9) NOT NULL,
  `alt`				VARCHAR(4) NOT NULL,
  `url`				VARCHAR(80),
  PRIMARY KEY (`circuitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT * FROM circuits;

###########
-- RACES
###########

DROP TABLE IF EXISTS `races`;
CREATE TABLE IF NOT EXISTS `races` (
  `raceId`			INT,
  `year` 			VARCHAR(4),
  `round`			VARCHAR(2),
  `circuitId`		INT,
  `name`			VARCHAR(50),
  `date`			DATE,
  `time`			VARCHAR(8),
  `url`				VARCHAR(70),
  PRIMARY KEY (`raceId`),
  FOREIGN KEY(`circuitId`) REFERENCES `circuits`(`circuitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT * FROM races;

####################
-- DRIVERS
####################

DROP TABLES IF EXISTS `drivers`;
CREATE TABLE IF NOT EXISTS `drivers` (
	`driverId`		INT,
    `driverRef`		VARCHAR(50),
    `number`		VARCHAR(10),
    `code`			VARCHAR(3),
    `name`			VARCHAR(100),
    `dob`			VARCHAR(10),
    `nationality`	VARCHAR(20),
    `url`			VARCHAR(100),
    PRIMARY KEY(`driverId`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT * FROM drivers;

#####################
-- CONSTRUCTORS
#####################

DROP TABLES IF EXISTS `constructors`;
CREATE TABLE IF NOT EXISTS `constructors` (
	`constructorId`			INT,
    `constructorRef`		VARCHAR(100),
    `name`					VARCHAR(50),
    `nationality`			VARCHAR(20),
    `url`					VARCHAR(100),
    PRIMARY KEY (`constructorId`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT * FROM constructors;

###############
-- PIT_STOPS
###############

DROP TABLES IF EXISTS `pit_stops`;
CREATE TABLE IF NOT EXISTS `pit_stops` (
	`raceId`			INT,
	`driverId`			INT,
	`stop`				VARCHAR(1),
	`lap`				VARCHAR(2),
	`time`				VARCHAR(8),
	`duration`			VARCHAR(18),
	`milliseconds`		VARCHAR(7),
    FOREIGN KEY (`raceId`) REFERENCES races(`raceId`),
	FOREIGN KEY (`driverId`) REFERENCES drivers(`driverId`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT COUNT(*) FROM pit_stops;

###############
-- RESUTLS
###############

DROP TABLES IF EXISTS `results`;
CREATE TABLE IF NOT EXISTS `results` (
	`resultId`		INT,
	`raceId`		INT,
	`driverId`		INT,
	`constructorId`	INT,
	`number`		VARCHAR(3),
	`grid`			VARCHAR(2),
	`position`		VARCHAR(2),
	`positionText`	VARCHAR(2),
	`positionOrder`	VARCHAR(2),
	`points`		VARCHAR(4),
	`laps`			VARCHAR(3),
	`time`			VARCHAR(11),
	`milliseconds`	VARCHAR(8),
	`fastestLap`	VARCHAR(2),
	`rank`			VARCHAR(2),
	`fastestLapTime`VARCHAR(8),
	`fastestLapSpeed`VARCHAR(7),
	`statusId`		VARCHAR(3),
    PRIMARY KEY(`resultId`),
    FOREIGN KEY(`raceId`) REFERENCES races(`raceId`),
    FOREIGN KEY(`driverId`) REFERENCES drivers(`driverId`),
    FOREIGN KEY(`constructorId`) REFERENCES constructors(`constructorId`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT COUNT(*) FROM results;

###############
-- QUALIFY
###############

DROP TABLES IF EXISTS `qualify`;
CREATE TABLE IF NOT EXISTS `qualify` (
	`qualifyId`			INT,
	`raceId`			INT,
	`driverId`			INT,
	`constructorId`		INT,
	`number`			VARCHAR(2),
	`position`			VARCHAR(2),
	`q1`				VARCHAR(9),
	`q2`				VARCHAR(9),
	`q3`				VARCHAR(9),
    PRIMARY KEY (`qualifyId`),
    FOREIGN KEY (`raceId`) REFERENCES races(`raceId`),
    FOREIGN KEY (`driverId`) REFERENCES drivers(`driverId`),
    FOREIGN KEY (`constructorId`) REFERENCES constructors(`constructorId`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
SELECT * FROM qualify;


