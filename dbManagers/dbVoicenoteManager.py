from dbConnections.dbConnections import dbConnection

class voiceNoteManager():
    db=dbConnection().getVoiceNoteConnection()
    cursor=db.cursor()
    def __init__(self):
        name='VoiceNote Manager'
    
    def fetchUnprocessedVoicenote(self):
        getvoicenotes="Select voicenote_id, voicenote_text from voicenote where voicenote_id not in (Select voicenote_id from event_voicenote_log)"
        self.cursor.execute(getvoicenotes)
        voicenotes=self.cursor.fetchall()
        vnotes=[]
        for i in range(0,len(voicenotes)):
            vnotes.append({'voicenote_id':voicenotes[i][0],'voicenote_text':voicenotes[i][1]})
        return vnotes
    
    def updateProcessTable(self,vid):
        neweventcreate="Insert into event_voicenote_log(voice_note_id) values ('{0}')".format(vid)
        self.cursor.execute(neweventcreate)
        self.db.commit()
    