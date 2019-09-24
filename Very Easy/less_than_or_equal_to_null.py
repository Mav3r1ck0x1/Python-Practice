

'''def less_than_or_equal_to_zero(num):
    if num <= 0:
        num = True
        print ('True')

    elif num == 'none' or 'None': #hack fix
        num = False
        print ('False')
        return
    else:
        num = False 
        print ('False')
        return



less_than_or_equal_to_zero(5)
less_than_or_equal_to_zero(0)
less_than_or_equal_to_zero(-2)
less_than_or_equal_to_zero('none')'''

def less_than_or_equal_to_zero(num):
   if num <= 0:
      return True
   else:
      return False


less_than_or_equal_to_zero(0)
less_than_or_equal_to_zero(1)
less_than_or_equal_to_zero(-7)
