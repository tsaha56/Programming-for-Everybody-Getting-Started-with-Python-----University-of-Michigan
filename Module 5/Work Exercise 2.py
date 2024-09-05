x1 = input ('Enter Hours:')
try:
    x2 = float (x1)
    y1 = input ('Enter rate:')
    try :
        y2 = float (y1)
        if x2 < 40:
            z = float ( x2 * y2)
            print ( "pay: ", z)
        else :
            z = float ( x2 * y2 * 1.5)
            print ( 'Pay:', z )
    except: 
        print ('Error, please enter numeric input')
except:
    print ('Error, please enter numeric input')