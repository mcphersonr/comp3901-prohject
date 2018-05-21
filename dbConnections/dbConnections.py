import pymysql
import os

class dbConnection:
	connection={'host':os.environ["IP"],'user':os.environ["C9_USER"],'password':'','database':''}
	eventdb='events'
	casedb='case_files'
	voicenotedb='citizens_voicenote'
	word_db='words'
	articledb='news_article'
	
	def __init__(self):
		name='Connections'

	def getEventConnection(self):
		self.connection['database']=self.eventdb
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db
	
	def getArticleConnection(self):
		self.connection['database']=self.articledb
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db


	def getVoiceNoteConnection(self):
		self.connection['database']=self.voicenotedb
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db


	def getWordConnection(self):
		self.connection['database']=self.word_db
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db


	def getCaseConnection(self):
		self.connection['database']=self.casedb
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db

	def getTempConnection(self):
		self.connection['database']='entries'
		db=pymysql.connect(self.connection['host'],self.connection['user'],self.connection['password'],self.connection['database'])
		return db
	