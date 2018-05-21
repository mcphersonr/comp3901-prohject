import nltk
from who import Who
from what import What
from when import When
from where import Where
from nltk.tokenize import word_tokenize


class eventCreator:
    def __init__(self):
        name='Event Creator'
    
    def getSentenceEvents(self,paragraph):
        events=[]
        sentences=self.__breakParagraph(paragraph)
        for i in range(0,len(sentences)):
            self.__createEvent(sentences[i],events)
        return events

    def __createEvent(self,sentence,events):
        tokensentences=self.__tagWords(sentence)
        whotemp=Who(tokensentences)
        whattemp=What(tokensentences,whotemp.getwhopos())
        whentemp=When(tokensentences)
        wheretemp=Where(whattemp.getwhatpos(),tokensentences)
        event={'who':whotemp.getwho(),'what':whattemp.getwhat(),'when':whentemp.getwhen(),'where':wheretemp.getwhere()}
        if whotemp.getwho()!='No who found' and whattemp.getwhat()!='No what found':
            events.append(event)
            
    def __tagWords(self,sentence):
        text=word_tokenize(sentence)
        return nltk.pos_tag(text)

    def __breakParagraph(self,paragraph):
        #list of abbreviations that would break the sentnce
        abbrev=['St.',' Mr.','Dr.']
        remove=paragraph.split(' ')
        for i in range(0,len(abbrev)):
            for m in range (0,len(remove)):
                if abbrev[i]==remove[m]:
                    remove[m]=abbrev[i][0:len(abbrev[i])-1]


        paragraph= ' '.join(str(e) for e in remove)
    
        #Goes through and find the punctuations and their position in the sentence
        punctfound=[]
        punctuations=['!','?','.']
        for i in range (0,len(punctuations)):
            for m in range (0,len(paragraph)):
                if paragraph[m]==punctuations[i]:
                    punctfound.append((punctuations[i],m))
        if len(punctfound) > 1:
            sortedpuncfound=sorted(punctfound,key=lambda index:index[1])
            number=len(sortedpuncfound)    
            sentences=[]
            pos1=0
            pos2=sortedpuncfound[0][1]
            sentences.append(paragraph[pos1:pos2])
            pos1=pos2+1
            pos2=sortedpuncfound[1][1]
            sentences.append(paragraph[pos1:pos2])
            for i in range(1,len(sortedpuncfound)-1):
                if i == (number-2):
                    pos1=sortedpuncfound[number-2][1]+1
                    pos2=sortedpuncfound[number-1][1]
                else:
                    pos1=sortedpuncfound[i][1]+1
                    pos2=sortedpuncfound[(i+1)][1]
                sentences.append(paragraph[pos1:pos2])
            return sentences
        if len(punctfound)==1:
            sentences=paragraph.split(punctfound[0][0])
            return sentences
        else:
            return [paragraph]
