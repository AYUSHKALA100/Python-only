# #okay use dictronary and its methods same for tuple and llist

# restraunt = {
#     "name": "kala ji ka dhaba",
#     "menu": "indian",
#     "price": {"indian":500, "punjabi":300,"south":400},
#     "location":"Dehradun"


# }
# print(restraunt.keys())
# print(restraunt.get("name"))
# print(restraunt.values())
# print(type(restraunt))
# hotel=list(restraunt.items())
# # print(hotel[0])
# for item,value in restraunt.items():
#     print(f"this is your list {item}")
#     price = restraunt[item]
#     print("this is price",price)

# # restraunt.update({"cusinetype":"vegan"})
# # print(restraunt)
# set ={"python","java","python","java","c++","c","javascript"}

# print(len(set))
              

student = {9}
st=list(student)
st.insert(1,9.0)
st=set(st)
new=student.union(st)

print(new)
