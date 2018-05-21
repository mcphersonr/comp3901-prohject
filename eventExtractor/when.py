from dbConnections.dbConnections import dbConnection
from dbManagers.wordManager import wordManager
class When:
    whenwords=[]
    db=dbConnection().getWordConnection()
    cursor=db.cursor()
    wordmanager=wordManager()
    dateparts=[]
    
    def __init__(self,sentencearray):
        self.dateparts=[]
        self.__setwords()
        self.__createwhen(sentencearray)
    
    def __createwhen(self,sentence):
        for i in range(0,len(sentence)):
            for m in range(0,len(self.whenwords)):
                if self.whenwords[m][0] in sentence[i][0]:
                    part=self.__extractwhenpart(self.whenwords[m],sentence,i)
                    self.__addwhenparts(part)
    
    def getwhen(self):
        if len(self.dateparts)==0:
            return 'No when found'
        else:
            return self.dateparts

    def __extractwhenpart(self,whenword,sentence,pos):
        if whenword[1]=='time':
            return self.__timetest(sentence,pos)
        if whenword[1]=='day':
            if whenword[0]=='day' and whenword[0]!=sentence[pos][0].lower():
                return None
            else:
                return self.__daytest(sentence,pos)
        if whenword[1]=='date':
            return self.__datetest(sentence,pos)
        
    def __daytest(self,sentence,index):
        partsofspeech=sentence[index-1][1]
        partsofspeech2=sentence[index+1][1]
        partsofspeech3=sentence[index-2][1]
        if 'IN' in partsofspeech3 and sentence[index].lower()=='day':
            daypart={'day':sentence[index-1][0]+' '+sentence[index][0]}
            return daypart
        if 'NN' in partsofspeech2:
            daypart={'day':sentence[index][0]+' '+sentence[index+1][0]}
            return daypart
        if 'JJ' in partsofspeech or 'NN' in partsofspeech and 'IN' not in partsofspeech:
            daypart={'day':sentence[index-1][0]+' '+sentence[index][0]}
            return daypart
        else:
            daypart={'day':sentence[index][0]}
            return daypart

    def __datetest(self,sentence,index):
        try:
            part1=sentence[index+1][1]
            part2=sentence[index+2][1]
            part3=sentence[index+3][1]

            if part1=='CD' and ((part3=='CD' and part2==',') or (part2=='CD')):
                if part2==',':
                    datepart={'date':sentence[index][0]+" "+sentence[index+1][0]+", "+sentence[index+3][0]}
                    return datepart
                else:
                    datepart={'date':sentence[index][0]+" "+sentence[index+1][0]+", "+sentence[index+2][0]}
                    return datepart 
        except:
            'Error'

    def __timetest(self,sentence,index):
        a=sentence[index-1][0]
        try:
            m=a.index(':')
            if m>0 and sentence[index-1][1]=='CD':
                time={'time':sentence[index-1][0]+" "+sentence[index][0]}
                return time
        except:
            if sentence[index-1][1]=='CD':
                time={'time':sentence[index-1][0]+" "+sentence[index][0]}
                return time

    def __addwhenparts(self,when):
        if when==None or when in self.dateparts:
            'Nothing'
        else:
            self.dateparts.append(when)
            
    def __setwords(self):
        self.whenwords=self.wordmanager.getwhenwords()

