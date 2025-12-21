employees = [
    {"id": 101, "name": "Amit",    "department": "HR",        "salary": 42000},
    {"id": 102, "name": "Neha",    "department": "IT",        "salary": 75000},
    {"id": 103, "name": "Ravi",    "department": "Finance",   "salary": 68000},
    {"id": 104, "name": "Priya",   "department": "Marketing", "salary": 50000},
    {"id": 105, "name": "Karan",   "department": "IT",        "salary": 90000},
    {"id": 106, "name": "Sneha",   "department": "HR",        "salary": 46000},
    {"id": 107, "name": "Arjun",   "department": "Finance",   "salary": 82000},
    {"id": 108, "name": "Meena",   "department": "Support",   "salary": 38000},
    {"id": 109, "name": "Rahul",   "department": "Marketing", "salary": 61000},
    {"id": 110, "name": "Anjali",  "department": "IT",        "salary": 72000}
]

def sort_emp(employee):
    return sorted(employee,key=lambda employee : employee['salary'])

sorted_emp = sort_emp(employees)

