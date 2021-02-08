-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2020 at 09:17 AM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `petspotter`
--

-- --------------------------------------------------------

--
-- Table structure for table `app1_add_food`
--

CREATE TABLE `app1_add_food` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `fid_id` int(11) NOT NULL,
  `availableqty` varchar(100) NOT NULL,
  `rating` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_add_food`
--

INSERT INTO `app1_add_food` (`id`, `name`, `Category`, `quantity`, `Description`, `Price`, `status`, `Image`, `fid_id`, `availableqty`, `rating`) VALUES
(1, 'Dry food', 'fish', '200mg', 'JShAJVCJAVC', '220', 'available', 'food/bl2.jpg', 2, '5', 0),
(2, 'dog biscuts', 'dog', '500mg', ' KJBKBKBK', '100', 'available', 'food/bl1.jpg', 2, '2', 0),
(3, 'Cat food', 'cat', '300mg', 'HGGJjgjg', '220', 'available', 'food/product-11_wCD87Y8_QRulSNV.jpg', 7, '166', 4),
(4, 'dogg born', 'dog', '500mg', 'vdfvdvdvdvdfvd', '500', 'available', 'food/product-7_mClmtkn.jpg', 7, '10', 0);

-- --------------------------------------------------------

--
-- Table structure for table `app1_add_pets`
--

CREATE TABLE `app1_add_pets` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `Breed` varchar(100) NOT NULL,
  `Age` varchar(100) NOT NULL,
  `Colour` varchar(100) NOT NULL,
  `size` int(11) NOT NULL,
  `Vaccination` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `pid_id` int(11) NOT NULL,
  `availableqty` varchar(100) NOT NULL,
  `rating` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_add_pets`
--

INSERT INTO `app1_add_pets` (`id`, `name`, `Category`, `Breed`, `Age`, `Colour`, `size`, `Vaccination`, `Description`, `Price`, `status`, `Image`, `type`, `pid_id`, `availableqty`, `rating`) VALUES
(1, 'JIPO', 'dog', 'Female', '1', 'White', 1, 'wwcwcwccw', 'dexddxdd', '10000', 'available', 'pets/02_1_Q4BHrNI.jpg', 'shop', 2, '10', 0),
(2, 'Tiger fish', 'fish', 'Female', '2', 'Multi color', 1, 'sssss', 'sssss', '500', 'available', 'pets/product-3.jpg', 'shop', 2, '10', 0),
(3, 'German', 'cat', 'Female', '2', 'White grey', 1, 'ssssss', 'sssssss', '5000', 'available', 'pets/3.jpg', 'shop', 2, '10', 0),
(4, 'Indian', 'cat', 'Male', '1', 'White Gold', 1, '1sxsxsx', 'ssws', '500', 'available', 'pets/2_lMAJRt0_OL6Sq3r_ygfXwCu.jpg', 'shop', 3, '10', 0),
(5, 'Crane', 'bird', 'Female', '1', 'Orange', 2, 'axdadxnmdx anx  axnb', 'axa xamnx amnxam m ', '5000', 'available', 'pets/port-3.jpg', 'shop', 3, '10', 0),
(6, 'Parrot', 'bird', 'Male', '5', 'Blue mixed', 4, 'cs c c cscsnc cn', 'ncksjcnkscsc scnsbcbc scsc', '50000', 'available', 'pets/parrot.jpg', 'shop', 3, '10', 0),
(7, 'Thin Cute', 'dog', 'Female', '2', 'White Gold', 1, 'wsxss', 'axaxax', '5000', 'available', 'pets/03_T83zppd.jpg', 'admin', 7, '70', 0),
(10, 'Crane', 'bird', 'Female', '1', 'White', 2, 'ssqsqsqs dwdwd dedd', 'dwdeecece\r\ncececcecece', '5000', 'available', 'pets/port-7_aiObxtX.jpg', 'admin', 1, '10', 0),
(11, 'Crane', 'bird', 'Female', '1', 'White grey', 2, 'ssqsqsqs dwdwd dedd', 'dwdeecece\r\ncececcecece', '5000', 'available', 'pets/port-7_HoPIkLp.jpg', 'admin', 1, '2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `app1_cart_tb`
--

CREATE TABLE `app1_cart_tb` (
  `id` int(11) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `shipping` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `unitprice` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `item` varchar(100) NOT NULL,
  `shopid` int(11) NOT NULL,
  `shoppay` varchar(100) NOT NULL,
  `fid_id` int(11) DEFAULT NULL,
  `pid_id` int(11) DEFAULT NULL,
  `userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_cart_tb`
--

INSERT INTO `app1_cart_tb` (`id`, `quantity`, `shipping`, `total`, `unitprice`, `date`, `status`, `item`, `shopid`, `shoppay`, `fid_id`, `pid_id`, `userid_id`) VALUES
(1, '1', '500', '5500', '5000', '2020-01-09 19:18:23.373793', 'Paid', 'pet', 2, 'pending', NULL, 3, 7),
(2, '2', '22', '462', '220', '2020-01-09 19:18:23.373793', 'Delivered', 'food', 7, 'Paid', 3, NULL, 7),
(40, '1', '500', '5500', '5000', '2020-01-21 16:25:20.313143', 'Paid', 'pet', 7, 'pending', NULL, 7, 7),
(42, '2', '500', '10500', '5000', '2020-01-21 16:25:20.313143', 'Paid', 'pet', 7, 'pending', NULL, 7, 7);

-- --------------------------------------------------------

--
-- Table structure for table `app1_paymenttoshop_tb`
--

CREATE TABLE `app1_paymenttoshop_tb` (
  `id` int(11) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `cartid_id` int(11) NOT NULL,
  `shopid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_paymenttoshop_tb`
--

INSERT INTO `app1_paymenttoshop_tb` (`id`, `amount`, `date`, `cartid_id`, `shopid_id`) VALUES
(1, '220', '2020-01-09 19:25:15.111000', 2, 7);

-- --------------------------------------------------------

--
-- Table structure for table `app1_payment_tb`
--

CREATE TABLE `app1_payment_tb` (
  `id` int(11) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_payment_tb`
--

INSERT INTO `app1_payment_tb` (`id`, `amount`, `status`, `date`, `userid_id`) VALUES
(1, '5962', 'Paid', '2020-01-09 19:18:23.373793', 7),
(2, '16000', 'Paid', '2020-01-21 16:25:20.313143', 7),
(3, '16000', 'Paid', '2020-01-21 16:27:23.509915', 7),
(4, '16000', 'Paid', '2020-01-21 16:28:10.091004', 7);

-- --------------------------------------------------------

--
-- Table structure for table `app1_register`
--

CREATE TABLE `app1_register` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(32) NOT NULL,
  `phone` varchar(32) NOT NULL,
  `address` varchar(100) NOT NULL,
  `status1` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_register`
--

INSERT INTO `app1_register` (`id`, `name`, `email`, `password`, `phone`, `address`, `status1`, `type`, `Image`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin', '6789087654', 'Kannur 670007', 'admin', 'admin', ''),
(2, 'Neenus pets', 'neenu@gmail.com', '1234', '3333666688', 'Chirakkal kannur kerala ', 'approved', 'shop', 'image/petshop1.jpg'),
(3, 'Aquarium', 'aq@gmail.com', '1234', '6780984587', 'Caltex Kannur', 'approved', 'shop', 'image/petshop2.jpg'),
(7, 'riya', 'riya@gmail.com', '1234', '56647854uee', 'Royals Villa', 'active', 'user', ''),
(8, 'Roy', 'roy@gmail.com', '1234', '5643789999', 'roy roy roy', 'rejected', 'user', ''),
(9, 'MYPets', 'mypet@gmail.com', '1234', '6789333332', 'mypets kozhikkode', 'rejected', 'shop', 'image/petshop3jpg'),
(10, 'PetsWorld', 'petsworld@gmail.com', '1234', '9897878676', 'Kannur Kerala', 'approved', 'shop', 'image/download.jpg'),
(13, 'Vivek KK', 'vivi@gmail.com', 'asdf', '6789333332', 'Aadithya nivas', 'approved', 'vetenery', 'image/beanie-2591388_1920-360x244_pzlmWf4.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `app1_review_tb`
--

CREATE TABLE `app1_review_tb` (
  `id` int(11) NOT NULL,
  `item` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `fid_id` int(11) DEFAULT NULL,
  `pid_id` int(11) DEFAULT NULL,
  `userid_id` int(11) NOT NULL,
  `cartid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_review_tb`
--

INSERT INTO `app1_review_tb` (`id`, `item`, `rating`, `fid_id`, `pid_id`, `userid_id`, `cartid_id`) VALUES
(17, 'food', '4', 3, NULL, 7, 2);

-- --------------------------------------------------------

--
-- Table structure for table `app1_vetenery_tb`
--

CREATE TABLE `app1_vetenery_tb` (
  `id` int(11) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `regid_id` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `days` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `clinic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app1_vetenery_tb`
--

INSERT INTO `app1_vetenery_tb` (`id`, `qualification`, `experience`, `regid_id`, `status`, `days`, `time`, `clinic`) VALUES
(1, 'MVsc', '1', 13, 'approved', 'Monday, Tuesday, Friday', '10 am to 5 pm', 'Kannur');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add add_food', 1, 'add_add_food'),
(2, 'Can change add_food', 1, 'change_add_food'),
(3, 'Can delete add_food', 1, 'delete_add_food'),
(4, 'Can view add_food', 1, 'view_add_food'),
(5, 'Can add add_pets', 2, 'add_add_pets'),
(6, 'Can change add_pets', 2, 'change_add_pets'),
(7, 'Can delete add_pets', 2, 'delete_add_pets'),
(8, 'Can view add_pets', 2, 'view_add_pets'),
(9, 'Can add cart_tb', 3, 'add_cart_tb'),
(10, 'Can change cart_tb', 3, 'change_cart_tb'),
(11, 'Can delete cart_tb', 3, 'delete_cart_tb'),
(12, 'Can view cart_tb', 3, 'view_cart_tb'),
(13, 'Can add register', 4, 'add_register'),
(14, 'Can change register', 4, 'change_register'),
(15, 'Can delete register', 4, 'delete_register'),
(16, 'Can view register', 4, 'view_register'),
(17, 'Can add user_order_pets', 5, 'add_user_order_pets'),
(18, 'Can change user_order_pets', 5, 'change_user_order_pets'),
(19, 'Can delete user_order_pets', 5, 'delete_user_order_pets'),
(20, 'Can view user_order_pets', 5, 'view_user_order_pets'),
(21, 'Can add user_order_food', 6, 'add_user_order_food'),
(22, 'Can change user_order_food', 6, 'change_user_order_food'),
(23, 'Can delete user_order_food', 6, 'delete_user_order_food'),
(24, 'Can view user_order_food', 6, 'view_user_order_food'),
(25, 'Can add paymenttoshop', 7, 'add_paymenttoshop'),
(26, 'Can change paymenttoshop', 7, 'change_paymenttoshop'),
(27, 'Can delete paymenttoshop', 7, 'delete_paymenttoshop'),
(28, 'Can view paymenttoshop', 7, 'view_paymenttoshop'),
(29, 'Can add payment_tb', 8, 'add_payment_tb'),
(30, 'Can change payment_tb', 8, 'change_payment_tb'),
(31, 'Can delete payment_tb', 8, 'delete_payment_tb'),
(32, 'Can view payment_tb', 8, 'view_payment_tb'),
(33, 'Can add add_shop', 9, 'add_add_shop'),
(34, 'Can change add_shop', 9, 'change_add_shop'),
(35, 'Can delete add_shop', 9, 'delete_add_shop'),
(36, 'Can view add_shop', 9, 'view_add_shop'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session'),
(61, 'Can add paymenttoshop_tb', 7, 'add_paymenttoshop_tb'),
(62, 'Can change paymenttoshop_tb', 7, 'change_paymenttoshop_tb'),
(63, 'Can delete paymenttoshop_tb', 7, 'delete_paymenttoshop_tb'),
(64, 'Can view paymenttoshop_tb', 7, 'view_paymenttoshop_tb'),
(65, 'Can add review_tb', 16, 'add_review_tb'),
(66, 'Can change review_tb', 16, 'change_review_tb'),
(67, 'Can delete review_tb', 16, 'delete_review_tb'),
(68, 'Can view review_tb', 16, 'view_review_tb'),
(69, 'Can add vetenery_tb', 17, 'add_vetenery_tb'),
(70, 'Can change vetenery_tb', 17, 'change_vetenery_tb'),
(71, 'Can delete vetenery_tb', 17, 'delete_vetenery_tb'),
(72, 'Can view vetenery_tb', 17, 'view_vetenery_tb');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'admin', 'logentry'),
(1, 'app1', 'add_food'),
(2, 'app1', 'add_pets'),
(9, 'app1', 'add_shop'),
(3, 'app1', 'cart_tb'),
(7, 'app1', 'paymenttoshop_tb'),
(8, 'app1', 'payment_tb'),
(4, 'app1', 'register'),
(16, 'app1', 'review_tb'),
(6, 'app1', 'user_order_food'),
(5, 'app1', 'user_order_pets'),
(17, 'app1', 'vetenery_tb'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(14, 'contenttypes', 'contenttype'),
(15, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-01-09 12:46:34.219397'),
(2, 'auth', '0001_initial', '2020-01-09 12:46:41.457059'),
(3, 'admin', '0001_initial', '2020-01-09 12:46:51.784931'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-01-09 12:46:53.556750'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-01-09 12:46:53.668755'),
(6, 'app1', '0001_initial', '2020-01-09 12:46:58.533708'),
(7, 'contenttypes', '0002_remove_content_type_name', '2020-01-09 12:47:14.014578'),
(8, 'auth', '0002_alter_permission_name_max_length', '2020-01-09 12:47:14.146593'),
(9, 'auth', '0003_alter_user_email_max_length', '2020-01-09 12:47:14.279917'),
(10, 'auth', '0004_alter_user_username_opts', '2020-01-09 12:47:14.371499'),
(11, 'auth', '0005_alter_user_last_login_null', '2020-01-09 12:47:16.089430'),
(12, 'auth', '0006_require_contenttypes_0002', '2020-01-09 12:47:16.136027'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2020-01-09 12:47:16.200294'),
(14, 'auth', '0008_alter_user_username_max_length', '2020-01-09 12:47:16.309838'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2020-01-09 12:47:16.421630'),
(16, 'auth', '0010_alter_group_name_max_length', '2020-01-09 12:47:16.599274'),
(17, 'auth', '0011_update_proxy_permissions', '2020-01-09 12:47:16.685100'),
(18, 'sessions', '0001_initial', '2020-01-09 12:47:17.775638'),
(19, 'app1', '0002_auto_20200109_1820', '2020-01-09 12:50:24.667469'),
(20, 'app1', '0003_auto_20200109_1821', '2020-01-09 12:51:23.013070'),
(21, 'app1', '0004_auto_20200109_1822', '2020-01-09 12:52:38.002716'),
(22, 'app1', '0005_auto_20200109_1931', '2020-01-09 14:01:43.818584'),
(23, 'app1', '0006_auto_20200120_1011', '2020-01-20 04:41:17.074950'),
(24, 'app1', '0007_auto_20200120_1051', '2020-01-20 05:21:41.128280'),
(25, 'app1', '0008_remove_add_pets_availableqty', '2020-01-20 07:46:48.881029'),
(26, 'app1', '0009_add_pets_availableqty', '2020-01-20 07:47:22.497832'),
(27, 'app1', '0010_auto_20200121_1057', '2020-01-21 05:27:29.025196'),
(28, 'app1', '0011_auto_20200121_1926', '2020-01-21 13:56:59.288588'),
(29, 'app1', '0012_review_tb_cartid', '2020-01-21 14:00:06.813312'),
(30, 'app1', '0013_auto_20200122_0516', '2020-01-21 23:47:01.969702'),
(31, 'app1', '0014_auto_20200122_0517', '2020-01-21 23:47:55.082805'),
(32, 'app1', '0015_auto_20200122_0618', '2020-01-22 00:48:20.477461'),
(33, 'app1', '0016_auto_20200122_0618', '2020-01-22 00:48:35.335206'),
(34, 'app1', '0017_auto_20200210_1005', '2020-02-10 04:35:35.458771'),
(35, 'app1', '0018_vetenery_tb_status', '2020-02-10 06:48:33.182951'),
(36, 'app1', '0019_auto_20200213_0405', '2020-02-12 22:36:01.583654'),
(37, 'app1', '0020_vetenery_tb_clinic', '2020-02-12 23:14:27.859962');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ewuoqqkbvix3vmp7nkeszj9qt047b3ey', 'NTk3YjA0Y2MwNTgxZmUxMzdlMjEwZmY2ZWI2YzE3OTJmN2M2YTA0MTp7Im15aWQiOjF9', '2020-02-27 08:12:30.946286'),
('ola9c7iwudbpxivk24d7pq1c8gya58sf', 'YmI5ODkxOWNjNmIxZmIyNTA4MTQ4ODI5ODllYWJkMTUxNjRhMWY1ZTp7Im15aWQiOjh9', '2020-02-08 08:32:21.770910'),
('quilmyfbc8dlo60jtg5nvqng8mb8iwen', 'NjgyZTU4MDViOWJkYTczOTg0ZDI1NmU5NWVjZjM0ZGQ3NjMwOWY4ODp7Im15aWQiOjd9', '2020-02-05 01:44:38.765142'),
('swb8c71f30levcwmckmgl9nsds00kklf', 'NjgyZTU4MDViOWJkYTczOTg0ZDI1NmU5NWVjZjM0ZGQ3NjMwOWY4ODp7Im15aWQiOjd9', '2020-01-23 13:47:22.405201'),
('xo4kma8hll2apzyltxsokuary9avmjyu', 'NjgyZTU4MDViOWJkYTczOTg0ZDI1NmU5NWVjZjM0ZGQ3NjMwOWY4ODp7Im15aWQiOjd9', '2020-02-05 02:05:29.067399');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app1_add_food`
--
ALTER TABLE `app1_add_food`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_add_food_fid_id_01e1c40d_fk_app1_register_id` (`fid_id`);

--
-- Indexes for table `app1_add_pets`
--
ALTER TABLE `app1_add_pets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_add_pets_pid_id_79492031_fk_app1_register_id` (`pid_id`);

--
-- Indexes for table `app1_cart_tb`
--
ALTER TABLE `app1_cart_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_cart_tb_userid_id_8cee2ced_fk_app1_register_id` (`userid_id`),
  ADD KEY `app1_cart_tb_pid_id_551bda73_fk_app1_add_pets_id` (`pid_id`),
  ADD KEY `app1_cart_tb_fid_id_4c575ce8_fk_app1_add_food_id` (`fid_id`);

--
-- Indexes for table `app1_paymenttoshop_tb`
--
ALTER TABLE `app1_paymenttoshop_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_paymenttoshop_cartid_id_5cc42b57_fk_app1_cart_tb_id` (`cartid_id`),
  ADD KEY `app1_paymenttoshop_shopid_id_9d8466f4_fk_app1_register_id` (`shopid_id`);

--
-- Indexes for table `app1_payment_tb`
--
ALTER TABLE `app1_payment_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_payment_tb_userid_id_c6f91ff9_fk_app1_register_id` (`userid_id`);

--
-- Indexes for table `app1_register`
--
ALTER TABLE `app1_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app1_review_tb`
--
ALTER TABLE `app1_review_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_review_tb_fid_id_376a3ebd_fk_app1_add_food_id` (`fid_id`),
  ADD KEY `app1_review_tb_pid_id_c609b0e8_fk_app1_add_pets_id` (`pid_id`),
  ADD KEY `app1_review_tb_userid_id_64568ef6_fk_app1_register_id` (`userid_id`),
  ADD KEY `app1_review_tb_cartid_id_86da8d7d_fk_app1_cart_tb_id` (`cartid_id`);

--
-- Indexes for table `app1_vetenery_tb`
--
ALTER TABLE `app1_vetenery_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_vetenery_tb_regid_id_12ee86a0_fk_app1_register_id` (`regid_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app1_add_food`
--
ALTER TABLE `app1_add_food`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `app1_add_pets`
--
ALTER TABLE `app1_add_pets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `app1_cart_tb`
--
ALTER TABLE `app1_cart_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `app1_paymenttoshop_tb`
--
ALTER TABLE `app1_paymenttoshop_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app1_payment_tb`
--
ALTER TABLE `app1_payment_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `app1_register`
--
ALTER TABLE `app1_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `app1_review_tb`
--
ALTER TABLE `app1_review_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `app1_vetenery_tb`
--
ALTER TABLE `app1_vetenery_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app1_add_food`
--
ALTER TABLE `app1_add_food`
  ADD CONSTRAINT `app1_add_food_fid_id_01e1c40d_fk_app1_register_id` FOREIGN KEY (`fid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_add_pets`
--
ALTER TABLE `app1_add_pets`
  ADD CONSTRAINT `app1_add_pets_pid_id_79492031_fk_app1_register_id` FOREIGN KEY (`pid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_cart_tb`
--
ALTER TABLE `app1_cart_tb`
  ADD CONSTRAINT `app1_cart_tb_fid_id_4c575ce8_fk_app1_add_food_id` FOREIGN KEY (`fid_id`) REFERENCES `app1_add_food` (`id`),
  ADD CONSTRAINT `app1_cart_tb_pid_id_551bda73_fk_app1_add_pets_id` FOREIGN KEY (`pid_id`) REFERENCES `app1_add_pets` (`id`),
  ADD CONSTRAINT `app1_cart_tb_userid_id_8cee2ced_fk_app1_register_id` FOREIGN KEY (`userid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_paymenttoshop_tb`
--
ALTER TABLE `app1_paymenttoshop_tb`
  ADD CONSTRAINT `app1_paymenttoshop_cartid_id_5cc42b57_fk_app1_cart_tb_id` FOREIGN KEY (`cartid_id`) REFERENCES `app1_cart_tb` (`id`),
  ADD CONSTRAINT `app1_paymenttoshop_shopid_id_9d8466f4_fk_app1_register_id` FOREIGN KEY (`shopid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_payment_tb`
--
ALTER TABLE `app1_payment_tb`
  ADD CONSTRAINT `app1_payment_tb_userid_id_c6f91ff9_fk_app1_register_id` FOREIGN KEY (`userid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_review_tb`
--
ALTER TABLE `app1_review_tb`
  ADD CONSTRAINT `app1_review_tb_cartid_id_86da8d7d_fk_app1_cart_tb_id` FOREIGN KEY (`cartid_id`) REFERENCES `app1_cart_tb` (`id`),
  ADD CONSTRAINT `app1_review_tb_fid_id_376a3ebd_fk_app1_add_food_id` FOREIGN KEY (`fid_id`) REFERENCES `app1_add_food` (`id`),
  ADD CONSTRAINT `app1_review_tb_pid_id_c609b0e8_fk_app1_add_pets_id` FOREIGN KEY (`pid_id`) REFERENCES `app1_add_pets` (`id`),
  ADD CONSTRAINT `app1_review_tb_userid_id_64568ef6_fk_app1_register_id` FOREIGN KEY (`userid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `app1_vetenery_tb`
--
ALTER TABLE `app1_vetenery_tb`
  ADD CONSTRAINT `app1_vetenery_tb_regid_id_12ee86a0_fk_app1_register_id` FOREIGN KEY (`regid_id`) REFERENCES `app1_register` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
