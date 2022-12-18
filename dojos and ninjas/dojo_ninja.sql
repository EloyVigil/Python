-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo_and_ninjas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo_and_ninjas` ;

-- -----------------------------------------------------
-- Schema dojo_and_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo_and_ninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojo_and_ninjas` ;

-- -----------------------------------------------------
-- Table `dojo_and_ninjas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_and_ninjas`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `dojo_and_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_and_ninjas`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `dojo_and_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_and_ninjas`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL,
  `age` TINYINT NULL,
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojo_and_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
