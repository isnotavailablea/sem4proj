import main as ma
import xlsxwriter

dictcopy=ma.maindict.copy()
totalpeople=0
agewt={}
others={}
# print(dictcopy)
# print(ma.maindict)
if __name__=="__main__":
    for key in dictcopy["ageGroups"]:
        totalpeople += dictcopy["ageGroups"][key]["value"]
    for key in dictcopy["ageGroups"]:
        agewt[key] = round(dictcopy["ageGroups"][key]["value"] / totalpeople, 4)
    for keys in dictcopy["ageGroups"]:
        for otherkeys in dictcopy["ageGroups"][keys]["others"]:
            if otherkeys in others:
                others[otherkeys] += dictcopy["ageGroups"][keys]["others"][otherkeys]
            else:
                others[otherkeys] = dictcopy["ageGroups"][keys]["others"][otherkeys]
    for keys in others:
        others[keys] = round(others[keys] / totalpeople, 3)
    l=["agebucket","agewt","ECG-0","ECG-1",
"ang10","ang11",
"ang20","ang21",
"ang30","ang31",
       "Chest_Pain(chronic-1,Acute-2,no-0)-0",
"Chest_Pain(chronic-1,Acute-2,no-0)-1",
"Chest_Pain(chronic-1,Acute-2,no-0)-2",
       "Diabetic-1",
       "Diabetic-0",
       "chol1",
       "chol0",
       "PHF /family history-0",
"PHF /family history-1",
]
    for keys in others:
        print(keys, "=", others[keys])
        # l.append(keys)
    workbook = xlsxwriter.Workbook('zerprodf.xlsx')
    worksheet = workbook.add_worksheet()
    totalrows = 0
    # l.sort()
    for index, i in enumerate(l):
        if i == "agebucket":
            worksheet.write(0, 0, i)
            row = 1
            for keys in agewt:
                worksheet.write(row, 0, keys)
                row += 1
            totalrows = row
        elif i == "agewt":
            worksheet.write(0, 1, i)
            row = 1
            for value in agewt:
                worksheet.write(row, 1, agewt[value])
                row += 1
        else:
            worksheet.write(0, index, i)
            for j in range(1, totalrows):
                worksheet.write(j, index, others[i])

    workbook.close()

# for keys in agewt:
#     print(keys," ",agewt[keys])
# print(totalpeople)