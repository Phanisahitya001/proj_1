import csv

def write_into_csv(data_list):
    with open('emp_data.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["name","emp_id","contact_no"])
        writer.writerow(data_list)

if __name__=='__main__':
    condition=True
    emp_num=1
    while(condition):
        emp_data=input("enter employee data for employee #{} in the following format(name emp_id contact_no):".format(emp_num))
        emp_list=emp_data.split(' ')
        print("\nThe entered data is -\nname: {}\nemp_id: {}\ncontact_num: {}".format(emp_list[0],emp_list[1],emp_list[2]))
        choice_check=input("Is the data correct? (y/n): ")
        if choice_check=="y":
            write_into_csv(emp_list)

            condition_check=input("enter (y/n) for another emp data entry: ")
            if condition_check=="y":
                condition=True
                emp_num= emp_num+1
            elif condition_check=="n":
                condition=False
        elif choice_check=="no":
            print("Please re-enter the data")
