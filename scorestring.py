import treeimpl
import json
sd=treeimpl.scoredict.copy()
scorestring={

}
agenum={
    "26-30":0,
    "31-35":1,
    "36-40":2,
    "41-45":3,
    "46-50":4,
    "51-55":5,
    "56-60":6,
    "61-65":7,
    "66-70":8,
    "71-75":9,
    "76-80":'a',
    "81-85":'b',
    "86-90":'c'
}
for string in sd:
    if string=="" or string==" ":
        continue
    print(string)
    l=string.split("->")
    strin=str(agenum[l[0]])
    for i in range(1,len(l)):
        if l[i]=="" or l[i]==" ":
            continue
        print(l[i])
        strin+=l[i][len(l[i])-1]
    scorestring[strin]=sd[string]
    print(strin," ",scorestring[strin])

json_object = json.dumps(scorestring, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
