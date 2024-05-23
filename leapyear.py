icon = '''
  _                       __     __             
 | |                      \ \   / /             
 | |     ___  __ _ _ __    \ \_/ /__  __ _ _ __ 
 | |    / _ \/ _` | '_ \    \   / _ \/ _` | '__|
 | |___|  __/ (_| | |_) |    | |  __/ (_| | |   
 |______\___|\__,_| .__/     |_|\___|\__,_|_|   
                  | |                           
                  |_|                           

'''
print(icon)

year = int(input('Enter \"Year\" to check \"Leap Year\" or \"not\": '))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"\"{year}\" is leap year.")

elif year % 4 == 0 and year % 100 != 0:
    print(f'\"{year}\" is leap year.')

else:
    print(f'\"{year}\" is not leap year.')