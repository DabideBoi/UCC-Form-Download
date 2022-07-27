def clean():
    with open('temp.csv', 'r') as in_file, open('C:/Users/UCC-IT-Admin/OneDrive - De La Salle University-Dasmariñas/UCCreg22-23.csv', 'w') as out_file:
        seen = set()
        for line in in_file:
            if line in seen: continue # skip duplicates
            if line == '': continue #skip blanks
            print(line)
            seen.add(line)
            out_file.write(line)