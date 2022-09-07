try:
#    print(x)
#    1/0
#    'x'+1
   pass
except NameError:
   # handle ValueError exception
    print('NameError----------------------------')
except ValueError:
   # handle ValueError exception
    print('ValueError----------------------------')
except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
    print('TypeError or ZeroDivisionError----------------------------')
except:
   # handle all other exceptions
    print('Something went wrong!')
