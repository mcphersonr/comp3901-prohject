drop database if exists `words`;

create database words;

use `words`;

CREATE TABLE `word` (
	`word` varchar(255) NOT NULL,
	`datefound` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`count` int(11),
	primary key(word)
);

CREATE TABLE `keywords` (
  `keyword` varchar(255) NOT NULL,
  `datecreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  primary key(keyword),
  Constraint FK_KeyWord foreign key (keyword) references word(word) on delete restrict on update cascade 
);

-- --------------------------------------------------------

CREATE TABLE `wordpartscount`(
	`word` varchar(255) NOT NULL,
	`whocount` int(11),
	`whatcount` int(11),
	`whencount` int(11),
	`wherecount` int(11),
	primary key (word),
	Constraint FK_WordPartscount foreign key (word) references word(word) on delete restrict on update cascade
);

--
-- Table structure for table `whenwords`
--

CREATE TABLE `whenwords` (
  `word` varchar(255) NOT NULL,
  `whenpart` varchar(30) NOT NULL,
  primary key (word),
  Constraint FK_Wordwhen foreign key (word) references word(word) on delete restrict on update cascade 
); 


INSERT INTO `word` (`word`, `count`) VALUES
('am', 1),
('Apr', 1),
('April', 1),
('Aug', 1),
('August', 1),
('day', 1),
('Dec', 1),
('December', 1),
('Feb', 1),
('February', 1),
('Friday', 1),
('Jan', 1),
('January', 1),
('Jul', 1),
('July', 1),
('Jun', 1),
('June', 1),
('Mar', 1),
('March', 1),
('May', 1),
('Monday', 1),
('November', 1),
("o'clock", 1),
('October', 1),
('pm', 1),
('Saturday', 1),
('September', 1),
('Sunday', 1),
('Thursday', 1),
('Tuesday', 1),
('Wednesday', 1);



INSERT INTO `whenwords` (`word`, `whenpart`) VALUES
('am', 'time'),
('Apr', 'date'),
('April', 'date'),
('Aug', 'date'),
('August', 'date'),
('day', 'day'),
('Dec', 'date'),
('December', 'date'),
('Feb', 'date'),
('February', 'date'),
('Friday', 'day'),
('Jan', 'date'),
('January', 'date'),
('Jul', 'date'),
('July', 'date'),
('Jun', 'date'),
('June', 'date'),
('Mar', 'date'),
('March', 'date'),
('May', 'date'),
('Monday', 'day'),
('November', 'date'),
('o''clock', 'time'),
('October', 'date'),
('pm', 'time'),
('Saturday', 'day'),
('September', 'date'),
('Sunday', 'day'),
('Thursday', 'day'),
('Tuesday', 'day'),
('Wednesday', 'day');



-- --------------------------------------------------------

--
-- Table structure for table `wherewords`
--

CREATE TABLE `wherewords` (
  `word` varchar(255) NOT NULL,
  `pos` varchar(30) NOT NULL,
  primary key(word)
);



--
-- Dumping data for table `wherewords`
--
INSERT INTO `word` (`word`, `count`) VALUES
('across', 1),
('after', 1),
('against', 1),
('along', 1),
('among', 1),
('area', 1),
('at', 1),
('before', 1),
('behind', 1),
('between', 1),
('blvd', 1),
('boulevard', 1),
('by', 1),
('city', 1),
('close', 1),
('community', 1),
('crescent', 1),
('district', 1),
('down', 1),
('drive', 1),
('in', 1),
('lane', 1),
('near', 1),
('off', 1),
('on', 1),
('over', 1),
('parish', 1),
('road', 1),
('street', 1),
('through', 1),
('to', 1),
('towards', 1),
('town', 1),
('vicinity', 1);

INSERT INTO `wherewords` (`word`, `pos`) VALUES
('across', 'prep'),
('after', 'prep'),
('against', 'prep'),
('along', 'prep'),
('among', 'prep'),
('area', 'noun'),
('at', 'prep'),
('before', 'prep'),
('behind', 'prep'),
('between', 'prep'),
('blvd', 'noun'),
('boulevard', 'noun'),
('by', 'prep'),
('city', 'noun'),
('close', 'noun'),
('community', 'noun'),
('crescent', 'noun'),
('district', 'noun'),
('down', 'prep'),
('drive', 'noun'),
('in', 'prep'),
('lane', 'noun'),
('near', 'prep'),
('off', 'prep'),
('on', 'prep'),
('over', 'prep'),
('parish', 'noun'),
('road', 'noun'),
('street', 'noun'),
('through', 'prep'),
('to', 'prep'),
('towards', 'prep'),
('town', 'noun'),
('vicinity', 'noun');


CREATE TABLE `keyword_avg` (
`avg_description` varchar(25),
`avg_figure` int,
primary key(avg_description)
);
-- --------------------------------------------------------