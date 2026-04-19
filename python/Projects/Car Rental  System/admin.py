import pwinput
import re
from car import CarManager

class AdminManager:
    def __init__(self):
        pass
    
    def login(self, username, password):
        try:
            with open("admin.txt", "r") as f:
                admin_user, admin_pass = f.read().strip().split(",")
            
            if username == admin_user and password == admin_pass:
                print("✅ Login successful!")
                return True
            return False
        except:
            return False
            # pass
    
    def admin_panel(self):
        # from car import CarManager
        car_manager = CarManager()
        
        print("\n" + "━"*50)
        print("🛠️  ADMIN PANEL".center(50))
        print("━"*50)
        
        while True:
            print("\n1. ➕ Add Car")
            print("2. 📋 Show Cars")
            print("3. 🔍 Search Car")
            print("4. ✏️  Update Car")
            print("5. 🗑️  Delete Car")
            print("6. 🔐 Change Password")
            print("7. ↩️  Logout")
            
            choice = input("Enter choice: ").strip()
            
            if choice == "1":
                car_manager.add_car()
            elif choice == "2":
                car_manager.show_cars()
            elif choice == "3":
                car_manager.search_car()
            elif choice == "4":
                car_manager.update_car()
            elif choice == "5":
                car_manager.delete_car()
            elif choice == "6":
                self.change_password()
            elif choice == "7":
                print("👋 Logging out...")
                break
            else:
                print("❌ Invalid choice!")
    
    def change_password(self):
        print("\n" + "━"*50)
        print("🔐 CHANGE PASSWORD".center(50))
        print("━"*50)
        
        try:
            with open("admin.txt", "r") as f:
                admin_user, admin_pass = f.read().strip().split(",")
            
            old = pwinput.pwinput("Old password: ", "*")
            if old == admin_pass:
                while True:
                    new = pwinput.pwinput("New password: ", "*")
                    confirm = pwinput.pwinput("Confirm password: ", "*")
                    
                    if new == confirm:
                        if self.validate_password(new):
                            with open("admin.txt", "w") as f:
                                f.write(f"{admin_user},{new}")
                            print("✅ Password changed!")
                            break
                        else:
                            print("❌ Password must be at least 4 characters!")
                    else:
                        print("❌ Passwords don't match!")
            else:
                print("❌ Wrong password!")
                
        except:
            print("❌ Error!")
    
    def validate_password(self, password):
        return len(password) >= 4
    


if(__name__ == '__main__'):
    a = AdminManager()
    # res = a.change_password()
    res = a.validate_password('111@')
    print(res)  