student_name = input("enter name: ")

st_map = {}

while student_name != "!":
    point = float(input("enter point: "))

    if student_name in st_map.keys():
        st_map[student_name]["total"] = st_map[student_name]["total"] + point
        st_map[student_name]["cnt"] = st_map[student_name]["cnt"] + 1
    else:
        st_map[student_name] = {}
        st_map[student_name]["total"] = point
        st_map[student_name]["cnt"] = 1

    student_name = input("enter name: ")

for k, v in st_map.items():
    st_map[k]["avg"] = v["total"] / v["cnt"]

mx_avg = 0
max_st_name = ""
for k, v in st_map.items():
    if v["avg"] > mx_avg:
        mx_avg = v["avg"]
        max_st_name = k

print("max gpa has student", max_st_name, "gpa:", mx_avg)
