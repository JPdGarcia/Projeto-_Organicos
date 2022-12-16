-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: receita
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendas` (
  `Cod_Prd` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Nome_Prd` varchar(20) DEFAULT NULL,
  `Vlr_Unit_Prd` float DEFAULT NULL,
  `Unidade_Prd` varchar(15) DEFAULT NULL,
  `Dt_Venda_Prd` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES ('1','Abóbora',3.99,'Kg','2022-12-01'),('2','Abricó',4.79,'Dúzia','2022-12-01'),('3','Aipim',4.89,'Kg','2022-12-01'),('4','Banana',7.9,'Dúzia','2022-12-01'),('5','Batata',4.93,'Kg','2022-12-01'),('6','Berinjela',3.79,'Kg','2022-12-01'),('7','Beterraba',5.55,'Kg','2022-12-01'),('8','Caqui',11.59,'Kg','2022-12-01'),('9','Cenoura',4.45,'Kg','2022-12-01'),('10','Chuchu',4.57,'Kg','2022-12-01'),('11','Coca Cola Zero ',8.49,'2 Litros','2022-12-01'),('12','Coco',8.69,'Unidade','2022-12-01'),('13','Leite',6.15,'Caixa 1 Litro','2022-12-01'),('14','Mamão Papaya',6.79,'Unidade','2022-12-01'),('15','Manga',4,'Unidade','2022-12-01'),('16','Milho',2.89,'Lata','2022-12-01'),('17','Ovos',6.53,'Dúzia','2022-12-01'),('18','Suco de Uva Natural',12.98,'Caixa 1 Litro','2022-12-01'),('19','Pão Francês',19.59,'Kg','2022-12-01'),('20','Alho',49.9,'Kg','2022-12-01'),('1','Abóbora',3.99,'Kg','2022-12-01'),('1','Abóbora',3.99,'Kg','2022-12-01'),('1','Abóbora',3.99,'Kg','2022-12-01'),('11','Coca Cola Zero ',8.49,'2 Litros','2022-12-01'),('11','Coca Cola Zero ',8.49,'2 Litros','2022-12-01'),('11','Coca Cola Zero ',8.49,'2 Litros','2022-12-01'),('11','Coca Cola Zero ',8.49,'2 Litros','2022-12-01'),('18','Suco de Uva Natural',12.98,'Caixa 1 Litro','2022-12-01'),('18','Suco de Uva Natural',12.98,'Caixa 1 Litro','2022-12-01'),('8','Caqui',11.59,'Kg','2022-12-01');
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-14 17:39:49
