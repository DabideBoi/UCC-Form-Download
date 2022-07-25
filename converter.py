import csv


def data_to_csv(latest):
    data = ["CONTROL #", "STUDENT TYPE", "LEVEL APPLIED FOR", 
"STRAND", "SCHOOL YEAR", "REGISTRATION DATE", "LEARNER REFERENCE NUMBER(LRN)",
"SURNAME", "FIRST NAME", "MIDDLE NAME", "BIRTHDATE", "CITIZENSHIP", "RELIGION",
 "PLACE OF BIRTH", "TELEPHONE NO.", "CELLPHONE NO.", "GENDER", "GOOGLE ACCOUNT",
 "HOME ADDRESS", "LAST SCHOOL ATTENDED", "GEN. AVERAGE", "ADDRESS OF LAST SCHOOL ATTENDED",
 "HONORS RECEIVED", "EDUCATION LEVEL", "PAYMENT TYPE", "OCCUPATION", "TOTAL FAMILY MONTHLY INCOME",
 "NUMBER OF SIBLINGS", "GUARDIAN'S NAME", "FAMILY STATUS", "DISCOUNT TYPE", "DOCUMENTS SUBMITTED",
 "Verified for completeness by Registrar:"]

    values = {}
    perma_values = []

    for counter in range(8845, latest):
        #print("Parsing file no. " + str(counter))
        for finder in data:
            f =  open('Files/'+ str(counter) + '.txt')
            a = ' '
            while(a):
                a = f.readline()
                l = a.find(finder)
                if ( l >= 0 ):
                    a = f.readline()
                    if not a.isupper():
                        values[finder] = a.strip()
                    elif a == "GOOGLE ACCOUNT (Gmail)":
                        values[finder] = "N/A"
                    else:
                        values[finder] = "N/A"

                    if finder != "OCCUPATION":
                        break
    perma_values.append(values)
    values = {}

    with open('C:/Users/UCC-IT-Admin/OneDrive - De La Salle University-Dasmariñas/UCCreg22-23.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = data)
        writer.writeheader()
        writer.writerows(perma_values)

def print(string):
    print(string)
