from dbConnections.dbConnections import dbConnection

class caseManager():
    db=dbConnection().getCaseConnection()
    cursor=db.cursor()
    def __init__(self):
        name='Case Manager'
    
    def fetchUnprocessedCases(self):
        casestatements=[]
        casedescription=[]
        casenotes=[]
        
        getcasestatements="Select caselog.case_id, statement_text, statements.statement_id from caselog inner join " 
        getcasestatements+="(Select citizen_statement_add.case_id, statement.statement_id, statement_text from statement join citizen_statement_add on statement.statement_id=citizen_statement_add.statement_id " 
        getcasestatements+="where citizen_statement_add.case_id not in (Select source_id from eventcaselog)) as statements on statements.case_id=caselog.case_id " 
        getcasestatements+="where caselog.case_id not in (Select source_id from eventcaselog) "
        
        getcasedescription="Select case_id,case_description from caselog where case_id not in (Select source_id from eventcaselog)"
        
        getcasenotes="Select caselog.case_id, police_notes,police_notes_id from caselog inner join " 
        getcasenotes+="(Select case_notes.case_id, police_notes.police_notes,police_notes.police_notes_id from police_notes join case_notes on police_notes.police_notes_id=case_notes.police_notes_id "
        getcasenotes+="where case_notes.case_id not in (Select source_id from eventcaselog)) as notes on notes.case_id=caselog.case_id " 
        getcasenotes+="where caselog.case_id not in (Select source_id from eventcaselog) "
        
        self.cursor.execute(getcasestatements)
        statements=self.cursor.fetchall()
        for i in range(0,len(statements)):
            casestatements.append({'source_id':statements[i][0],'statement_id':statements[i][2],'statement':statements[i][1]})
        
        self.cursor.execute(getcasedescription)
        description=self.cursor.fetchall()
        for i in range(0,len(statements)):
            casedescription.append({'case_id':description[i][0],'description':description[i][1]})
        
        self.cursor.execute(getcasenotes)
        notes=self.cursor.fetchall()
        for i in range(0,len(notes)):
            casenotes.append({'source_id':notes[i][0],'notes_id':notes[i][2],'notes':notes[i][1]})
        print (casestatements,casedescription,casenotes)
        return casestatements,casedescription,casenotes
    
    def updateCaseProcessTable(self,caseid):
        neweventcreate="Insert into eventcaselog(source_id) values ('{0}')".format(caseid)
        self.cursor.execute(neweventcreate)
        self.db.commit()
    
    def fetchUnprocessedReports(self):
        logreports=[]
        getreports="Select report_id, report_text from report where report_id not in (Select source_id from eventreportlog)"
        self.cursor.execute(getreports)
        reports=self.cursor.fetchall()
        for i in range(0,len(reports)):
            logreports.append({'source_id':reports[i][0],'report':reports[i][1]})
        return logreports
    
    def updateReportProcessTable(self,reportid):
        neweventcreate="Insert into eventreportlog(source_id) values ('{0}')".format(reportid)
        self.cursor.execute(neweventcreate)
        self.db.commit()
        