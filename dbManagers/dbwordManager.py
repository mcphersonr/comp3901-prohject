from dbConnections.dbConnections import dbConnection
class wordManager:
    keywords=[]
    whenwords=[]
    wherewords=[]
    db=dbConnection().getWordConnection()
    cursor=db.cursor()
    tabletoevent={'where':'wherecount','when':'whencount','what':'whatcount','who':'whocount'}
    
    def __init__(self):
        self.__loadKeywords()
        self.__loadWords()

    def eventWordCount(self,sentence,event):
        eventpart=self.tabletoevent[event]
        array=sentence.lower().split(' ')
        partition=len(array)//2
        self.__countword(array[0:partition],eventpart)
        self.__countword(array[partition:],eventpart)

    def __countword(self,array,eventpart):
        for i in range (0,len(array)):
            self.__updateWordCount(array[i],eventpart)

    def __updateWordCount(self,word,eventpart):
        totalcountupdate="update word set word.count=word.count+1 where word='"+word+"'"
        partcountupdate="update wordpartscount set wordpartscount."+eventpart+"=wordpartscount."+eventpart+"+1 where word='"+word+"'"
        wordcheck="Select word from word where word='"+word+"'"
        self.cursor.execute(wordcheck)
        data=self.cursor.fetchall()
        try:
            if len(data)>0:
                self.cursor.execute(totalcountupdate);
                self.cursor.execute(partcountupdate);
                self.db.commit();
            else:
                insertword="insert into word(word,count) values('"+word+"',1)"
                insertwordpart="insert into wordpartscount (word,"+eventpart+") values ('"+word+"',1)"
                self.cursor.execute(insertword)
                self.cursor.execute(insertwordpart)
                self.db.commit()
        except:
            'Error'

    def getWordAvg(self):
       avg ="Select 'Current Average', FORMAT(sum(count)/count(word),0) as avg from word"
       self.cursor.execute(avg)
       wordavg=self.cursor.fetchall()[0][1]
       return wordavg

    def checkavg(self):
        avg="Select word.word,word.count from word where word.word not in (Select keywords.keyword from keywords) and "
        avg+="(word.count BETWEEN (Select keyword_avg.avg_figure FROM keyword_avg where avg_description='Current') and "
        avg+="(Select keyword_avg.avg_figure FROM keyword_avg where avg_description='Current')*1.15) or "
        avg+="(word.count BETWEEN (Select keyword_avg.avg_figure FROM keyword_avg where avg_description='Previous') and "
        avg+="(Select keyword_avg.avg_figure FROM keyword_avg where avg_description='Current')) " 

        try:
            self.cursor.execute(avg)
            possible_keyswords=this

        except:
            'Error'

    def __loadKeywords(self):
        sql='Select keyword from keywords'
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            for i in range (0,len(data)):
                self.keywords.append(data[i])
        except:
            'Error'
    
    def __loadWords(self):
        where='Select word,pos from wherewords'
        when='Select word,whenpart from whenwords'
        try:
            self.cursor.execute(where)
            wherewords=self.cursor.fetchall()
            for i in range (0,len(wherewords)):
                self.wherewords.append(wherewords[i])
                
            self.cursor.execute(when)
            whenwords=self.cursor.fetchall()
            for i in range (0,len(whenwords)):
                self.whenwords.append(whenwords[i])
        except:
            'Error'
                
    
    def reloadKeywords(self):
        self.__loadKeywords()

    def getKeywords(self):
        return self.keywords 
        
    def getwherewords(self):
        return self.wherewords
    
    def getwhenwords(self):
        return self.whenwords
