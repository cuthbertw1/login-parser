#! /usr/bin/python3
import csv
def readFile():
    file=open("employee_logins.csv","r")
    logins=csv.reader(file)
    counter=0
    for row in logins:             # prints out all the data in the employee_logins file
        print(row)
        counter+=1
    print(str(counter)+" original entries")

def newFile():
    header=['Name', 'First IP address','login_count','login_count_excess']          # file handling and formatting inits
    file = open("employee_logins.csv", "r")
    logins = csv.reader(file)
    newFile = open("cuthbertw1.csv", "w")
    csvwriter=csv.writer(newFile)
    csvwriter.writerow(header)
    next(logins)            # prevents header from being read in
    counter=0
    print("{:<20} {:<15} {:<15} {:<15}".format("Name", "First IP", "Total Logins","Login Excess"))  # Header for the output
    print("-" * 70)  # Line separator
    for row in logins:        # reading from employee_logins.csv file

        if int(row[3])>=200 or "i" in row[1] or "e" in row[1] :    # if logins exceed 200 or last name contains i or e
            totalLogins=row[3]
            IPs=row[4].split(';')
            firstIP=IPs[0]
            name=row[0]+" "+row[1]
            loginExcess=int(row[3])-200
            print("{:<20} {:<15} {:<15} {:<15}".format(name, firstIP, totalLogins, loginExcess))   # prints the information as it is read in
            rewrite = [name, firstIP, totalLogins,loginExcess]    #writes the same data to the new file
            csvwriter.writerow(rewrite)
            counter += 1                    # tracks the number of suspicous logins
    print(str(counter)+" suspicious logins")



def main():
    readFile()

    newFile()
    #footer
    print("------------------------------------------------------------")
main()