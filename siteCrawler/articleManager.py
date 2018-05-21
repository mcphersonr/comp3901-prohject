from dbConnections.dbConnections import dbConnection

class articlesManager():
    db=dbConnection().getArticleConnection()
    cursor=db.cursor()
    def __init__(self):
        name='Article Manager'
    
    def insertArticles(self,articles):
        for i in range (0,len(articles)):
            self.__addNewArticle(articles[i]['title'],articles[i]['content'],articles[i]['date'],articles[i]['page_url'],)
            
            
    def __addNewArticle(self,title,content,article_date,page_url):
        
        newarticle="Insert into articles(title,content,article_date,page_url) values('{0}','{1}','{2}','{3}')".format(title,content,article_date,page_url)
        print(newarticle)
        self.cursor.execute(newarticle)
        self.db.commit()
    
    def fetchUnprocessedArticles(self):
        getarticles="Select cid, content from articles where cid not in (Select cid from eventarticlelog)"
        self.cursor.execute(getarticles)
        articles=self.cursor.fetchall()
        newarticles=[]
        for i in range(0,len(articles)):
            newarticles.append({'article_id':articles[i][0],'content':articles[i][1]})
        return newarticles
    
    def updateProcessTable(self,cid):
        neweventcreate="Insert into eventarticlelog(cid) values ('{0}')".format(cid)
        self.cursor.execute(neweventcreate)
        self.db.commit()
    
    def getSources(self):
        source_list=[]
        sources="Select source_name, source_page, site_address from sources"
        self.cursor.execute(sources)
        data=self.cursor.fetchall()
        for i in range(0,len(data)):
            source_list.append({'Sitename':data[i][0],'Source_page':data[i][1],'Site Address':data[i][2]})
        return source_list
    