import csv
import pinger
import cleaner

def data_to_csv(latest, last):
    data = ["CONTROL #", "STUDENT TYPE", "LEVEL APPLIED FOR", 
"STRAND", "SCHOOL YEAR", "REGISTRATION DATE", "LEARNER REFERENCE NUMBER(LRN)",
"SURNAME", "FIRST NAME", "MIDDLE NAME", "BIRTHDATE", "CITIZENSHIP", "RELIGION",
 "PLACE OF BIRTH", "TELEPHONE NO.", "CELLPHONE NO.", "GENDER", "GOOGLE ACCOUNT",
 "HOME ADDRESS", "LAST SCHOOL ATTENDED", "GEN. AVERAGE", "ADDRESS OF LAST SCHOOL ATTENDED",
 "HONORS RECEIVED", "EDUCATION LEVEL", "PAYMENT TYPE", "OCCUPATION", "TOTAL FAMILY MONTHLY INCOME",
 "NUMBER OF SIBLINGS", "GUARDIAN'S NAME", "FAMILY STATUS", "DISCOUNT TYPE", "DOCUMENTS SUBMITTED",
 "Verified for completeness by Registrar:"]
    check = ["CONTROL #", "STUDENT TYPE", "LEVEL APPLIED FOR", 
"STRAND", "SCHOOL YEAR", "REGISTRATION DATE", "LEARNER REFERENCE NUMBER(LRN)",
"SURNAME", "FIRST NAME", "MIDDLE NAME", "BIRTHDATE", "CITIZENSHIP", "RELIGION",
 "PLACE OF BIRTH", "TELEPHONE NO.", "CELLPHONE NO.", "GENDER", "GOOGLE ACCOUNT (Gmail)",
 "HOME ADDRESS", "LAST SCHOOL ATTENDED", "GEN. AVERAGE", "ADDRESS OF LAST SCHOOL ATTENDED ",
 "HONORS RECEIVED", "EDUCATION LEVEL", "PAYMENT TYPE", "OCCUPATION", "TOTAL FAMILY MONTHLY INCOME",
 "NUMBER OF SIBLINGS", "GUARDIAN'S NAME", "FAMILY STATUS", "DISCOUNT TYPE", "DOCUMENTS SUBMITTED",
 "Verified for completeness by Registrar:"]

    values = {}
    perma_values = []
    cnt = 0
    for counter in range(last, latest):
        print("Parsing file no. " + str(counter))
        for finder in data:
            f =  open('Files/'+ str(counter) + '.txt')
            a = ' '
            while(a):
                a = f.readline()
                l = a.find(finder)
                if ( l >= 0 ):
                    a = f.readline()
                    if cnt < 9:
                        if not a.isupper():
                            values[finder] = a.strip()
                        elif a == "GOOGLE ACCOUNT (Gmail)":
                            values[finder] = "N/A"
                        else:
                            values[finder] = "N/A"

                        if finder != "OCCUPATION":
                            break
                    else:
                        if a not in data:
                            values[finder] = a.strip()
                        elif a == "GOOGLE ACCOUNT (Gmail)":
                            values[finder] = "N/A"
                        else:
                            values[finder] = "N/A"

                        if finder != "OCCUPATION":
                            break
        print("Appending...")
        perma_values.append(values)
        values = {}

    with open('temp.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = data)
        writer.writeheader()
        writer.writerows(perma_values)
    cnt = cnt + 1

#when things go wrong use this hahhahahahaha
#data_to_csv(11111, 8845)
#cleaner.clean()