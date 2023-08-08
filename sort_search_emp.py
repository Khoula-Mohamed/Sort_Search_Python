import pandas as pd
from employee import employee 
#assuming already have data into excel file into a datafram df
df = pd.read_excel('Reading.xlsx', sheet_name='employee')
print("%-20s%-20s%-10s" %("emp id", "Name", "salary"))
print("-"*50)
pList = []
for index, row in df.iterrows():
    eid = row['id']
    name = row['name']
    salary = row['salary']
    
    emp1 = employee(eid,name, salary)
    pList.append(emp1)
    
for e in pList:
    print("%-10i%-20s%-10.2f" %(e.getid(),e.getname(),e.getsalary()))
    
print('====================================')

print('list of employee after sorting the id')
print(df.sort_values('id',ascending=True))

t=df.sort_values('id',ascending=True)

print('+++++++++++++++++++++++++++++++++')
print('Search element')

def binary_search(arr, target):
    arr=list(t.id)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test case
def main():
    ordered_list = t

    target_ID = 55
    result_index = binary_search(ordered_list, target_ID)

    if result_index != -1:
        print(f"ID {target_ID} found at index {result_index}.")
    else:
        print(f"ID {target_ID} not found in the list.")
main()
    

    


