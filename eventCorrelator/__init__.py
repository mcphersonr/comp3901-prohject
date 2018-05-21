import correlatorDBManager
from eventCorrelator import eventCorrelator
from correlatorDBManager import correlatorDBManager

def runCorrelator():
    eventsdb=correlatorDBManager()
    oldevents=eventsdb.getProcessedEvents()
    newevents=eventsdb.getUnprocessedEvents()
    
    if len(oldevents)==0:
        processEvents(newevents,newevents)
    else:
        processEvents(newevents,newevents)
        processEvents(newevents,oldevents)
    

def processEvents(events,eventstemp1):
    dbcontroller=correlatorDBManager()
    percentages=dbcontroller.getCorrelatorPercentages()
    correlator=eventCorrelator(percentages)
    for i in range(0,len(events)):
        for m in range(0,len(eventstemp1)):
            score=correlator.checkEvent(events[i],eventstemp1[m])
            dbcontroller.insertLinkedEvents(events[i]['event_id'],eventstemp1[m]['event_id'],score)

runCorrelator()