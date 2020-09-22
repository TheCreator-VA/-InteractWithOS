# Pass a department name and a list of users belonging to that department.
# Return a string as dept: names

def group_list(group, users):
    members = group + ":" +" "
    for user in users:
        members+= user+','
    members = members[:len(members)-1]
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"