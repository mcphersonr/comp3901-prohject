from dbConnections.dbConnections import dbConnection
from dbManagers.dbwordManager import wordManager

class eventDBManager:
    db=dbConnection().getEventConnection()
    cursor=db.cursor()
    wordlogger=wordManager()
    def __init__(self):
        name='Event Connection'
        
    def insertEvents(self,events,source,externalid,secondary_id):
        tables=[]
        for i in range (0,len(events)):
            event=events[i]
            self.__createEvent(event['who'],event['what'],event['when'],event['where'],source,externalid,secondary_id)
    
    def __createEvent(self,who,what,when,where,source,externalid,secondary_id):
        numsql="Select max(event_id) from events"
        try:
            self.cursor.execute(numsql)
            number=self.cursor.fetchall()[0][0]
            if number is None:
                number=1
                
            else:
                number=number+1
            
            newevent="Insert into events(event_id) values({0})".format(number)
            newsource="Insert into source(external_id,secondary_id,source) values('{0}','{1}','{2}')".format(externalid,secondary_id,source)
            self.cursor.execute(newevent)
            if self.cursor.rowcount >0:
                self.db.commit()
                self.__eventwho(who,number)
                self.__eventwhat(what,number)
                self.__eventwhere(where,number)
                self.__eventwhen(when,number)
                self.cursor.execute(newsource)
                if self.cursor.rowcount > 0:
                    self.cursor.execute(newsource)
                    self.db.commit()
                    newsourceid="Select max(source_id) from source"
                    self.cursor.execute(newsourceid)
                    sourceid=self.cursor.fetchall()[0][0]
                    neweventsource="Insert into eventsource(event_id,source_id) values ('{0}','{1}')".format(number,sourceid)
                    self.cursor.execute(neweventsource)
                    self.db.commit()
        except:
            'Error'
            
    def __eventwho(self,who,eventid):
        if who=='No who found':
            return 0
        else:
            newwho="Insert into who (event_who) values ('{0}')".format(who)
            self.cursor.execute(newwho)
            if self.cursor.rowcount > 0:
                self.db.commit()
                whosearch="Select max(who_id) from who"
                self.cursor.execute(whosearch)
                whoid=self.cursor.fetchall()[0][0]
                neweventwho="Insert into eventwho(who_id,event_id) values ({0},{1})".format(whoid,eventid)
                self.cursor.execute(neweventwho)
                self.db.commit()
                self.wordlogger.eventWordCount(who,'who')
                return 1
            else:
                return -1
        
    def __eventwhat(self,what,eventid):
        if what=='No what found':
            return 0
        else:
            newwhat="Insert into what (event_what) values ('{0}')".format(what)
            self.cursor.execute(newwhat)
            if self.cursor.rowcount > 0:
                self.db.commit()
                whatsearch="Select max(what_id) from what"
                self.cursor.execute(whatsearch)
                whatid=self.cursor.fetchall()[0][0]
                neweventwhat="Insert into eventwhat(what_id,event_id) values ({0},{1})".format(whatid,eventid)
                self.cursor.execute(neweventwhat)
                self.db.commit()
                self.wordlogger.eventWordCount(what,'what')
                return 1
            else:
                return -1
        
    def __eventwhere(self,where,eventid):
        if where=='No where found':
            return 0
        else:
            newwhere="Insert into wheredata (event_where) values ('{0}')".format(where)
            self.cursor.execute(newwhere)
            if self.cursor.rowcount > 0:
                self.db.commit()
                wheresearch="Select max(where_id) from wheredata"
                self.cursor.execute(wheresearch)
                whereid=self.cursor.fetchall()[0][0]
                neweventwhere="Insert into eventwhere(where_id,event_id) values ({0},{1})".format(whereid,eventid)
                self.cursor.execute(neweventwhere)
                self.db.commit()
                self.wordlogger.eventWordCount(where,'where')
            else:
                return -1
        
    def __eventwhen(self,when,eventid):
        if when=='No when found':
            return 0
        else:
            date=0
            day=0
            time=0
            try:
                if when[0]['day']:
                    day=1
                if when[0]['date']:
                    date=1
                if when[0]['time']:
                    time=1
            except:
                'Error'
            if day==1:
                newday="Insert into whenday (dayinfo) values ('{0}')".format(when[0]['day'])
                self.cursor.execute(newday)
                if self.cursor.rowcount > 0:
                    self.db.commit()
                    whenpartsearch="Select max(when_id) from whenday"
                    self.cursor.execute(whenpartsearch)
                    when_id=self.cursor.fetchall()[0][0]
                    neweventday="Insert into eventwhen (when_id,event_id,whenpart) values ('{0}','{1}','{2}')".format(when_id,eventid,'day')
                    self.cursor.execute(neweventday)
                    self.db.commit()
                    
            if  date==1:
                newdate="Insert into whendate (dateinfo) values ('{0}')".format(when[0]['date'])
                self.cursor.execute(newdate)
                if self.cursor.rowcount > 0:
                    self.db.commit()
                    whenpartsearch="Select max(when_id) from whendate"
                    self.cursor.execute(whenpartsearch)
                    when_id=self.cursor.fetchall()[0][0]
                    neweventdate="Insert into eventwhen (when_id,event_id,whenpart) values ('{0}','{1}','{2}')".format(when_id,eventid,'date')
                    self.cursor.execute(neweventdate)
                    self.db.commit()
                    
            if  time==1:
                newtime="Insert into whentime (timeinfo) values ('{0}')".format(when[0]['time'])
                self.cursor.execute(newtime)
                if self.cursor.rowcount > 0:
                    self.db.commit()
                    whenpartsearch="Select max(when_id) from whentime"
                    self.cursor.execute(whenpartsearch)
                    when_id=self.cursor.fetchall()[0][0]
                    neweventtime="Insert into eventwhen (when_id,event_id,whenpart) values ('{0}','{1}','{2}')".format(when_id,eventid,'time')
                    self.cursor.execute(neweventtime)
                    self.db.commit()
                    
    def checkInserts(self,sourcelist,source):
        return 1
            