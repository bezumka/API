-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2019 at 10:54 PM
-- Server version: 5.5.25
-- PHP Version: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ub`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `user`(
    IN `NAME` varchar(15)
)
BEGIN
    SELECT
        CONCAT('[',
               GROUP_CONCAT( CONCAT( '{ "id":', u.id, ', "login":"', u.login, '", "friends":', s.friend, ' }' )  SEPARATOR ', ' ),
               ']'
            )
    FROM
        users u
            LEFT JOIN (
            SELECT
                login,
                CONCAT(
                        '[',
                        GROUP_CONCAT( CONCAT( '{ "id":', id, ', "friend":"', friend, '" }' ) SEPARATOR ', '),
                        ']'
                    ) friend
            FROM friends
            GROUP BY login ) s ON u.login = s.login and u.login = NAME;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `friends`
--

CREATE TABLE IF NOT EXISTS `friends` (
                                         `id` int(255) NOT NULL AUTO_INCREMENT,
                                         `login` varchar(15) NOT NULL,
                                         `friend` varchar(15) NOT NULL,
                                         PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `friends`
--

INSERT INTO `friends` (`id`, `login`, `friend`) VALUES
(1, 'admin', 'root'),
(2, 'admin', 'test_login1');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
                                       `id` int(255) NOT NULL AUTO_INCREMENT,
                                       `login` varchar(15) NOT NULL,
                                       `password` varchar(20) NOT NULL,
                                       `first_name` varchar(255) NOT NULL,
                                       `last_name` varchar(255) NOT NULL,
                                       PRIMARY KEY (`id`),
                                       UNIQUE KEY `id` (`id`),
                                       UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=80 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `first_name`, `last_name`) VALUES
(1, 'admin', 'admin', 'Vasya', 'Pupkin'),
(2, 'root', 'root', 'Inkognito', 'Pendosovich'),
(7, 'test_login1', 'test_pass', 'test_name', 'test_last_name'),
(71, 'TestAccount', 'testPassword', 'admin', 'admin'),
(78, 'asd23', 'testPassword', 'admin', 'admin'),
(79, 'qbKSARVd', '', '', '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
