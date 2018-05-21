from eventCreator import eventCreator
from dbManagers.dbwordManager import wordManager
from eventDBManger import eventDBManager
from dbManagers.dbVoicenoteManager import voiceNoteManager
from siteCrawler.articleManager import articlesManager
from dbManagers.dbcaseManager import caseManager

class eventExtractor():

    casedbcontroller=caseManager()
    voicenotecontroller=voiceNoteManager()
    articlescontroller=articlesManager()
    casedbcontroller=caseManager()
    eventcreator=eventCreator()
    eventdbcontroller=eventDBManager()
    casestatements=[]
    casedescriptions=[]
    casenotes=[]
    voicenotes=[]
    reports=[]
    articles=[]
    
    
    def __init__(self):
        name='Event Extractor'
        self.__setSources()
    
    def runExtractor(self):
        print(self.casenotes)
        self.__extractEvents(self.__shortenarray(self.casestatements,'source_id','statement_id','statement'),'Case')
        self.__extractEvents(self.__shortenarray(self.casedescriptions,'case_id','No secondary id','description'),'Case')
        self.__extractEvents(self.__shortenarray(self.casenotes,'source_id','notes_id','notes'),'Case')
        self.__extractEvents(self.__shortenarray(self.voicenotes,'voicenote_id','No secondary id','voicenote_text'),'VoiceNote')
        self.__extractEvents(self.__shortenarray(self.reports,'source_id','No secondary id','report'),'Report`')
        self.__extractEvents(self.__shortenarray(self.articles,'article_id','No secondary id','content'),'Article')
    
    def __shortenarray(self,array,field1,field2,field3):
        eventshort=[]
        if field2=='No secondary id':
            eventshort=[[x[field1],-1,x[field3]] for x in array ] 
        else:
            eventshort=[[x[field1],x[field2],x[field3]] for x in array ]
        return eventshort
        
    def __getCaseInfo(self):
        casestatements,casedescription,casenotes=self.casedbcontroller.fetchUnprocessedCases()
        return [casestatements,casedescription,casenotes]
        
    
    def __setSources(self):
        temp=self.__getCaseInfo()
        self.casestatements=temp[0]
        self.casedescriptions=temp[1]
        self.casenotes=temp[2]
        self.voicenotes=self.__getVoiceNotes()
        self.reports=self.__getcaseReports()
        self.articles=self.__getArticles()
    
    
    def __getVoiceNotes(self):
        voicenotes=self.voicenotecontroller.fetchUnprocessedVoicenote()
        return voicenotes
        
        
    def __getArticles(self):
        articles=self.articlescontroller.fetchUnprocessedArticles()
        return articles
    
    
    def __getcaseReports(self):
        reports=self.casedbcontroller.fetchUnprocessedReports()
        return reports
    
    def __extractEvents(self,eventsources,source):
        eventstemp=[]
        if len(eventsources) > 0:
            for i in range(0,len(eventsources)):
                eventstemp.append(self.eventcreator.getSentenceEvents(eventsources[i][2]))
                self.eventdbcontroller.insertEvents(events,source,eventsources[0],eventsources[1])
        print(eventstemp)
        
    def __updateEventlogs(self,source_ids,source):
        if source=='Case':
            for i in range(0,len(source_ids)):
                self.casedbcontroller.updateCaseProcessTable(source_ids[i])
        if source=='Report':
            for i in range(0,len(source_ids)):
                self.casedbcontroller.updateReportProcessTable(source_ids[i])
        if source=='VoiceNote':
            for i in range(0,len(source_ids)):
                self.voicenotecontroller.updateProcessTable(source_ids[i])
        if source=='Article':
            for i in range(0,len(source_ids)):
                self.articlescontroller.updateProcessTable(source_ids[i])
    
    def __getInsertedIds(self):
        return 1
            
