class What:
    what=''
    whatpos=0
    def __init__(self,sentencearray,start):
        self.__whatcreate(sentencearray,start)
        
    def __whatcreate(self,sentencearray,start):
        what=[]
        whatvalue=[];
        whatpos=0
        for i in range (start,len(sentencearray)):
            if 'NN' in sentencearray[i][1]:
                whatpos=i
                m=i
                try:
                    while 'NN' in sentencearray[m][1] or 'PR' in sentencearray[m][1]:
                        what.append(sentencearray[m])
                        m+=1
                        whatpos=m
                except:
                    'Error'
                v=whatpos
                try:
                    while 'VB' in sentencearray[v][1]:
                        what.append(sentencearray[v])
                        v+=1
                        whatpos=v
                    if sentencearray[whatpos][1]=='JJ':
                        what.append(sentencearray[whatpos])
                except:
                    'Error'
                break
            else:
                what.append(sentencearray[i])
        for i in range (0,len(what)):
            if 'VB' in what[i][1]:
                whatvalue.append(1)
        if len(whatvalue)==0:
            self.__setwhat('No what found')
            self.__setwhatpos(whatpos)
        else:
            self.__setwhatpos(whatpos)
            self.__convertwhat(what)
            
    def __convertwhat(self,array):
        punctuations=[',','.','-']
        newwhat=''
        for i in range(0,len(array)):
            if array[i][0] not in punctuations:
                if i ==0:
                    newwhat=array[i][0]
                else:
                    newwhat+=" "+array[i][0]
        self.__setwhat(newwhat)

    def getwhat(self):
        return self.what
    
    def getwhatpos(self):
        return self.whatpos
    
    def __setwhat(self,fragment):
        self.what=fragment
        
    def __setwhatpos(self,pos):
        self.whatpos=pos
    
    def addtowhat(self,array):
        temp=self.getwhat()+' '+self.__convertwhat(array)
        self.__setwhat(temp)
        
        
        
