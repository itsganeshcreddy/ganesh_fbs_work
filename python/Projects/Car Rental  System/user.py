import hashlib
import pwinput
import re
import time
from datetime import datetime, date
from car import CarManager
from payment import PaymentProcessor

class UserManager:
    def __init__(self):
        self.current_user = None
        self.car_manager = CarManager()
        self.payment_processor = PaymentProcessor()
    
    def user_login(self):
        print("\n" + "━"*50)
        print("🔐 USER LOGIN".center(50))
        print("━"*50)
        
        for i in range(3):
            username = input("Username: ")
            password = pwinput.pwinput("Password: ", "*")
            
            if self.check_credentials(username, password):
                self.current_user = username
                print(f"✅ Welcome {username}!")
                time.sleep(1)
                self.user_dashboard()
                return
            
            if i < 2:
                print(f"❌ Try again! {2-i} attempts left")
        
        print("❌ Login failed!")
    
    def check_credentials(self, username, password):
        hashed_user = hashlib.sha256(username.encode()).hexdigest()
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            with open("login.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2 and parts[0] == hashed_user and parts[1] == hashed_pass:
                        return True
        except:
            pass
        return False
    
    def user_dashboard(self):
        while True:
            print("\n" + "━"*50)
            print(f"👤 WELCOME {self.current_user}".center(50))
            print("━"*50)
            print("\n1. 🚗 Rent Car")
            print("2. 📋 Return Car")
            print("3. 🔙 Logout")
            
            choice = input("Enter choice: ").strip()
            
            if choice == "1":
                self.rent_car()
            elif choice == "2":
                self.return_car_flow()
            elif choice == "3":
                print("👋 Logging out...")
                self.current_user = None
                break
            else:
                print("❌ Invalid!")
    
    def rent_car(self):
        print("\n" + "━"*50)
        print("🚗 RENT CAR".center(50))
        print("━"*50)
        
        self.car_manager.show_cars()
        
        car_id = input("\nEnter Car ID: ")
        
        if self.is_car_rented(car_id):
            print("❌ Already rented this car!")
            return
        
        if not self.car_manager.check_available(car_id):
            print("❌ Car not available!")
            return
        
        car_info = self.car_manager.get_car_info(car_id)
        if not car_info:
            print("❌ Car not found!")
            return
        
        print(f"\n🚗 Car: {car_info['name']}")
        print(f"💰 Price/Day: Rs{car_info['price']}")
        
        # Get rental days with validation
        while True:
            try:
                days = int(input("Enter rental days: "))
                if days < 1:
                    print("❌ Minimum 1 day!")
                    continue
                if days > 365:
                    print("❌ Maximum 365 days!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a number!")
        
        rental_date = self.get_rental_date()
        if not rental_date:
            return
        
        # Calculate 50% advance
        price_per_day = int(car_info['price'])
        total_amount = days * price_per_day
        advance_amount = total_amount * 0.5  # 50% advance
        
        print("\n" + "💰"*50)
        print("PAYMENT SUMMARY".center(50))
        print("💰"*50)
        print(f"Total Amount:    Rs{total_amount}")
        print(f"50% Advance Due: Rs{advance_amount:.2f}")
        print("💰"*50)
        
        # Process 50% payment
        print("\n💳 PAY 50% ADVANCE NOW")
        print("1. 💻 Online/UPI")
        print("2. 💵 Cash")
        
        while True:
            payment_choice = input("Select payment method (1-2): ").strip()
            if payment_choice in ["1", "2"]:
                break
            print("❌ Please enter 1 or 2!")
        
        if payment_choice == "1":
            if not self.payment_processor.online_payment(advance_amount):
                print("❌ Payment failed!")
                return
            payment_method = "Online"
        else:
            print(f"💵 Please pay Rs{advance_amount:.2f} cash")
            payment_method = "Cash"
        
        # Reduce car stock
        if not self.car_manager.reduce_stock(car_id):
            print("❌ Error updating stock!")
            return
        
        # Save rental record with payment info
        with open("issue.txt", "a") as f:
            f.write(f"{self.current_user},{car_id},{rental_date},{price_per_day},{car_info['name']},{total_amount},{advance_amount:.2f},{payment_method}\n")
        
        print("\n" + "✅"*50)
        print("RENTAL CONFIRMED!".center(50))
        print("✅"*50)
        print(f"Car:      {car_info['name']}")
        print(f"Days:     {days}")
        print(f"From:     {rental_date}")
        print(f"Total:    Rs{total_amount}")
        print(f"Paid:     Rs{advance_amount:.2f} ({payment_method})")
        print(f"Due:      Rs{total_amount - advance_amount:.2f} (on return)")
        print("✅"*50)
        print("\n📞 Contact: 1800-RENTALS")
        print("🎉 Enjoy your ride!")
    
    def return_car_flow(self):
        print("\n" + "━"*50)
        print("📋 RETURN CAR PROCESS".center(50))
        print("━"*50)
        
        print("\n" + "▶"*50)
        print("STEP 1: CAR SELECTED?".center(50))
        print("▶"*50)
        
        rented_cars = self.get_user_rentals()
        if not rented_cars:
            print("❌ NO - No cars rented!")
            print("END PROCESS")
            return
        
        print("✅ YES - Your rented cars:")
        for i, car in enumerate(rented_cars, 1):
            print(f"{i}. {car['name']} (ID: {car['id']}) - Rented: {car['date']}")
        
        try:
            choice = int(input("\nSelect car number: ")) - 1
            if 0 <= choice < len(rented_cars):
                car_id = rented_cars[choice]['id']
                car_name = rented_cars[choice]['name']
                print(f"✅ Selected: {car_name}")
            else:
                print("❌ Invalid selection!")
                return
        except:
            print("❌ Invalid input!")
            return
        
        print("\n" + "▶"*50)
        print("STEP 2: RETURN CAR PROCESS".center(50))
        print("▶"*50)
        
        print("\n" + "▶"*50)
        print("STEP 3: ENTER RETURN DATE".center(50))
        print("▶"*50)
        
        return_date = self.get_return_date()
        if not return_date:
            return
        
        print("\n" + "▶"*50)
        print("STEP 4: CALCULATE FINAL BILL".center(50))
        print("▶"*50)
        
        bill = self.calculate_bill(car_id, return_date)
        if not bill:
            return
        
        print("\n" + "💰"*50)
        print("FINAL BILL".center(50))
        print("💰"*50)
        print(f"Car:          {bill['car_name']}")
        print(f"Rented on:    {bill['rental_date']}")
        print(f"Returned on:  {bill['return_date']}")
        print(f"Total Days:   {bill['days']}")
        print(f"Rate:         Rs{bill['price_per_day']}/day")
        print(f"Total:        Rs{bill['total']}")
        print(f"50% Paid:     Rs{bill['advance_paid']:.2f} ({bill['payment_method']})")
        print(f"50% Due:      Rs{bill['remaining']:.2f}")
        print("💰"*50)
        
        print("\n" + "▶"*50)
        print("STEP 5: PAY REMAINING 50%".center(50))
        print("▶"*50)
        
        print("\n💳 PAY REMAINING 50%")
        print("1. 💻 Online/UPI")
        print("2. 💵 Cash")
        
        while True:
            payment_choice = input("Select payment method (1-2): ").strip()
            if payment_choice in ["1", "2"]:
                break
            print("❌ Please enter 1 or 2!")
        
        if payment_choice == "1":
            if not self.payment_processor.online_payment(bill['remaining']):
                print("❌ Payment failed!")
                return
            return_payment_method = "Online"
        else:
            print(f"💵 Please pay Rs{bill['remaining']:.2f} cash")
            return_payment_method = "Cash"
        
        print("\n" + "▶"*50)
        print("STEP 6: UPDATE RECORDS".center(50))
        print("▶"*50)
        
        self.car_manager.increase_stock(car_id)
        self.remove_rental_record(car_id)
        
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
        with open("requests.txt", "a") as f:
            f.write(f"{self.current_user},{car_id},{timestamp},Final:Rs{bill['total']},Paid:Rs{bill['advance_paid']:.2f}+Rs{bill['remaining']:.2f},Method:{bill['payment_method']}+{return_payment_method}\n")
        
        print("✅ Records updated!")
        
        print("\n" + "▶"*50)
        print("STEP 7: UPDATE CAR STATUS".center(50))
        print("▶"*50)
        
        print(f"\n🚗 Car ID {car_id} status: ✅ AVAILABLE")
        
        print("\n" + "▶"*50)
        print("✅ RETURN PROCESS COMPLETE".center(50))
        print("▶"*50)
        print("\n🎉 Thank you for your business!")
        print("📞 Visit us again!")
    
    def calculate_bill(self, car_id, return_date):
        try:
            with open("issue.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 8 and parts[0] == self.current_user and parts[1] == car_id:
                        rental_date = datetime.strptime(parts[2], "%d-%m-%Y").date()
                        days = (return_date - rental_date).days
                        
                        if days < 0:
                            print("❌ Return date cannot be before rental date!")
                            return None
                        
                        if days == 0:
                            days = 1
                        
                        price_per_day = int(parts[3])
                        total_amount = days * price_per_day
                        
                        # Get advance payment details
                        advance_paid = float(parts[6]) if len(parts) > 6 else 0
                        payment_method = parts[7] if len(parts) > 7 else "Unknown"
                        
                        # Calculate remaining
                        remaining = total_amount - advance_paid
                        
                        return {
                            'car_id': car_id,
                            'car_name': parts[4],
                            'rental_date': parts[2],
                            'return_date': return_date.strftime("%d-%m-%Y"),
                            'days': days,
                            'price_per_day': price_per_day,
                            'total': total_amount,
                            'advance_paid': advance_paid,
                            'payment_method': payment_method,
                            'remaining': remaining
                        }
            
            print("❌ Rental record not found!")
            return None
            
        except Exception as e:
            print(f"❌ Error calculating bill: {e}")
            return None
    
    def get_rental_date(self):
        while True:
            date_str = input("Rental date (dd-mm-yyyy): ")
            try:
                # Validate date format
                date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                today = datetime.now().date()
                if date_obj.date() < today:
                    print("❌ Cannot select past date!")
                    continue
                return date_str
            except ValueError:
                print("❌ Invalid date format! Use dd-mm-yyyy")
    
    def get_return_date(self):
        while True:
            date_str = input("Return date (dd-mm-yyyy): ")
            try:
                return datetime.strptime(date_str, "%d-%m-%Y").date()
            except:
                print("❌ Invalid date! Use dd-mm-yyyy")
    
    def get_user_rentals(self):
        rentals = []
        try:
            with open("issue.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 5 and parts[0] == self.current_user:
                        rentals.append({
                            'id': parts[1],
                            'name': parts[4],
                            'date': parts[2]
                        })
        except:
            pass
        return rentals
    
    def is_car_rented(self, car_id):
        try:
            with open("issue.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2 and parts[0] == self.current_user and parts[1] == car_id:
                        return True
        except:
            pass
        return False
    
    def remove_rental_record(self, car_id):
        lines = []
        try:
            with open("issue.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2 and parts[0] == self.current_user and parts[1] == car_id:
                        continue
                    lines.append(line)
            
            with open("issue.txt", "w") as f:
                f.writelines(lines)
        except:
            pass
    
    # ============ REGISTRATION WITH VALIDATIONS ============
    def register_user(self):
        print("\n" + "━"*50)
        print("📝 REGISTER NEW USER".center(50))
        print("━"*50)
        
        # Name validation
        while True:
            name = input("Full Name: ").strip()
            if len(name) < 3:
                print("❌ Name must be at least 3 characters!")
                continue
            if not re.match(r"^[A-Za-z\s]+$", name):
                print("❌ Name can only contain letters and spaces!")
                continue
            if len(name.split()) < 2:
                print("❌ Please enter both first and last name!")
                continue
            break
        
        # Age validation
        while True:
            age_str = input("Age: ")
            try:
                age = int(age_str)
                if age < 18:
                    print("❌ Must be 18 or older!")
                    continue
                if age > 100:
                    print("❌ Please enter valid age!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a number!")
        
        # Mobile validation
        while True:
            mobile = input("Mobile Number (10 digits): ").strip()
            if not re.match(r"^[6-9]\d{9}$", mobile):
                print("❌ Invalid mobile number! Must start with 6-9 and be 10 digits")
                continue
            break
        
        # Address validation
        while True:
            address = input("Address: ").strip()
            if len(address) < 5:
                print("❌ Address too short!")
                continue
            break
        
        # Username validation
        while True:
            username = input("Username: ").strip()
            if len(username) < 5:
                print("❌ Username must be at least 5 characters!")
                continue
            if not re.match(r"^[A-Za-z0-9_]+$", username):
                print("❌ Username can only contain letters, numbers, and underscores!")
                continue
            
            # Check if username exists
            if self.check_username_exists(username):
                print("❌ Username already taken!")
                continue
            break
        
        # Password validation
        while True:
            print("\n📋 Password Requirements:")
            print("- At least 8 characters")
            print("- At least 1 uppercase letter")
            print("- At least 1 lowercase letter")
            print("- At least 1 number")
            print("- At least 1 special character (!@#$%^&*)")
            
            password = pwinput.pwinput("Password: ", "*")
            confirm = pwinput.pwinput("Confirm Password: ", "*")
            
            if password != confirm:
                print("❌ Passwords don't match!")
                continue
            
            if len(password) < 8:
                print("❌ Password must be at least 8 characters!")
                continue
            
            if not re.search(r"[A-Z]", password):
                print("❌ Password must contain at least one uppercase letter!")
                continue
            
            if not re.search(r"[a-z]", password):
                print("❌ Password must contain at least one lowercase letter!")
                continue
            
            if not re.search(r"\d", password):
                print("❌ Password must contain at least one number!")
                continue
            
            if not re.search(r"[!@#$%^&*]", password):
                print("❌ Password must contain at least one special character!")
                continue
            
            break
        
        # Hash and save
        hashed_user = hashlib.sha256(username.encode()).hexdigest()
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        
        with open("login.txt", "a") as f:
            f.write(f"{hashed_user},{hashed_pass},{name},{age},{mobile},{address}\n")
        
        print("\n" + "✨"*20)
        print("✅ REGISTRATION SUCCESSFUL!".center(40))
        print("✨"*20)
        print(f"\n👤 Welcome {name}!")
        print(f"📱 Mobile: {mobile}")
        print(f"🏠 Address: {address}")
        print("\n🚗 You can now rent cars!")
        time.sleep(2)
    
    def check_username_exists(self, username):
        hashed_user = hashlib.sha256(username.encode()).hexdigest()
        
        try:
            with open("login.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts and parts[0] == hashed_user:
                        return True
        except:
            pass
        return False
    
if(__name__ == '__main__'):
    u = UserManager()
    # res = u.user_login()
    res = u.user_dashboard()
    print(res)