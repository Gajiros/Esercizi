import math

#1.
def safe_sqrt(number: int) -> float:
    if (number >= 0):
        return math.sqrt(number)
    else:
        raise Exception('The number is negative, it has to be positive.')

#2.
class InvalidPasswordError(Exception):
    'Invalid password.'

def validate_password(password: str):

    count_spec_char: int = 0
    count_cap_char: int = 0
    special_char: str = '-_.:,;#§+*][^\'?=]/&%$£"!)('

    for char in password:
        if (char.isupper() == True):
            count_cap_char += 1
        if (char in special_char):
            count_spec_char += 1
    if (len(password) >= 20) and (count_cap_char >= 3) and (count_spec_char >= 4):
        print('The password is valid.')
    else:
        raise InvalidPasswordError

#3
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except IOError as e:
            print(f"Error opening file: {e}")
            self.file = None
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            try:
                self.file.close()
            except IOError as e:
                print(f"Error closing file: {e}")

#4
class Date:

    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year
    
    def getDate(self):
        full_date: str = f'{self.day}.{self.month}.{self.year}'
        return full_date

class Database:

    def __init__(self) -> None:
        self.dates = []
    
    def addDate(self, date: Date):
        self.dates.append(date)
        print(f'You added this date: {date.getDate}')
    
    def deleteDate(self, date: Date):
        print(f'You removed this date: {date.getDate}')
        self.dates.remove(date)
    
    def modifyDate(self, date: Date):
        flag = True
        oldDate: str = date.getDate
        while (flag == True):

            choice: int = input('you want to modify the day, the month or the year? Type 1, 2 or 3: ')
            if (choice == 1):
                date.day = input('Type the new day: ')
            elif (choice == 2):
                date.month = input('Type the new month: ')
            elif (choice == 3):
                date.year = input('Type the new year: ')
            
            again: str = input('Do you want to change something else? Type y or n: ')
            if (again == 'y'):
                continue
            elif (again == 'n'):
                flag = False
                print(f'You modified the date from {oldDate} to {date.getDate}.')

#date: Date = Date(30,5,2004)
#database: Database = Database()
#database.addDate(date)
#database.modifyDate(date)