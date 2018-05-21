drop database if exists `case_files`;

create database case_files;

use `case_files`;

/* Personal information*/
create table user(
	user_id int auto_increment not null,
	user_fname varchar(20),
	user_lname varchar(20),
	user_email varchar(30),
	primary key(user_id)
);

create table citizen(
	citizen_id int auto_increment not null,
	citizen_fname varchar(20),
	citizen_lname varchar(20),
	citizen_street varchar(20),
	citizen_parish varchar(20),
	citizen_telephone int,
	citizen_signature_path varchar(50),
	primary key(citizen_id)
);

create table citizen_create(
	user_id int,
	citizen_id int,
	Constraint FK_Useruserid foreign key(user_id) references user(user_id) on delete restrict on update cascade,
	Constraint FK_Citizenid foreign key(citizen_id) references citizen(citizen_id) on delete restrict on update cascade
);

/********************************/



/**********Case Data****************************/
create table caselog(
	case_id int auto_increment not null,
	date_occured datetime,
	report_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	case_description varchar(255),
	case_street varchar(30),
	case_parish varchar(30),
	status varchar(30),
	primary key(case_id)
);

create table case_create(
	user_id int,
	case_id int,
	primary key(user_id, case_id),
	Constraint FK_Caseuserid foreign key(user_id) references user(user_id) on delete cascade on update cascade,
	Constraint FK_Casecaseid foreign key(case_id) references caselog(case_id) on delete cascade on update cascade
);


create table casefile_victims(
	case_id int,
	victim varchar(100),
	primary key(case_id, victim),
	Constraint FK_Casevictim foreign key (case_id) references caselog(case_id) on delete restrict on update cascade
);

create table casefile_accused(
	case_id int,
	accused varchar(100),
	primary key(case_id, accused),
	Constraint FK_Caseaccused foreign key (case_id) references caselog(case_id) on delete restrict on update cascade
);

create table statement(
	statement_id int auto_increment not null,
	statement_text varchar(100),
	statement_recording_path varchar(50),
	primary key(statement_id)
);

create table citizen_statement_add(
	user_id int,
	statement_id int,
	case_id int,
	dateadded timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	primary key(user_id,statement_id,case_id),
	Constraint FK_Casestatementuserid foreign key(user_id) references user(user_id) on delete restrict on update cascade,
	Constraint FK_Casestatementcaseid foreign key(case_id) references caselog(case_id) on delete restrict on update cascade,
	Constraint FK_Casestatementid foreign key(statement_id) references statement(statement_id) on delete restrict on update cascade
);

create table police_notes(
	police_notes_id int auto_increment not null,
	police_notes text,
	primary key (police_notes_id)
);

create table case_notes(
	user_id int,
	case_id int,
	police_notes_id int,
	dateadded timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key(user_id,case_id,police_notes_id),
	Constraint FK_NotesCaseid foreign key (case_id) references caselog(case_id) on delete restrict on update cascade,
	Constraint FK_Casenotesuserid foreign key (user_id) references user(user_id) on delete restrict on update cascade,
	Constraint FK_Policenotesid foreign key (police_notes_id) references police_notes(police_notes_id) on delete restrict on update cascade
);

create table eventcaselog(
	source_id int,
	dateprocessed timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key (source_id),
	Constraint FK_EventCaseid foreign key (source_id) references caselog(case_id) on delete restrict on update cascade
);


/*create table caserelated(
	case_id int,
	caserelated_id int,
	primary key(case_id,caserelated_id),
	foreign key(case_id) references caselog(case_id) on delete cascade on update cascade,
	foreign key(caserelated_id) references caselog(case_id) on delete cascade on update cascade
)*/ 

/**********************Case Data *****************/


/***************Report Data**********************/
create table report(
	report_id int auto_increment not null,
	report_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	report_text varchar(255),
	report_recording_path varchar(50),
	primary key(report_id)
);

create table report_create(
	user_id int,
	report_id int,
	primary key(user_id,report_id),
	Constraint FK_Reportuserid foreign key(user_id) references user(user_id) on delete restrict on update cascade,
	Constraint FK_Reportid foreign key(report_id) references report(report_id) on delete restrict on update cascade
);


create table citizen_report_add(
	report_id int,
	citizen_id int,
	user_id int,
	primary key(report_id,citizen_id,user_id),
	Constraint FK_Reportaddreportid foreign key(report_id) references report(report_id) on delete restrict on update cascade,
	Constraint FK_Reportaddcitizenid foreign key(citizen_id) references citizen(citizen_id) on delete restrict on update cascade,
	Constraint FK_Reportadduserid foreign key(user_id) references user(user_id) on delete restrict on update cascade
);



create table eventreportlog(
	source_id int,
	dateprocessed timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key (source_id),
	Constraint FK_EventReportid foreign key(source_id) references report(report_id) on delete restrict on update cascade
);

/***************Report Data**********************/



insert into user(user_id,user_fname,user_lname,user_email) values (1,'Ramone','McPherson','rmcpherson@hotmail.com');
insert into user(user_id,user_fname,user_lname,user_email) values (2,'Shemara','Nation','snation@hotmail.com');
insert into user(user_id,user_fname,user_lname,user_email) values (3,'Milton','Edwards','medwards@gmail.com');
insert into user(user_id,user_fname,user_lname,user_email) values (4,'Amelia','Francis','afrancis@outlook.com');
insert into user(user_id,user_fname,user_lname,user_email) values (5,'Jhevaughn','Mais','jmais@yahoo.com');
insert into user(user_id,user_fname,user_lname,user_email) values (6,'Debbie','Lynch','dlynch@gmail.com');	
insert into user(user_id,user_fname,user_lname,user_email) values (7,'Lashana','Mills','lmills@outlook.com');
insert into user(user_id,user_fname,user_lname,user_email) values (8,'Peter','Downer','pdowner@yahoo.com');
insert into user(user_id,user_fname,user_lname,user_email) values (9,'Ryan','Paiz','rpaiz@gmail.com');
insert into user(user_id,user_fname,user_lname,user_email) values (10,'Catherine','McBroom','cmcbroom@hotmail.com');


-- yy/mm/dd
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values (1,'2017-05-09','2017-05-10','Shoot out with gun men in August Town','River Lane','Kingston','open');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values (2,'2018-02-20','2018-02-20','Stolen vehicle','Mountain View','Kingston','open');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(3,'2016-03-19','2016-03-20','Shooting of Clive Williams','Hughenden Drive','St.Thomas','closed');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(4,'2015-07-18','2015-07-18','John Brown was murdered in St.Ann','St.Lewis Drive','St.Ann','open');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(5,'2017-01-25','2017-01-26','','Luke Street','St. James','closed');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(6,'2018-04-01','2018-04-01','','Church Drive','Portland','open');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(7,'2014-08-01','2014-08-01','','Spanish Bridge','Trelawny','closed');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(8,'2015-10-11','2015-10-11','','South Avenue','St.Andrew','open');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(9,'2017-12-30','2017-12-31','','Andrew Parkways','Mandeville','closed');
insert into caselog(case_id,date_occured,report_time,case_description,case_street,case_parish,status) values(10,'2016-06-10','2016-06-11','','Emily Heights','Kingston','open');

insert into casefile_victims(case_id,victim) values (1,'Dean Jones');
insert into casefile_victims(case_id,victim) values (2,'Anthony Blackwood');
insert into casefile_victims(case_id,victim) values(3,'Clive Williams');
insert into casefile_victims(case_id,victim) values(4,'John Brown');
insert into casefile_victims(case_id,victim) values(5,'Yanique Allen');
insert into casefile_victims(case_id,victim) values(6,'Jocelyn Solomon');
insert into casefile_victims(case_id,victim) values(7,'Joseph Martin');
insert into casefile_victims(case_id,victim) values(8,'Robert Johnson');
insert into casefile_victims(case_id,victim) values(9,'Kayla Ayala');
insert into casefile_victims(case_id,victim) values(10,'Bonnie Parrish');


 insert into casefile_accused(case_id, accused) values (1,'John Smith');
 insert into casefile_accused(case_id, accused) values (2,'Junior Reid');
 insert into casefile_accused(case_id, accused) values(3,'Marlon Jones');
 insert into casefile_accused(case_id, accused) values(4,'Steven Richards');
 insert into casefile_accused(case_id, accused) values(5,'George Bush');
 insert into casefile_accused(case_id, accused) values(6,'Michael Cooper');
 insert into casefile_accused(case_id, accused) values(7,'Haley Beck');
 insert into casefile_accused(case_id, accused) values(8,'Thomas Morris');
 insert into casefile_accused(case_id, accused) values(9,'Mark Ballard');
 insert into casefile_accused(case_id, accused) values(10,'Larry Gonzalez');	


insert into report(report_id,report_time,report_text,report_recording_path) values (1,'2017-05-10','Uriel James, alias Rooksie, the reputed area leader of Rose Town — one of Kingston toughest communities — was reportedly murdered last night.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (2,'2018-12-20','The Shady Grove police have arrested and charged a 17-year-old male for several offences following the death of a man who was unable to speak or hear and the injuring of another during a robbery in Top Hill, St Catherine on January 13.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (3,'2016-03-20','OMAR “Best” Collymore, the 35-year-old man accused of masterminding the murder of his wife on Stanley Terrace in Red Hills, St Andrew','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (4,'2015-07-18','A man who was implicated in a triple murder at Yohan Close in Linstead, St Catherine was arrested during an operation in Frazers Content in the parish yesterday','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (5,'2017-01-26','Police in Santa Cruz, St Elizabeth are investigating the death of a woman who was found with her throat slashed at her home in Park district in the parish yesterday.Dead is 22-year-old Yashika Smith, otherwise called Rushell','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (6,'2018-06-12','The St Thomas police have arrested a suspect in relation to the double murder of an elderly couple in the parish on Tuesday, January 9. Following preliminary investigations the suspect was held in Seaforth district yesterday.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (7,'2014-08-01','A 43-year-old man was shot dead while his son escaped with injuries after they were pounced upon by unknown assailants while driving through the Mount Carey district in Anchovy, St James yesterday.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (8,'2015-10-11','A woman accused of luring her baby father to a motel in Kingston, where she and the father of another of her children allegedly stabbed and chopped him to death last June, was yesterday remanded when she appeared in the Kingston and St Andrew Parish Court.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (9,'2017-12-31','Three men have been charged with the murder of Chinese businessman Teng Fei Cheng, who was shot dead on February 27, in Browns Town, St Ann.','URL');
insert into report(report_id,report_time,report_text,report_recording_path) values (10,'2016-06-11','THE police say a 16-year-old boy has been charged in connection with the November 12 triple murder of a father and his two sons in Osbourne Store, Clarendon','URL');


insert into statement(statement_id,statement_text,statement_recording_path) values (1,'Robert and I was arguing about money problems. We started to raise our voices during the argument and Robert hit me in the head with a pillow because I cursed at him. Afterwards, I threw a pillow back at him. He then said to me "Youre not going to hit me" and then he hit me in 
the back of my head with his fist. I then threw a bottle of baby wash at him. Robert then grabbed me by my arms and hair and forced me to the floor and kicked me but I could not remember exactly where. I started feeling a lot of pain. My son, Ariel saw the fight and watched as her pulled me from the bathroom to the living room. He began to cry. ','URL');

insert into statement(statement_id,statement_text,statement_recording_path) values (2,'I have blood pressure so that is why I was sweating a lot when I arrived. Vianney was very angry today about her checking account. We started to argue and grabbed her by her elbows so she could listen calmly as I spoke to her. When I grabbed her by her elbows she started to scratch
me on my arms. (An actual scratch was on his arm however, not big enough to photograph). I beat her with a pillow. You know what I better watch what I’m saying I hit her with the pillow. She then continued to attempt to scratch and kick me in my groin. I don’t remember ever pulling her hair. We even tried to keep Ariel from seeing.','URL');

insert into statement(statement_id,statement_text,statement_recording_path) values (3,'I, Anna Rossi, of 3 Arthur Street, Croydon Park NSW 2133, home duties, state: On 1 December 2017 at about 3:30pm, I was about to get into my car in the car park next to the shops on Burwood Road, Burwood NSW 2134.I noticed that a red Toyota Yaris was driving down the lane behind me.
I saw a black Mazda 3 reverse out of a car space and collide with the red Toyota Yaris. The red car was moving at the time of the collision. My car was parked opposite where the accident happened. The driver of the black car got out of his car. He did not seem to be hurt. Both drivers exchanged details. The driver of the black car said "Did you see the accident?” 
I said words to the effect "I saw it". He then said "Can you give me your contact details, just in case I need a statement from you". I replied "Yes". I then gave him my contact details. It was a sunny day. The speed limit in the car park was 20km per hour. The red car seemed to be travelling faster than that. I noticed damage to the back left side of the black Mazda 3. I believe that the contents of this statement are true and correct.','URL');

insert into statement(statement_id,statement_text,statement_recording_path) values (4,'At 5:22 p.m. on May 12, 2010, I was dispatched to 239 Carol Avenue regarding a theft. Lawrence Cooper (DOB 7-15-1987) reported that his son David’s bicycle had been stolen. Cooper told me: David (DOB 11-04-2001) had brought the bicycle into the carport the evening before (May 11). The bicycle wasn’t locked. The bicycle is a blue Sears boys’ bicycle with black tires 
and black handlebars. The bicycle is three years old. David went to the carport after school to ride the bicycle. He saw the bicycle was missing. When his father came home, David told him that the bike had been stolen. Lawrence called the police at 5:20.','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (5,'Gaines told me he lives alone. He was out of town on business when the burglary happened. He had left on Monday, April 5, at approximately 6:15 p.m. and returned on Friday morning at approximately 8:45 a.m. Because he used his car for the trip, there was no car in his carport when he was gone. He said because he left during daylight, he hadn’t thought to leave any 
lights burning. He is a sales representative for Pfizer, and many people know that he often does business from home and makes sales trips. When he returned from his trip, he saw a broken window over the kitchen table.','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (6,'I heard Gary go into our bedroom. He then walked past me carrying a bag and slammed the door on his way out. When I went into the bedroom I noticed that my laptop was missing. The next day I sent Gary a text message with words to the effect of: "Please return my laptop. I need to pay the mortgage and electricity. They are due tomorrow." Gary did not reply. Gary 
has been verbally abusive to me in the past. He has also thrown objects but this is the first time he has physically hurt me. Since losing his job, Gary has been drinking heavily, often finishing a six-pack of beer every night. This makes him more agitated and aggressive.','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (7,'Paul opened the wallet and removed some bank notes. He said, “Where’s the credit card” I said, “I don’t have any, just get out I’m going to call the police”. He then moved towards me and as he walked past he grabbed me by the left shoulder, pulled me towards him and head-butted me on the left side of my head. 
I fell to the floor in pain and was lapsing in and out of consciousness. I saw him leave my house and get into a silver ford fiesta car, which he had parked on my drive and I could see it through the lounge and front door. I know he owns this car. He got into the driver’s side and drove off spinning the wheels.','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (8,'On February 12, 2011, I lied about me going into that truck, my intentions were to go steal. The SUV then rolled up to the Stanley farm, but the group was simply looking for help with the tire. I was blinded by glass when the SUV’s windshield was smashed. I jumped out and ran after the SUV hit another vehicle on the Stanley farm. We didn’t think about it. We just ran.
I was scared out of my mind. As I was running and as I was to the approach another vehicle further up I heard a ricochet. I heard a bullet right by my right ear. I saw my father standing beside the SUV looking sick with a gun in his hand saying, “It just went off.” ','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (9,'On August 10th Mr. Darryl Hunt and Sammy Mitchell were at Motel 6 and Darryl Hunt and Sammy Mitchell left the room at about 6:00 a.m. and that they were both wearing black shirts and black pants and Darryl told me he was going to call a cab. The next time I saw Darryl was about 9:30 a.m. and he was nervous when he came back to the motel room and he said he needed a drink.
Darryl had mud or grass stains on his pants knees.','URL');
insert into statement(statement_id,statement_text,statement_recording_path) values (10,'He has his body against the door preventing me from opening it. His stomach was against the door. His hands were inside on me... he had to duck his head to come inside my vehicle and he entered my vehicle with his hands, his arms, his head ... assaulting me ... The first time he struck me somewhere in this area, but it was a glancing blow "cause I was able to defend a little bit.
After that I was just scrambling to get his arms out of my face and grabbing me and everything else. He turned to his left and handed the first subject ...a pack of several cigarillos which was just stolen from the Market Store. And when he did that I grabbed his right arm trying just to control something. As I was holding it he came around with his arm extended, fist made, and went like that straight at my face with a full swing with his left hand.','URL');


insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (1,'Snooki','White','Augusta Drive','St.Thomas',2389087,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (2,'Carl','Edwards','Reef Avenue','Kingston',4678219,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (3,'Andrea','Lee','Barry Street','Kingston',7623091,'URL   ');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (4,'Stephen', 'Roth','Morgan Stream', 'St.James',5489023,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (5,'Sonia', 'Bauer','Portland Circle','St.Catherine',8910349,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (6,'Kenneth', 'Donovan','Duke Street','Westmoreland',3409874,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (7,'Jeffrey', 'Sullivan','Highgate','St.Mary',7261098,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (8,'Sarah', 'Banks', 'Haughton Court','Hanover',7245679,'URL');
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (9,'Maria', 'Rodriguez', 'Goshen','St.Elizabeth',6428976,'URL' );
insert into citizen(citizen_id,citizen_fname,citizen_lname,citizen_street,citizen_parish,citizen_telephone,citizen_signature_path) values (10,'Frances', 'Velez','Dawkins Drive', 'Clarendon',2569714,'URL');

insert into caserelated(case_id,caserelated_id) values (1,1);
insert into caserelated(case_id,caserelated_id) values (2,2);
insert into caserelated(case_id,caserelated_id) values (3,3);
insert into caserelated(case_id,caserelated_id) values (4,4);
insert into caserelated(case_id,caserelated_id) values (5,5);
insert into caserelated(case_id,caserelated_id) values (6,6);
insert into caserelated(case_id,caserelated_id) values (7,7);
insert into caserelated(case_id,caserelated_id) values (8,8);
insert into caserelated(case_id,caserelated_id) values (9,9);
insert into caserelated(case_id,caserelated_id) values (10,10);
*/

insert into case_create(user_id,case_id) values (1,1);
insert into case_create(user_id,case_id) values (2,2);
insert into case_create(user_id,case_id) values (3,3);
insert into case_create(user_id,case_id) values (4,4);
insert into case_create(user_id,case_id) values (5,5);
insert into case_create(user_id,case_id) values (6,6);
insert into case_create(user_id,case_id) values (7,7);
insert into case_create(user_id,case_id) values (8,8);
insert into case_create(user_id,case_id) values (9,9);
insert into case_create(user_id,case_id) values (10,10);


insert into citizen_statement_add(user_id,statement_id,case_id) values (1,1,1);
insert into citizen_statement_add(user_id,statement_id,case_id) values (2,2,2);
insert into citizen_statement_add(user_id,statement_id,case_id) values (3,3,3);
insert into citizen_statement_add(user_id,statement_id,case_id) values (4,4,4);
insert into citizen_statement_add(user_id,statement_id,case_id) values (5,5,5);
insert into citizen_statement_add(user_id,statement_id,case_id) values (6,6,6);
insert into citizen_statement_add(user_id,statement_id,case_id) values (7,7,7);
insert into citizen_statement_add(user_id,statement_id,case_id) values (8,8,8);
insert into citizen_statement_add(user_id,statement_id,case_id) values (9,9,9);
insert into citizen_statement_add(user_id,statement_id,case_id) values (10,10,10);


insert into report_create(user_id,report_id) values (1,1);
insert into report_create(user_id,report_id) values (2,2);
insert into report_create(user_id,report_id) values (3,3);
insert into report_create(user_id,report_id) values (4,4);
insert into report_create(user_id,report_id) values (5,5);
insert into report_create(user_id,report_id) values (6,6);
insert into report_create(user_id,report_id) values (7,7);
insert into report_create(user_id,report_id) values (8,8);
insert into report_create(user_id,report_id) values (9,9);
insert into report_create(user_id,report_id) values (10,10);


insert into citizen_create(user_id,citizen_id) values (1,1);
insert into citizen_create(user_id,citizen_id) values (2,2);
insert into citizen_create(user_id,citizen_id) values (3,3);
insert into citizen_create(user_id,citizen_id) values (4,4);
insert into citizen_create(user_id,citizen_id) values (5,5);
insert into citizen_create(user_id,citizen_id) values (6,6);
insert into citizen_create(user_id,citizen_id) values (7,7);
insert into citizen_create(user_id,citizen_id) values (8,8);
insert into citizen_create(user_id,citizen_id) values (9,9);
insert into citizen_create(user_id,citizen_id) values (10,10);


insert into citizen_report_add(report_id,citizen_id,user_id) values (1,1,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (2,2,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (3,3,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (4,4,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (5,5,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (6,6,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (7,7,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (8,8,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (9,9,1);
insert into citizen_report_add(report_id,citizen_id,user_id) values (10,10,1);




