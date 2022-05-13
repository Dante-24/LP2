from nltk.stem import *

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def problem():
    print('BOT --> If you are facing some issues while booking, please visit www.irc/troubleshoot')
def fullbooking():
    print('BOT --> We are sorry! The booking is full')
def timetable():
    print('BOT --> To check the timetable, visit www.irdc/timetable')
def price():
    print('BOT --> Cost : 400 rs for adults\n\t 250 rs for children')
def cancel():
    print('BOT --> To cancel your booking, visit www.irdc/cancelbooking')
def availableslots():
    print('BOT --> Visit www.irdc/avl to check available slots')
def FAQ():
    print('for your other queries, visit www.irdc/faq')
print('BOT --> Hello! How can I help you?')
resp=1
print(ps)
while(resp!=0):
    s=input("USER --> enter text : ")
    arr=s.split(' ')
    flag=0
    #print(arr)
    for i in range(len(arr)):
        if(flag==1):
            continue
        stemmed=ps.stem(arr[i])
        if(stemmed=='can i' or stemmed=='how' or stemmed=='able to' or stemmed=='where' or stemmed=='when'):
            FAQ() 
            flag=1
        elif(stemmed=='cancel'):
            cancel()
            flag=1
        elif(stemmed=='issu' or stemmed=='difficulti' or stemmed=='error' or stemmed=='troubl' or stemmed=='problem'):
            problem()
            flag=1
        elif(stemmed=='avail' or stemmed=='slot' or stemmed=='book'):
            availableslots()
            flag=1
        elif(stemmed=='price' or stemmed=='money' or stemmed=='cost'):
            price()
            flag=1
        
        elif(stemmed=='timet'):
            timetable()
            flag=1
        elif(stemmed=='not avail' or stemmed=='full'):
            fullbooking()
            flag=1
        
    resp=int(input("BOT --> If you want to end the conversation, type 0, else type 1 \n"))

