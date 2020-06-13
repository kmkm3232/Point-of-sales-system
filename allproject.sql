-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2018 年 11 月 28 日 11:43
-- 伺服器版本: 10.1.31-MariaDB
-- PHP 版本： 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `allproject`
--

-- --------------------------------------------------------

--
-- 資料表結構 `invoice1`
--

CREATE TABLE `invoice1` (
  `userID` int(8) NOT NULL,
  `orderID` int(8) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `totalPrice` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `invoice1`
--

INSERT INTO `invoice1` (`userID`, `orderID`, `Date`, `Time`, `totalPrice`) VALUES
(1, 173, '2018-11-16', '23:44:21', 87),
(1, 174, '2018-11-16', '23:45:58', 935),
(1, 175, '2018-11-27', '16:06:53', 379),
(1, 176, '2018-11-27', '17:07:27', 379),
(1, 178, '2018-11-27', '17:09:19', 20),
(1, 179, '2018-11-27', '17:09:47', 379),
(1, 180, '2018-11-27', '17:10:22', 379),
(1, 181, '2018-11-27', '17:24:32', 20),
(1, 182, '2018-11-27', '17:27:14', 50),
(1, 183, '2018-11-27', '17:30:50', 1799),
(1, 184, '2018-11-27', '17:34:56', 379),
(1, 185, '2018-11-27', '17:35:28', 379),
(1, 186, '2018-11-27', '17:37:58', 379),
(1, 187, '2018-11-27', '17:38:02', 379),
(1, 188, '2018-11-27', '17:39:15', 88),
(1, 189, '2018-11-27', '17:39:17', 88),
(1, 190, '2018-11-27', '17:39:36', 379),
(1, 191, '2018-11-27', '17:40:56', 379),
(1, 192, '2018-11-27', '17:41:14', 379),
(1, 193, '2018-11-27', '17:44:01', 379),
(1, 194, '2018-11-27', '17:46:11', 379),
(1, 195, '2018-11-27', '17:46:38', 379),
(1, 196, '2018-11-27', '17:47:21', 379),
(1, 197, '2018-11-27', '17:48:02', 379),
(1, 198, '2018-11-27', '17:53:16', 0),
(1, 199, '2018-11-27', '17:57:24', 50),
(1, 200, '2018-11-27', '17:58:25', 379),
(1, 201, '2018-11-27', '17:58:31', 379),
(1, 202, '2018-11-27', '17:59:12', 379),
(1, 203, '2018-11-27', '18:00:11', 379),
(1, 204, '2018-11-27', '18:00:22', 379),
(1, 205, '2018-11-27', '18:00:45', 379),
(1, 206, '2018-11-27', '18:06:57', 20),
(1, 207, '2018-11-27', '19:01:23', 1799),
(1, 208, '2018-11-27', '19:04:30', 1799),
(1, 209, '2018-11-27', '19:36:34', 379),
(1, 210, '2018-11-27', '20:47:35', 816),
(1, 211, '2018-11-28', '17:38:07', 0),
(1, 212, '2018-11-28', '17:39:15', 0),
(123, 213, '2018-11-28', '18:42:35', 196),
(123, 214, '2018-11-28', '18:42:49', 490),
(123, 215, '2018-11-28', '18:43:05', 700);

-- --------------------------------------------------------

--
-- 資料表結構 `order1`
--

CREATE TABLE `order1` (
  `orderID` int(8) NOT NULL,
  `productID` int(6) DEFAULT NULL,
  `quantity` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `order1`
--

INSERT INTO `order1` (`orderID`, `productID`, `quantity`) VALUES
(186, 1, 1),
(187, 1, 1),
(188, 2, 1),
(189, 2, 1),
(190, 1, 1),
(191, 1, 1),
(192, 1, 1),
(193, 1, 1),
(194, 1, 1),
(195, 1, 1),
(196, 1, 1),
(197, 1, 1),
(199, 7, 1),
(200, 1, 1),
(201, 1, 1),
(202, 1, 1),
(203, 1, 1),
(204, 1, 1),
(205, 1, 1),
(206, 5, 1),
(207, 4, 1),
(208, 4, 1),
(209, 1, 1),
(210, 1, 1),
(210, 2, 2),
(210, 6, 3),
(213, 5, 1),
(213, 6, 1),
(213, 10, 1),
(214, 2, 2),
(214, 9, 1),
(214, 13, 2),
(215, 5, 10),
(215, 7, 10);

-- --------------------------------------------------------

--
-- 資料表結構 `product`
--

CREATE TABLE `product` (
  `productID` int(6) NOT NULL,
  `productType` varchar(10) NOT NULL,
  `productName` varchar(20) DEFAULT NULL,
  `productPrice` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `product`
--

INSERT INTO `product` (`productID`, `productType`, `productName`, `productPrice`) VALUES
(1, 'Cow', 'Ribeye steak', 379),
(2, 'Cow', 'Oxtail', 88),
(3, 'Cow', 'Cow\'s trotters', 324),
(4, 'Cow', 'Level A5 sliced beef', 1799),
(5, 'Cow', 'Butter', 20),
(6, 'Chicken', 'Chicken breast', 87),
(7, 'Chicken', 'Chicken wings', 50),
(8, 'Chicken', 'Chicken thigh', 56),
(9, 'Chicken', 'Drumstick ', 14),
(10, 'Pig', 'Pork Feet', 89),
(11, 'Pig', 'Pork shoulder butt', 67),
(12, 'Pig', 'Pork neck', 45),
(13, 'Pig', 'Spare Ribs', 150);

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `userID` int(8) NOT NULL,
  `Password` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `user`
--

INSERT INTO `user` (`userID`, `Password`) VALUES
(1, 123456),
(123, 123456),
(791, 1),
(792, 123),
(793, 123),
(794, 123);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `invoice1`
--
ALTER TABLE `invoice1`
  ADD PRIMARY KEY (`orderID`),
  ADD KEY `userID` (`userID`);

--
-- 資料表索引 `order1`
--
ALTER TABLE `order1`
  ADD KEY `orderID` (`orderID`),
  ADD KEY `productID` (`productID`);

--
-- 資料表索引 `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`productID`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `invoice1`
--
ALTER TABLE `invoice1`
  MODIFY `orderID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=216;

--
-- 使用資料表 AUTO_INCREMENT `product`
--
ALTER TABLE `product`
  MODIFY `productID` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用資料表 AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `userID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=795;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
