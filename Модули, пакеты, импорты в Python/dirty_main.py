from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print('start')

calculate_salary()
get_employees()


print(datetime.now())