from eventExtractor.eventCreator import eventCreator
from dbManagers.dbwordManager import wordManager
from eventExtractor.eventDBManger import eventDBManager
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
    
    def __init__(self):
        name='Event Extractor'
    
    def runExtractor(self):
        return 1
        
    def __getCaseInfo(self):
        casestatements,casedescription,casenotes=self.casedbcontroller.fetchUnprocessedCases()
        return casestatements,casedescription,casenotes
    
    def __getVoiceNotes(self):
        voicenotes=self.voicenotecontroller.fetchUnprocessedVoicenote()
        return voicenotes
        
        
    def __getArticles(self):
        articles=self.articlescontroller.fetchUnprocessedArticles()
        return articles
    
    
    def __getcaseReports(self):
        reports=casedbcontroller.fetchUnprocessedReports()
        return reports
    
    def __extractEvents(self,eventsources,source):
        for i in range(0,len(eventsources)):
            events=self.eventcreator.getSentenceEvents(eventsources[i][2])
            self.eventdbcontroller.insertEvents(events,source,eventsources[0],eventsources[1])
            
    def __updateEventlogs(self,source_ids,source):
        if source=='case':
            for i in range(0,len(source_ids)):
                casedbcontroller.updateCaseProcessTable(source_ids[i])
        if source=='reports':
            for i in range(0,len(source_ids)):
                casedbcontroller.updateReportProcessTable(source_ids[i])
        if source=='voicenotes':
            for i in range(0,len(source_ids)):
                voicenotecontroller.updateProcessTable(s)
        if source=='articles':
            for i in range(0,len(source_ids)):
                articlescontroller.updateProcessTable(source_ids[i])
    
    def __getInsertedIds(self):
        return 1
            
