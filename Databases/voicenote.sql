drop database if exists `citizens_voicenote`;

create database citizens_voicenote;

use `citizens_voicenote`;

create table voicenote(
	voicenote_id int auto_increment not null,
	date_uploaded timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	voicenote_text varchar(100),
	voicenote_recording_url varchar(50),
	primary key(voicenote_id)
);

create table voicenote_contact(
	voicenote_id int,
	sender_email varchar(30),
	sender_telephone int,
	primary key (voicenote_id),
	Constraint FK_Voicenoteid foreign key (voicenote_id) references voicenote(voicenote_id) on delete restrict on update cascade
);

create table event_voicenote_log(
	voicenote_id int,
	dateprocessed timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key(voicenote_id),
	Constraint FK_Eventvoicenoteid foreign key (voicenote_id) references voicenote(voicenote_id) on delete restrict on update cascade
);