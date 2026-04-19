import os
import time
import pwinput
from admin import AdminManager
from user import UserManager

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=^"*30)
    print("🚗  CAR RENTAL SYSTEM  🚗".center(60))
    print("=^"*30)
    time.sleep(1)
    
    admin_manager = AdminManager()
    user_manager = UserManager()
    
    while True:
        print("\n" + "━"*50)
        print("🏠 MAIN MENU".center(50))
        print("━"*50)
        print("1. 👨‍💼 Admin")
        print("2. 👤 User")
        print("3. 🚪 Exit")
        print("━_"*50)
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            admin_login(admin_manager)
        elif choice == "2":
            user_menu(user_manager)
        elif choice == "3":
            exit_system()
            break
        else:
            print("❌ Invalid choice!")

def admin_login(admin_manager):
    print("\n" + "━"*50)
    print("🔐 ADMIN LOGIN".center(50))
    print("━"*50)
    
    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = pwinput.pwinput("Password: ", "*")
        
        if admin_manager.login(username, password):
            admin_manager.admin_panel()
            return
        else:
            attempts += 1
            if attempts < 3:
                print(f"❌ Wrong! {3-attempts} tries left")
    
    print("❌ Blocked! Try later.")

def user_menu(user_manager):
    print("\n" + "━"*50)
    print("👤 USER PORTAL".center(50))
    print("━"*50)
    
    while True:
        print("\n1. 🔐 Login")
        print("2. 📝 Register")
        print("3. ↩️  Back")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            user_manager.user_login()
        elif choice == "2":
            user_manager.register_user()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice!")

def exit_system():
    print("\n" + "✨"*50)
    print("🙏 Thank You!".center(50))
    print("✨"*50)
    time.sleep(2)

if __name__ == "__main__":
    main()
