-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2022 at 07:26 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `educationapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `classnote`
--

CREATE TABLE `classnote` (
  `No` text NOT NULL,
  `CourseID` text NOT NULL,
  `Details` text NOT NULL,
  `NoteLink` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `classnote`
--

INSERT INTO `classnote` (`No`, `CourseID`, `Details`, `NoteLink`) VALUES
('1', 'COM3000', 'JavaScript', 'https://drive.google.com/drive/folders/1zQSSKq8XJpI6kDEIhrFqqFbjVO9A3L96');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` text NOT NULL,
  `StudentID` int(10) NOT NULL,
  `StudentUserName` text NOT NULL,
  `MockScore` int(3) NOT NULL,
  `WrittenExamScore` int(3) NOT NULL,
  `AssignmentScore` int(3) NOT NULL,
  `QuizzScore` int(3) NOT NULL,
  `ProjectScore` int(3) NOT NULL,
  `PresentationScore` int(3) NOT NULL,
  `HomeWorkScore` int(3) NOT NULL,
  `ClassWorkScore` int(3) NOT NULL,
  `OverallGrade` text NOT NULL,
  `TeacherRemarks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coursestudents`
--

CREATE TABLE `coursestudents` (
  `CourseID` int(11) NOT NULL,
  `StudentID` int(11) NOT NULL,
  `StudentUserName` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `coursestudents`
--

INSERT INTO `coursestudents` (`CourseID`, `StudentID`, `StudentUserName`) VALUES
(1, 1, '0'),
(2, 2, '0'),
(3, 3, 'rohit');

-- --------------------------------------------------------

--
-- Table structure for table `createcourse`
--

CREATE TABLE `createcourse` (
  `CourseID` text NOT NULL,
  `CourseName` text NOT NULL,
  `TeacherID` text NOT NULL,
  `TeacherUserName` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `createcourse`
--

INSERT INTO `createcourse` (`CourseID`, `CourseName`, `TeacherID`, `TeacherUserName`) VALUES
('Database Management ', 'Database Management ', '111', '111'),
('Human Resource Development ', 'Human Resource Development ', '7758', 'shamim '),
('1', 'Programming', '1', 'ruksana'),
('111', 'Computer', '122', 'xyz');

-- --------------------------------------------------------

--
-- Table structure for table `deliverable`
--

CREATE TABLE `deliverable` (
  `Ref` text NOT NULL,
  `CourseID` text NOT NULL,
  `Details` text NOT NULL,
  `StudentID` text NOT NULL,
  `DeliverableLink` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `deliverable`
--

INSERT INTO `deliverable` (`Ref`, `CourseID`, `Details`, `StudentID`, `DeliverableLink`) VALUES
('1', 'COM', 'HW-1', '2022', 'hw.com');

-- --------------------------------------------------------

--
-- Table structure for table `organisationalcost`
--

CREATE TABLE `organisationalcost` (
  `Serial` int(10) NOT NULL,
  `Rent` int(10) NOT NULL,
  `Electricity Bill` int(8) NOT NULL,
  `Gas Bill` int(8) NOT NULL,
  `Water Bill` int(8) NOT NULL,
  `Wifi Bill` int(8) NOT NULL,
  `Telephone Bill` int(8) NOT NULL,
  `Marketing Bill` int(8) NOT NULL,
  `Repair Bill` int(8) NOT NULL,
  `New Purchase Bill` int(8) NOT NULL,
  `Snacks Bill` int(8) NOT NULL,
  `Event Bill` int(8) NOT NULL,
  `Miscellaneous` int(8) NOT NULL,
  `Month` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `salarytable`
--

CREATE TABLE `salarytable` (
  `EmployeeID` int(30) NOT NULL,
  `UserName` text NOT NULL,
  `January2023` int(6) NOT NULL,
  `February2023` int(6) NOT NULL,
  `March2023` int(6) NOT NULL,
  `April2023` int(6) NOT NULL,
  `May2023` int(6) NOT NULL,
  `June2023` int(6) NOT NULL,
  `July2023` int(6) NOT NULL,
  `August2023` int(6) NOT NULL,
  `September2023` int(6) NOT NULL,
  `October2023` int(6) NOT NULL,
  `November2023` int(6) NOT NULL,
  `December2023` int(6) NOT NULL,
  `Yearly Bonus 1` int(6) NOT NULL,
  `Yearly Bonus 2` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `studentaccounts`
--

CREATE TABLE `studentaccounts` (
  `StudentID` int(10) NOT NULL,
  `UserName` text NOT NULL,
  `AdmissionFee` int(10) NOT NULL,
  `CourseFee` int(10) NOT NULL,
  `ExamFee` int(10) NOT NULL,
  `Club Fee` int(10) NOT NULL,
  `Library Fee` int(10) NOT NULL,
  `Fine` int(10) NOT NULL,
  `Miscellaneous` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `studentdues`
--

CREATE TABLE `studentdues` (
  `Ref` text NOT NULL,
  `StudentUserName` text NOT NULL,
  `StudentID` int(11) NOT NULL,
  `Description` text NOT NULL,
  `Ammount` int(11) NOT NULL,
  `Deadline` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `studentdues`
--

INSERT INTO `studentdues` (`Ref`, `StudentUserName`, `StudentID`, `Description`, `Ammount`, `Deadline`) VALUES
('1', 'shpvon', 1, 'fee', 1, '1');

-- --------------------------------------------------------

--
-- Table structure for table `studentgrade`
--

CREATE TABLE `studentgrade` (
  `CourseID` int(11) NOT NULL,
  `StudentID` int(11) NOT NULL,
  `Grade` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `studentgrade`
--

INSERT INTO `studentgrade` (`CourseID`, `StudentID`, `Grade`) VALUES
(1, 1, '1'),
(1, 1, '1'),
(2, 2, 'A+');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Serial` int(50) NOT NULL,
  `Name` text NOT NULL,
  `UserName` text NOT NULL,
  `UserType` text NOT NULL,
  `Email` text NOT NULL,
  `Mobile` text NOT NULL,
  `Address` text NOT NULL,
  `Gender` text NOT NULL,
  `PassWord` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Serial`, `Name`, `UserName`, `UserType`, `Email`, `Mobile`, `Address`, `Gender`, `PassWord`) VALUES
(0, 'Superadmin', 'Superadmin', 'Superadmin', 'superadmin@education360byshovon.com ', '01785692324', 'Dhaka', 'Male', '12345');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
