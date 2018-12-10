from osc import *
from music import * 
from filepicker import pickAFile

oscIn = OscIn( 6448 )

def printMessage(message):    
   address = message.getAddress()
   args    = message.getArguments()
   print "OSC message:", address,         
   for i in range( len(args) ):            
      print args[i],
   print


file=pickAFile()



def playNote(message):
   global file
   f4Note = Note(F4, HN)
   f3Note = Note(F3, HN)
   f2Note = Note(F2, HN)
   args    = message.getArguments()

   isEyesClosed = args[8]
   if(isEyesClosed > 50):
      Play.midi(f4Note) 
      
   
   isBrowRaised = args[2]
   if(isBrowRaised > 50):
      a=AudioSample(file)
      a.play()
      

   isAttentionAway = args[0]   
   if(isAttentionAway < 9):
      Play.midi(f2Note)
 
oscIn.onInput("/.*", playNote)


