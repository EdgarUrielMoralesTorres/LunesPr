-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bitpost
CREATE DATABASE IF NOT EXISTS `bitpost` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `bitpost`;

-- Volcando estructura para tabla bitpost.tareas
CREATE TABLE IF NOT EXISTS `tareas` (
  `Id` int(11) NOT NULL,
  `IdUs` int(11) DEFAULT NULL,
  `titulo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `fecha_limit` timestamp(6) NULL DEFAULT NULL,
  `estado` enum('Incompleto','Completado','Por Realizar') DEFAULT NULL,
  `clasificacion` varchar(50) DEFAULT NULL,
  `prioridad` enum('Alta','Media','Baja') DEFAULT NULL,
  `completada` timestamp(6) NULL DEFAULT NULL,
  `fecha_completada` timestamp(6) NULL DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bitpost.tareas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla bitpost.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `idUs` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `contra` varchar(255) NOT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `fecha_regis` timestamp(6) NULL DEFAULT NULL,
  `ultimo_acceso` timestamp(6) NULL DEFAULT NULL,
  `activo` bit(1) NOT NULL,
  `foto_perfil` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idUs`) USING BTREE,
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla bitpost.usuarios: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
