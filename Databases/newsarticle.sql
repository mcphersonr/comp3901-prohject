drop database if exists `news_article`;

create database news_article;

use `news_article`;

create table articles(
	cid int auto_increment not null,
	title varchar(50),
	content varchar(255),
	article_date datetime,
	page_url varchar(255),
	date_fetched timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key(cid)
);


create table eventarticlelog(
	cid int,
	dateprocessed timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key (cid),
	Constraint FK_EventCrawlerid foreign key (cid) references articles(cid) on delete restrict on update cascade
);

create table sources(
	source_name varchar(255),
	source_page varchar(255),
	site_address varchar(255),
	primary key(source_name)
);


Insert into sources(source_name,source_page,site_address) values ('Jamaica Observer',"http://www.jamaicaobserver.com/results/","http://www.jamaicaobserver.com")

