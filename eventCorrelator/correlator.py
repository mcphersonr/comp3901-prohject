import correlatorDBManager
from eventCorrelator import eventCorrelator
from correlatorDBManager import correlatorDBManager


class correlator():
    dbcontroller=correlatorDBManager()
    percentages=dbcontroller.getCorrelatorPercentages()
    correlator=eventCorrelator(percentages)
    
    def __init__(self):
        name='Correlator'

    def runCorrelator(self):
        
        oldevents=self.dbcontroller.getProcessedEvents()
        newevents=self.dbcontroller.getUnprocessedEvents()
        
        if len(oldevents)==0:
            self.__processEvents(newevents,newevents)
        else:
            self.__processEvents(newevents,newevents)
            self.__processEvents(newevents,oldevents)
        
    def __processEvents(self,events,eventstemp1):
        for i in range(0,len(events)):
            for m in range(0,len(eventstemp1)):
                score=self.correlator.checkEvent(events[i],eventstemp1[m])
                self.dbcontroller.insertLinkedEvents(events[i]['event_id'],eventstemp1[m]['event_id'],score)