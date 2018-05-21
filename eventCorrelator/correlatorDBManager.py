from dbConnections.dbConnections import dbConnection
class correlatorDBManager:
    db=dbConnection().getEventConnection()
    cursor=db.cursor()
    def __init__(self):
        name='Correlator Connection'
        
    def getCorrelatorPercentages(self):
        percentage="Select who_percent,what_percent,when_percent,where_percent from percentages"
        self.cursor.execute(percentage)
        percentlist=self.cursor.fetchall()
        percentages={'who':percentlist[0][0],'what':percentlist[0][1],'when':percentlist[0][2],'where':percentlist[0][3]}
        return percentages
            
    def updateCertainty(self):
        return 1
    
    def insertLinkedEvents(self,parent_id,child_id,score):
        correlation="Insert into linked_events(parent_id,child_id,score) values('{0}','{1}','{2}')".format(parent_id,child_id,score)
        self.cursor.execute(correlation)
        self.db.commit()
        
    def getUnprocessedEvents(self):
        return self.__getEvents(0)
        
    
    def getProcessedEvents(self):
        return self.__getEvents(1)
        
    def __getEvents(self,status):
        eventslog=[]
        
        events="Select events.event_id,event_who,event_what,event_where,whentemp.dayinfo,whentemp.timeinfo,whentemp.dateinfo from events left join (Select event_who,event_id from who inner join eventwho on eventwho.who_id=who.who_id where event_id in " 
        events+="(Select event_id from events where process_status='{0}')) as whotemp on events.event_id=whotemp.event_id left join ".format(status) 
        events+="(Select event_what,event_id from what inner join eventwhat on eventwhat.what_id=what.what_id where event_id in " 
        events+="(Select event_id from events where process_status='{0}')) as whattemp on events.event_id=whattemp.event_id left join ".format(status)
        events+="(Select event_where,event_id from wheredata inner join eventwhere on eventwhere.where_id=wheredata.where_id where event_id in " 
        events+="(Select event_id from events where process_status='{0}')) as wheretemp on events.event_id=wheretemp.event_id left join (".format(status)
        events+="Select events.event_id, day.dayinfo, timepart.timeinfo, datepart.dateinfo from events left join (Select dayinfo,event_id from whenday join eventwhen on whenday.when_id=eventwhen.when_id where whenpart='day' "
        events+="and event_id in (Select event_id from events where process_status='{0}')) as day on events.event_id=day.event_id left join".format(status)
        events+="(Select timeinfo,event_id from whentime join eventwhen on whentime.when_id=eventwhen.when_id where whenpart='time' "
        events+="and event_id in (Select event_id from events where process_status='{0}')) as timepart on events.event_id=timepart.event_id left join ".format(status)
        events+="(Select dateinfo,event_id from whendate join eventwhen on whendate.when_id=eventwhen.when_id where whenpart='date' "
        events+=" and event_id in (Select event_id from events where process_status='{0}')) as datepart on events.event_id=datepart.event_id ) as whentemp on whentemp.event_id=events.event_id where events.event_id "
        events+="in (Select event_id from events where process_status='{0}')".format(status)
        
        self.cursor.execute(events)
        eventlist=self.cursor.fetchall()
        for i in range (0,len(eventlist)):
            eventslog.append({'event_id':eventlist[i][0],
            'who':eventlist[i][1],'what':eventlist[i][2],
            'where':eventlist[i][3],'when':{'day':eventlist[i][4],'date':eventlist[i][6],'time':eventlist[i][5]}})
        return eventslog
        