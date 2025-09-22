print("######The followinng are the usernames:######")
for i in range(150):
    if i %3:
        print("carlos")
    else:
        print("wiener")
        
print("########The following are the passwords:########")
with open('passwd.txt', 'r') as f:
    lines = f.readlines()
    

i = 0
for pwd in lines:
    if i %3:
        
        print(pwd.strip('\n'))
    else:
        print("peter")
        print(pwd.strip('\n'))
        i+=1
    i+=1


# print("######The followinng are the usernames:######")
# usernames = []
# for i in range(150):
#     if i % 3:
#         usernames.append("carlos")
#     else:
#         usernames.append("wiener")

# print("########The following are the passwords:########")
# with open('passwd.txt', 'r') as f:
#     lines = f.readlines()

# passwords = []
# i = 0
# for pwd in lines:
#     pwd = pwd.strip('\n')
#     if i % 3:
#         passwords.append(pwd)
#     else:
#         passwords.append("peter")
#         passwords.append(pwd)
#         i += 1
#     i += 1

# # Now combine username + password line by line
# print("\n######Combined Username and Password######")
# for u, p in zip(usernames, passwords):
#     print(f"{u} {p}")


