import json
import time

print("--------------------------------------")
print("PLEASE SETUP THE CONFIG IF YOU HAVENT!")
print("--------------------------------------")

time.sleep(1)

with open("cfg/config.txt") as configFile:
    data = configFile.read()
    mailProviders = data.split(":")[1]
    thread = data.split(":")[4]
    keywords = data.split(":")[3]
    with open(keywords) as keys:
        lines = keys.readlines()
    with open(mailProviders) as mailFile:
        mails = mailFile.readlines()
        for line in lines:
            line = line.replace("\n", "")
            for mail in mails:
                mail = mail.replace("\n", "")
                keyword = line + "@" + mail
                print(keyword)
                with open("output.txt", "a") as file:
                    file.writelines(keyword + "\n")