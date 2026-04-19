import random
import time
import re

class PaymentProcessor:
    def __init__(self):
        pass
    
    def online_payment(self, amount):
        print("\n" + "━"*50)
        print("💻 ONLINE PAYMENT".center(50))
        print("━"*50)
        
        # UPI ID validation
        while True:
            upi = input("Enter UPI ID (e.g. user@upi, user@okbank, user@paytm): ").strip().lower()
            if self.validate_upi(upi):
                break
            print("❌ Invalid UPI ID! Must be in format: user@provider")
        
        # Generate OTP
        otp = random.randint(100000, 999999)
        print(f"\n📱 OTP sent to your mobile: {otp}")
        print("(Valid for 5 minutes)")
        
        # OTP validation
        attempts = 0
        while attempts < 3:
            try:
                user_otp = int(input("Enter OTP: "))
                
                if user_otp == otp:
                    print(f"\n💳 Processing Rs{amount:.2f}...")
                    time.sleep(2)
                    print(f"✅ Payment successful!")
                    print(f"💰 Amount: Rs{amount:.2f}")
                    print(f"🔗 UPI ID: {upi}")
                    print(f"📊 Transaction ID: {random.randint(1000000000, 9999999999)}")
                    return True
                else:
                    attempts += 1
                    if attempts < 3:
                        print(f"❌ Wrong OTP! {3-attempts} attempts left")
                    else:
                        print("❌ Too many wrong attempts! Payment failed.")
                        return False
                        
            except ValueError:
                print("❌ Please enter numbers only!")
                attempts += 1
        
        return False
    
    def validate_upi(self, upi_id):
        # Basic UPI validation pattern
        pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+$'
        return re.match(pattern, upi_id) is not None
    
    def cash_payment(self, amount):
        print(f"\n💵 CASH PAYMENT")
        print(f"Amount: Rs{amount:.2f}")
        print("Please keep exact amount ready")
        return True
    


if(__name__ == '__main__'):
    p = PaymentProcessor()
    # res = p.online_payment(1000)
    # res = p.cash_payment(2000)
    res = p.validate_upi('a@upi')
    print(res)

