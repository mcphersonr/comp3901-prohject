drop database if exists `events`;

create database events;

use `events`;

create table events(
	event_id int,
	datecreated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	process_status int NOT NULL DEFAULT 0,
	dateprocess datetime,
	primary key(event_id)
);

create table eventsource(
	event_id int,
	source_id int,
	primary key (event_id,source_id)
);

create table source(
	source_id int auto_increment not null,
	external_id int,
	source varchar(150),
	primary key (source_id)
);

create table who (
	who_id int auto_increment not null,
	event_who text,
	event_certainty float,
	primary key (who_id)
);

create table eventwho(
	event_id int,
	who_id int,
	primary key(event_id, who_id),
	Constraint FK_Eventwhoid foreign key (event_id) references events (event_id) on delete restrict on update cascade,
	Constraint FK_Whoid foreign key (who_id) references who (who_id) on delete restrict on update cascade
);

create table what (
	what_id int auto_increment not null,
	event_what text,
	event_certainty float,
	primary key (what_id)
);

create table eventwhat(
	event_id int,
	what_id int,
	primary key(event_id, what_id),
	Constraint FK_Eventwhatid foreign key (event_id) references events (event_id) on delete restrict on update cascade,
	Constraint FK_Whatid foreign key (what_id) references what (what_id) on delete restrict on update cascade
);

create table wheredata (
	where_id int auto_increment not null,
	event_where text,
	event_certainty float,
	primary key (where_id)
);

create table eventwhere(
	event_id int,
	where_id int,
	primary key(event_id, where_id),
	Constraint FK_Eventwhereid foreign key (event_id) references events (event_id) on delete restrict on update cascade,
	Constraint FK_Whereid foreign key (where_id) references wheredata (where_id) on delete restrict on update cascade
);

create table whenday(
	when_id int auto_increment not null,
	dayinfo varchar(255),
	event_certainty
	primary key (when_id)
);


create table whentime(
	when_id int auto_increment not null,
	timeinfo time,
	event_certainty,
	primary key (when_id)
);

create table whendate(
	when_id int auto_increment not null,
	dateinfo date,
	event_certainty,
	primary key (when_id)
);

create table whenparts(
	whenpart varchar(50),
	primary key(whenpart)
);

create table percentages(
	percentage_id int auto_increment not null,
	effectivedate datetime,
	who_percent float,
	what_percent float,
	where_percent float,
	when_percent float,
	unique key(effectivedate),
	primary key(percentage_id)
);

create table eventwhen(
	event_id int,
	when_id int,
	whenpart varchar(50),
	primary key(event_id,when_id,whenpart),
	Constraint FK_Whenpartid foreign key (whenpart) references whenparts(whenpart) on delete restrict on update cascade,
	Constraint FK_Eventwhenid foreign key (event_id) references events (event_id) on delete restrict on update cascade
);

create table linked_events(
	parent_id int,
	child_id int,
	score float, 
	primary key(parent_id,child_id),
	Constraint FK_LinkEventparentid foreign key (parent_id) references events (event_id) on delete restrict on update cascade,
	Constraint FK_LinkEventchildid foreign key (child_id) references events (event_id) on delete restrict on update cascade
);

Insert into whenparts(whenpart) values('day'),('date'),('time');
Insert into percentages(effectivedate,who_percent,what_percent,where_percent,when_percent) values ('1880-01-01',0.45,0.35,0.12,0.08);