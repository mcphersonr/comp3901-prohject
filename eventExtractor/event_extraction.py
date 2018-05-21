from eventExtractor.eventCreator import eventCreator
from dbManagers.dbwordManager import wordManager
from eventExtractor.eventDBManger import eventDBManager
#things left to do:
#figure what to do with remaining portions of the sentence
#how to break sentences without punctuations


a="A 25 year-old male was shot and injured Thursday night in the Willowdene area of St. Catherine. "
a+="Reports from the Spanish Town police are that the young man was walking along Willowdene Drive towards Old Harbour Road where he was approached by two men. "
a+="One of the men brandished a gun demanded his cellular phone and cash. A tussle ensued and the man was shot."
a+="He was then robbed of his phone, an undetermined amount of cash and personal documents."
a+="The robbers escaped, the victim was taken to the spanish Town hospital. Up to press time, his condition could not be ascertained, but the police are investigating."

first=eventCreator(a)
dbcreator=eventDBManager()
dbcreator.insertEvents(first.getEvents(),'source',1515)



#print(first.getevents(),'\n')

#second=event_creator.EventCreator(b)
#print(second.getevents(),'\n')


#third=event_creator.EventCreator(c)
#print(third.getevents(),'\n')


#fourth=event_creator.EventCreator(d)
#print(fourth.getevents(),'\n')

#print(fourth.getevents(),'\n')

