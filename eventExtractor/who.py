class Who:        
    who=''
    whopos=0
    def __init__(self,sentencearray):
        self.__whocreate(-1,sentencearray)
        if self.getwho()=='No who found':
            self.__whosearch(self.getwhopos(),sentencearray)
   
    def __whosearch(self,start,sentencearray):
        self.__whocreate(start,sentencearray)
                
    def __whocreate(self,start,sentencearray):
        who=[]
        whovalue=[]
        whopos=0
        for i in range (start+1,len(sentencearray)):
            if 'VB' in sentencearray[i][1]:
                whopos=i
                break
            else:
                who.append(sentencearray[i])
        for i in range (0,len(who)):
            if 'NN' in who[i][1] or 'PRP' in who[i][1]:
                whovalue.append(1)   
        if len(whovalue)==0:
            self.__setwho('No who found')
            self.__setwhopos(whopos)
        else:
            self.__setwhopos(whopos)
            self.__convertwho(who)

    def __convertwho(self,array):
        punctuations=[',','.','-']
        newwho=''
        for i in range(0,len(array)):
            if array[i][0] not in punctuations:
                if i ==0:
                    newwho=array[i][0]
                else:
                    newwho+=" "+array[i][0]
        self.__setwho(newwho)     

    def getwho(self):
        return self.who

    def getwhopos(self):
        return self.whopos

    def __setwho(self,fragment):
        self.who=fragment

    def __setwhopos(self,pos):
        self.whopos=pos
