-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema world
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema world
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `world` DEFAULT CHARACTER SET latin1 ;
USE `world` ;

-- -----------------------------------------------------
-- Table `world`.`countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`countries` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `code` CHAR(3) NOT NULL DEFAULT '',
  `name` CHAR(52) NOT NULL DEFAULT '',
  `continent` ENUM('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America') NOT NULL DEFAULT 'Asia',
  `region` CHAR(26) NOT NULL DEFAULT '',
  `surface_area` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `indep_year` SMALLINT(6) NULL DEFAULT NULL,
  `population` INT(11) NOT NULL DEFAULT '0',
  `life_expectancy` FLOAT(3,1) NULL DEFAULT NULL,
  `gnp` FLOAT(10,2) NULL DEFAULT NULL,
  `gnp_old` FLOAT(10,2) NULL DEFAULT NULL,
  `local_name` CHAR(45) NOT NULL DEFAULT '',
  `government_form` CHAR(45) NOT NULL DEFAULT '',
  `head_of_state` CHAR(60) NULL DEFAULT NULL,
  `capital` INT(11) NULL DEFAULT NULL,
  `code2` CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 240
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `world`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`cities` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` CHAR(35) NOT NULL DEFAULT '',
  `country_code` CHAR(3) NOT NULL DEFAULT '',
  `district` CHAR(20) NOT NULL DEFAULT '',
  `population` INT(11) NOT NULL DEFAULT '0',
  `country_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cities_countries1_idx` (`country_id` ASC) VISIBLE,
  CONSTRAINT `fk_cities_countries1`
    FOREIGN KEY (`country_id`)
    REFERENCES `world`.`countries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4080
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `world`.`languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`languages` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `country_code` CHAR(3) NOT NULL DEFAULT '',
  `language` CHAR(30) NOT NULL DEFAULT '',
  `is_official` ENUM('T', 'F') NOT NULL DEFAULT 'F',
  `percentage` FLOAT(4,1) NOT NULL DEFAULT '0.0',
  `country_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_languages_countries_idx` (`country_id` ASC) VISIBLE,
  CONSTRAINT `fk_languages_countries`
    FOREIGN KEY (`country_id`)
    REFERENCES `world`.`countries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 985
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
