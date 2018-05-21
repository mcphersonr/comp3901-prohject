from dbConnections.dbConnections import dbConnection
from dbManagers.wordManager import wordManager
class Where:
    db=dbConnection().getWordConnection()
    cursor=db.cursor()
    where=''
    wordmanager=wordManager()
    whererawtext=[]
    wherepos=0
    locations=[]
    def __init__(self,start,sentencearray):
        self.__createwhere(start,sentencearray)
        if self.where=='No where found':
            possiblelocations=self.__searchforwhere(sentencearray)
            if len(possiblelocations)>0:
                self.__getwherelocations(possiblelocations,sentencearray,start)
        if self.where=='No where found':
            self.__setwherepos(start)
            
    def __getwherelocations(self,possiblelocations,sentencearray,nullvalue):
            self.locations=[]
            for i in range (0,len(possiblelocations)):
                start=possiblelocations[i][1]
                self.__createwhere(start,sentencearray)
                if self.where!='No where found':
                    self.locations.append(self.where)

    def __searchforwhere(self,array):
        wherelocations=[]
        preplist=[i[0] for i in self.wordmanager.getwherewords() if i[1]=='prep']
        for i in range(0,len(array)):
            if array[i][1]=='IN' and array[i][0] in preplist:
                wherelocations.append([array[i],i])
        return wherelocations
    
    def __createwhere(self,start,sentencearray):
        where=[]
        foundwords=[]
        propernouns=[]
        wherenouns=[]
        commonnouns=[]
        locations=[]
        wherepos=0
        wherewords=self.wordmanager.getwherewords()
        for i in range(start,len(sentencearray)):
            if 'NN' in sentencearray[i][1]:
                wherepos=i
                m=i
                try:
                    while 'NN' in sentencearray[m][1]:
                        where.append(sentencearray[m])
                        m+=1
                        wherepos=m
                except:
                    'Error'
                break
            else:
                where.append(sentencearray[i])
        for i in range (0,len(where)):
            if 'NNP' in where[i][1]:
                propernouns.append(where[i][1])
            if 'NN' in where[i][1] and 'NNP' not in where[i][1]:
                commonnouns.append(where[i][0].lower())
            for m in range(0,len(wherewords)):
                if where[i][0].lower()==wherewords[m][0]:
                    foundwords.append(where[i])
                    if wherewords[m][1]=='noun':
                        wherenouns.append(where[i])

        for i in range (0,len(wherenouns)):
            if wherenouns[i][0] not in commonnouns:
                locations.append(wherenouns[i])

        if  len(foundwords)>0:
            if (len(locations)!=0 and len(propernouns)==0 and len(commonnouns)!=0):
                return self.__setwhereinfo(wherepos,where)
            
            if (len(wherenouns)!=0 and len(commonnouns)!=0 and len(locations)!=0)  or (len(wherenouns)!=0 and len(propernouns)!=0):
                return self.__setwhereinfo(wherepos,where)
            else:
                self.__setwherepos(start)
                return self.__setwhere('No where found')
        else:
            self.__setwherepos(start)
            return self.__setwhere('No where found')
            #self.__setwherepos()

    def __setwhereinfo(self,wherepos,where):
        self.__setwherepos(wherepos)
        self.__convertwhere(where)
        
    def __convertwhere(self,array):
        punctuations=[',','.','-']
        newwhere=''
        for i in range(0,len(array)):
            if array[i][0] not in punctuations:
                if i ==0:
                    newwhere=array[i][0]
                else:
                    newwhere+=" "+array[i][0]
        self.__setwhere(newwhere)
        
    def __setwhere(self,fragment):
        self.where=fragment

    def __setwherepos(self,pos):
        self.wherepos=pos
        
    def __setrawtext(self,pos):
        return None

    def getwhere(self):
        return self.where

    def getwherepos(self):
        return self.wherepos
    #def __setwherepos(self):
    #    self.wherepos=0
