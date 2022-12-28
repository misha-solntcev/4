n = int(input())
logins = {}
for i in range(n):
    login = input()
    if login in logins:
        print(f"{login}{logins[login]}")
        logins[login] += 1
    else:
        print("OK")
        logins[login] = 1
