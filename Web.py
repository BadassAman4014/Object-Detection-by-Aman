import pyttsx3

engine = pyttsx3.Engine()
engine.setProperty( "rate", 200 )
engine.setProperty( "volume", 1.0 )
engine.say( 'say something' )
engine.runAndWait()

with open( 'combo.py', mode='rt') as files:
    lines = files.readlines()

lines = [ x.strip(' ') for x in lines ] # remove un-necessary spaces
lines = [ x for x in lines if x!='\n'] # remove empty lines

for a in lines:
    print( a, end ='' )
    engine.say( a )
    engine.runAndWait()