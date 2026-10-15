# Password Vault
import json
from getpass import getpass

class PasswordManager:
    def __init__(self):
        self.pass_list = self.load_passwords()
        self.actions = {
                "1": self.add_password,
                "2": self.show_passwords,
                "3": self.search_password,
                "4": self.delete_password,
                "5": self.edit_password
            }
        
    def load_passwords(self):
        try:
            with open("pass.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []      
          
    def save_passwords(self):
        with open("pass.json", "w") as file:
            json.dump(self.pass_list, file, indent=4)

    def add_password(self):
        print("adding password")
        website = input("your website: ").strip()
        username = input("your username: ").strip()
        password = input("your password: ").strip()
        if not password:
            print("password cannot be empty.")
            return
        elif not username:
            print("username cannot be empty.")
            return
        elif not website:
            print("website cannot be empty.")
            return
        else:
            self.pass_list.append({"password": password,
                                   "username": username,
                                   "website": website})
            self.save_passwords()
            print("Password saved successfully.")
  
    def show_passwords(self):
        print("showing passwords")
        if not self.pass_list:
            print("No passwords yet!")
        else:
            for i, account in enumerate(self.pass_list):
                print(f'{i+1}.{account["website"]} | {account["username"]}')    


    def search_password(self):
        thing = input("enter a website or username to search: ")
        thing = thing.lower()
        for account in self.pass_list:
            if account["website"].lower() == thing or account["username"].lower() == thing:
                print(
                    f"Website : {account['website']}\n"
                    f"Username: {account['username']}\n"
                    f"Password: {account['password']}"
                )
                return account
                
        print("website not found!")        
        return None


    
    def delete_password(self):
        x = input("Enter account number: ")
        y = getpass("password: ")
        try:
            num = int(x)
            if not self.pass_list:
                print("No passwords yet!")
            elif num < 1 or num > len(self.pass_list):
                print("Invalid task number!")
            elif y == self.pass_list[num-1]["password"]:
                self.pass_list.pop(num-1)
                self.save_passwords()
                print("Password deleted.")
            else:
                print("number and password does not match! try again.")
        except ValueError:
            print("Please enter a number!")


    def edit_password(self):
        account = self.search_password()
        if account:
            new_password = input("Enter your new password: ").strip()
            if not new_password:
                print("Password cannot be empty.")
                return
            else:
                account["password"] = new_password
                self.save_passwords()
                print("Password updated successfully.")


    def run(self):
        try:
            with open("master.json", "r") as file:
                pass
        except FileNotFoundError:
            password = getpass("Create master password: ")
            with open("master.json", "w") as file:
                json.dump(password, file)

        check = getpass("Enter master password: ")
        with open("master.json", "r") as file:
            p = json.load(file)
        if check != p:
            print("Wrong password!")
            return
        
        while True:
            print("1.Add password")
            print("2.Show paswords")
            print("3.Search Password")
            print("4.Delete Password")
            print("5.Edit password")
            print("6.Exit")
            # check = input("Enter master password: ")

            choice = input("Choice: ")
            action = self.actions.get(choice)
            if action:
                action()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

manager = PasswordManager()
manager.run()