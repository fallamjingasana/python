student_data ={
    "id1":{"name":"jeremy","class":"7","subject": "'math,science"},
        "id2":{"name":"jakson","class":"7","subject": "'math,science"},
            "id3":{"name":"jeremy","class":"7","subject": "'math,science"},
                "id4":{"name":"jack","class":"7","subject": "'math,science"},
}
result = {}
seenkeys = []
for student_id,details in student_data.items():
    uniquekey = (details["name"],details["class"],details["subject"])
    if uniquekey not in seenkeys:
        seenkeys.append(uniquekey)
        result[student_id]=details
for k,v in result.items():
    print(k,":",v)