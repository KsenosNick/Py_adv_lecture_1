from datetime import datetime

from db.people import get_employees
from application.salary import calculate_salary

def main():
    date = datetime.date(datetime.today())
    print(date)
    employee = get_employees()
    salary = calculate_salary(employee)
    print(salary)


if __name__ == '__main__':
    main()
