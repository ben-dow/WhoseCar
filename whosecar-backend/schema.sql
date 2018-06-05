-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Carpools'
--
-- ---

DROP TABLE IF EXISTS `Carpools`;

CREATE TABLE `Carpools` (
  `id` VARCHAR(8) NOT NULL DEFAULT 'NULL',
  `Title` MEDIUMTEXT NULL DEFAULT NULL,
  `DateCreated` TIMESTAMP NOT NULL DEFAULT 'NULL',
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Cars'
--
-- ---

DROP TABLE IF EXISTS `Cars`;

CREATE TABLE `Cars` (
  `id` INTEGER NOT NULL DEFAULT NULL,
  `id_Carpools` VARCHAR(8) NOT NULL DEFAULT 'NULL',
  `NumberPassengers` INTEGER NULL DEFAULT NULL,
  `CarOwner` INTEGER NULL DEFAULT NULL,
  `DateCreated` TIMESTAMP NULL DEFAULT NULL,
  `CarpoolID` VARCHAR(8) NOT NULL DEFAULT 'NULL',
  `CarOwnerID` INTEGER NULL  DEFAULT NULL,


  PRIMARY KEY (`id`)
  FOREIGN KEY (CarpoolID) REFERENCES Carpools(id)
  FOREIGN KEY (CarOwnerID) REFERENCES CarOwners(id)
);


-- ---
-- Table 'Passengers'
--
-- ---

DROP TABLE IF EXISTS `Passengers`;

CREATE TABLE `Passengers` (
  `id` INTEGER NULL DEFAULT NULL,
  `Car` INTEGER NULL DEFAULT NULL,
  `Passenger` INTEGER NULL DEFAULT NULL,
  `TimeSelected` TIMESTAMP NULL DEFAULT NULL,
  `CarID` INTEGER NOT NULL DEFAULT NULL,
  `PassengerID` INTEGER NULL  DEFAULT NULL,

  PRIMARY KEY (`id`)

  FOREIGN KEY (CarID) REFERENCES Cars(id)
  FOREIGN KEY (PassengerID) REFERENCES CarPassengers(id)

);




-- ---
-- Table 'CarOwners'
--
-- ---

DROP TABLE IF EXISTS `CarOwners`;

CREATE TABLE `CarOwners` (
  `id` INTEGER NULL  DEFAULT NULL,
  `Name` MEDIUMTEXT NULL DEFAULT NULL,
  `Password` VARCHAR NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'CarPassengers'
--
-- ---

DROP TABLE IF EXISTS `CarPassengers`;

CREATE TABLE `CarPassengers` (
  `id` INTEGER NULL  DEFAULT NULL,
  `Name` MEDIUMTEXT NULL DEFAULT NULL,
  `Password` VARCHAR NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Foreign Keys
-- ---



-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Carpools` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Cars` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Passengers` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `CarOwners` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `CarPassengers` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Carpools` (`id`,`Title`,`DateCreated`) VALUES
-- ('','','');
-- INSERT INTO `Cars` (`id`,`id_Carpools`,`NumberPassengers`,`CarOwner`,`DateCreated`) VALUES
-- ('','','','','');
-- INSERT INTO `Passengers` (`id`,`Car`,`Passenger`,`TimeSelected`) VALUES
-- ('','','','');
-- INSERT INTO `CarOwners` (`id`,`Name`,`Password`) VALUES
-- ('','','');
-- INSERT INTO `CarPassengers` (`id`,`Name`,`Password`) VALUES
-- ('','','');