from __future__ import division
import nltk
from nltk.tokenize import word_tokenize
from dbManagers.dbwordManager import wordManager

class eventCorrelator:
    percentages={}
    
    def __init__(self,percentages):
        name='Event Correlator'
        self.percentages=percentages
    
    def checkEvent(self,event1,event2):
        who=self.__checkWho(event1['who'],event2['who'])
        what=self.__checkWhat(event1['what'],event2['what'])
        where=self.__checkWhere(event1['where'],event2['where'])
        when=self.__checkwhen(event1['when'],event2['when'])
        correlation=(who+what+when+where)
        return correlation
    
    def __checkWho(self,who1,who2):
    	if (len(who1)==0 or len(who2)==0):
    		return 0
    	else:
    		nounratio=0
    		adjratio=0
	    	noun=85
	    	adj=15
	    	whotemp1=self.__tagwords(who1)
	    	whotemp2=self.__tagwords(who2)
	    	firstnouns=[x[0] for x in whotemp1 if 'NN' in x[1]]
	    	secondnouns=[x[0] for x in whotemp2 if 'NN'  in x[1]]
	    	nounmatch=self.__checkcounter(firstnouns,secondnouns)
	    	nouncount=len(firstnouns)+len(secondnouns)
	    	nounratio=self.__calculateRatio(nounmatch,nouncount,noun)
	    	firstadjs=[x[0] for x in whotemp1 if 'JJ' in x[1]]
	    	secondadjs=[x[0] for x in whotemp2 if 'JJ'  in x[1]]
	    	adjmatch=self.__checkcounter(firstadjs,secondadjs)
	    	adjcount=len(firstadjs)+len(secondadjs)
	    	adjratio=self.__calculateRatio(adjmatch,adjcount,adj)
	    	return (nounratio+adjratio )/(noun+adj) * self.percentages['who']
    
    def __checkWhat(self,what1,what2):
    	if len(what1)==0 or len(what2)==0:
    		return 0
    	else:
	    	verb=70
	    	noun=30
	    	whattemp1=self.__tagwords(what1)
	    	whattemp2=self.__tagwords(what2)
	    	firstverbs=[x[0] for x in whattemp1 if 'NN' in x[1]]
	    	secondverbs=[x[0] for x in whattemp2 if 'NN'  in x[1]]
	    	verbmatch=self.__checkcounter(firstverbs,secondverbs)
	    	verbcount=len(firstverbs)+len(secondverbs)
	    	verbratio=self.__calculateRatio(verbmatch,verbcount,verb) 
	    	firstnouns=[x[0] for x in whattemp1 if 'JJ' in x[1]]
	    	secondnouns=[x[0] for x in whattemp2 if 'JJ'  in x[1]]
	    	nounmatch=self.__checkcounter(firstnouns,secondnouns)
	    	nouncount=len(firstnouns)+len(secondnouns)
	    	nounratio=self.__calculateRatio(nounmatch,nouncount,noun)
	    	return (nounratio+verbratio)/(verb+noun) * self.percentages['what']
    
    def __checkWhere(self,where1,where2):
        if (where1==None or where2==None):
            return 0
        else:
            wherewords=[x[0] for x in wordManager().getwherewords() if x[1]=='noun']
            wheretemp1=self.__tagwords(where1)
            wheretemp2=self.__tagwords(where2)
            firstnouns=[x[0] for x in wheretemp1 if 'NN' in x[1] and x[0].lower() not in wherewords]
            secondnouns=[x[0] for x in wheretemp2 if 'NN'  in x[1] and x[0].lower() not in wherewords]
            nounmatch=self.__checkcounter(firstnouns,secondnouns)
            nouncount=len(firstnouns)+len(secondnouns)
            nounratio=self.__calculateRatio(nounmatch,nouncount,1)*self.percentages['where']
            return nounratio
        
            
    def __checkwhen(self,when1,when2):
    	if len(when1)==0 or len(when2)==0:
    		return 0
    	else:
    		dayvalue=0
    		datevalue=self.__checkdate(when1['date'],when2['date'])
    		if datevalue == 0:
    			dayvalue=self.__checkday(when1['day'],when2['day'])
    		timevalue=self.__checktime(when1['time'],when2['time'])
    		corrlation=(dayvalue,datevalue,timevalue)
    		if dayvalue+datevalue+timevalue==0:
    		    return 0
    		else:
    		    return (dayvalue+datevalue+timevalue)/(dayvalue+datevalue+timevalue)*self.percentages['when']
    
    def __checkdate(self,date1,date2):
    	if date1==None or date2==None:
    		return 0
    	if date1==date2:
    		return 85
    	if date1!=date2:
    	    return 0
    
    def __checktime(self,time1,time2):
    	if time1==None or time2==None:
    		return 0
    	else:
    		if time1==time2:
    			return 25
    		return 0
    
    def __checkday(self,day1,day2):
   		whenwords=[x[0].lower() for x in wordManager().getwhenwords() if x[1]=='day']
   		if day1==None or day2==None:
   			return 0
   		else:
   			daytemp1=day1.split(' ')
   			daytemp2=day2.split(' ')
   			day1test=[x for x in daytemp1 if x.lower() in whenwords]
   			day2test=[x for x in daytemp2 if x.lower() in whenwords]
   			count=self.__checkcounter(day1test,day2test)
   			if count > 0:
   				return 15
   			else:
   				return 0
    
    def __calculateRatio(self,intersect,total,value):
        if total-intersect==0:
            return value
        else:
            return intersect/(total-intersect)* value
            
    def __tagwords(self,sentence):
        text=word_tokenize(sentence)
        return nltk.pos_tag(text)
        
    def __checkcounter(self,list1,list2):
        count=0
        if len(list1)==0 or len (list2)==0:
            return 0
        else:
            if len(list1) < len(list2):
                temp=list2
                list2=list1
                list1=temp
            for i in range (0,len(list1)):
                for m in range(0,len(list2)):
                    if list1[i].lower()==list2[m].lower():
                        count+=1
            return count
            