score = input ('Score:')
try :
    grade = float (score)
    if grade > 1 :
        print ( ' Out of Range')
    elif grade >= 0.9 :
        print ('A')
    elif grade >= 0.8 :
        print ('B')
    elif grade >= 0.7:
        print ('C')
    elif grade >= 0.6 :
        print ('D')
    elif grade < 0.6 :
        print ('F')
    elif grade < 0 :
        print ( ' Out of Range')            
except: 
    print (' enter a number between 1 and 0')

