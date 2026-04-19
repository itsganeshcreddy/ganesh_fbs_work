import re
from tabulate import tabulate

class CarManager:
    def __init__(self):
        pass
    
    def add_car(self):
        print("\n" + "━"*50)
        print("➕ ADD CAR".center(50))
        print("━"*50)
        
        # Car ID validation
        while True:
            car_id = input("Car ID (numbers only): ").strip()
            if not car_id.isdigit():
                print("❌ Car ID must contain only numbers!")
                continue
            if len(car_id) < 1:
                print("❌ Car ID cannot be empty!")
                continue
            
            # Check duplicate
            duplicate = False
            try:
                with open("data.txt", "r") as f:
                    for line in f:
                        if line.startswith(car_id + ","):
                            duplicate = True
                            break
            except:
                pass
            
            if duplicate:
                print("❌ Car ID already exists!")
                continue
            break
        
        # Car Name validation
        while True:
            name = input("Car Name: ").strip()
            if len(name) < 2:
                print("❌ Car name too short!")
                continue
            if not re.match(r"^[A-Za-z0-9\s\-]+$", name):
                print("❌ Car name can only contain letters, numbers, spaces, and hyphens!")
                continue
            break
        
        # Price validation
        while True:
            price_str = input("Price/Day: Rs:").strip()
            try:
                price = int(price_str)
                if price < 100:
                    print("❌ Price must be at least Rs100!")
                    continue
                if price > 10000:
                    print("❌ Price too high!")
                    continue
                price = str(price)
                break
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Quantity validation
        while True:
            qty_str = input("Quantity: ").strip()
            try:
                qty = int(qty_str)
                if qty < 1:
                    print("❌ Quantity must be at least 1!")
                    continue
                if qty > 100:
                    print("❌ Quantity too high!")
                    continue
                qty = str(qty)
                break
            except ValueError:
                print("❌ Please enter a valid number!")
        
        with open("data.txt", "a") as f:
            f.write(f"{car_id},{name},{price},{qty}\n")
        
        print(f"\n✅ Car '{name}' added successfully!")
    
    def show_cars(self):
        print("\n" + "━"*50)
        print("📋 CAR LIST".center(50))
        print("━"*50)
        
        try:
            with open("data.txt", "r") as f:
                cars_data = []
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        if len(parts) >= 4:
                            cars_data.append(parts)
            
            if not cars_data:
                print("🚫 No cars available!")
                return
            
            # Create headers
            headers = ["🔢 ID", "🚗 Car Name", "💰 Price/Day", "📦 Available"]
            
            # Format data for tabulate
            table_data = []
            for car in cars_data:
                table_data.append([
                    car[0],  # ID
                    car[1],  # Name
                    f"Rs{car[2]}",  # Price
                    car[3]   # Quantity
                ])
            
            # Display table using tabulate
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            print(f"\n📊 Total Cars: {len(cars_data)}")
            
        except FileNotFoundError:
            print("📭 No cars data found!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def search_car(self):
        print("\n" + "━"*50)
        print("🔍 SEARCH CAR".center(50))
        print("━"*50)
        
        car_id = input("Enter Car ID: ")
        
        try:
            found_car = None
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        found_car = parts
                        break
            
            if found_car:
                print(f"\n✅ Car Found!")
                print("="*40)
                
                # Display in table format
                headers = ["🔢 ID", "🚗 Car Name", "💰 Price/Day", "📦 Available"]
                table_data = [[
                    found_car[0],
                    found_car[1],
                    f"Rs{found_car[2]}",
                    found_car[3]
                ]]
                
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                print("="*40)
            else:
                print(f"❌ Car ID {car_id} not found!")
            
        except:
            print("❌ Error searching car!")
    
    def update_car(self):
        print("\n" + "━"*50)
        print("✏️  UPDATE CAR".center(50))
        print("━"*50)
        
        car_id = input("Enter Car ID: ")
        
        cars = []
        found = False
        
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        found = True
                        print(f"\n📝 Updating Car: {parts[1]}")
                        print("-"*40)
                        print("What to update?")
                        print("1. 🏷️  Name")
                        print("2. 💰 Price")
                        print("3. 📦 Quantity")
                        print("-"*40)
                        
                        while True:
                            choice = input("Choice (1-3): ").strip()
                            if choice in ["1", "2", "3"]:
                                break
                            print("❌ Please enter 1, 2, or 3!")
                        
                        if choice == "1":
                            while True:
                                new_name = input("New Car Name: ").strip()
                                if len(new_name) < 2:
                                    print("❌ Name too short!")
                                    continue
                                parts[1] = new_name
                                break
                        elif choice == "2":
                            while True:
                                new_price = input("New Price: Rs").strip()
                                try:
                                    price = int(new_price)
                                    if price < 100:
                                        print("❌ Price must be at least Rs100!")
                                        continue
                                    parts[2] = str(price)
                                    break
                                except ValueError:
                                    print("❌ Please enter valid number!")
                        else:
                            while True:
                                new_qty = input("New Quantity: ").strip()
                                try:
                                    qty = int(new_qty)
                                    if qty < 0:
                                        print("❌ Quantity cannot be negative!")
                                        continue
                                    parts[3] = str(qty)
                                    break
                                except ValueError:
                                    print("❌ Please enter valid number!")
                    
                    cars.append(",".join(parts))
            
            if found:
                with open("data.txt", "w") as f:
                    f.write("\n".join(cars) + "\n")
                print("✅ Car updated successfully!")
            else:
                print("❌ Car not found!")
                
        except:
            print("❌ Error updating car!")
    
    def delete_car(self):
        print("\n" + "━"*50)
        print("🗑️  DELETE CAR".center(50))
        print("━"*50)
        
        car_id = input("Enter Car ID to delete: ")
        
        cars = []
        found = False
        
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        found = True
                        
                        # Show car details before deletion
                        print(f"\n⚠️  Deleting this car:")
                        print("="*40)
                        headers = ["🔢 ID", "🚗 Car Name", "💰 Price/Day", "📦 Available"]
                        table_data = [[
                            parts[0],
                            parts[1],
                            f"Rs{parts[2]}",
                            parts[3]
                        ]]
                        print(tabulate(table_data, headers=headers, tablefmt="grid"))
                        print("="*40)
                        
                        confirm = input("\n❓ Are you sure? (yes/no): ").lower().strip()
                        if confirm != "yes":
                            print("✅ Deletion cancelled!")
                            return
                        continue
                    if parts:
                        cars.append(",".join(parts))
            
            if found:
                with open("data.txt", "w") as f:
                    f.write("\n".join(cars) + "\n")
                print("✅ Car deleted successfully!")
            else:
                print("❌ Car not found!")
                
        except:
            print("❌ Error deleting car!")
    
    def check_available(self, car_id):
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        return int(parts[3]) > 0
        except:
            pass
        return False
    
    def reduce_stock(self, car_id):
        cars = []
        updated = False
        
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        qty = int(parts[3])
                        if qty > 0:
                            parts[3] = str(qty - 1)
                            updated = True
                        else:
                            return False
                    
                    cars.append(",".join(parts))
            
            if updated:
                with open("data.txt", "w") as f:
                    f.write("\n".join(cars) + "\n")
                return True
                
        except:
            pass
        return False
    
    def increase_stock(self, car_id):
        cars = []
        updated = False
        
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        qty = int(parts[3])
                        parts[3] = str(qty + 1)
                        updated = True
                    
                    cars.append(",".join(parts))
            
            if not updated:
                try:
                    with open("issue.txt", "r") as f:
                        for line in f:
                            parts = line.strip().split(",")
                            if len(parts) >= 5 and parts[1] == car_id:
                                cars.append(f"{car_id},{parts[4]},{parts[3]},1")
                                break
                except:
                    pass
            
            with open("data.txt", "w") as f:
                f.write("\n".join(cars) + "\n")
            return True
            
        except:
            pass
        return False
    
    def get_car_info(self, car_id):
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == car_id:
                        return {'name': parts[1], 'price': parts[2]}
        except:
            pass
        return None
    

if(__name__ == '__main__'):
    cm = CarManager()
    # res = cm.add_car()
    # res = cm.show_cars()
    # res = cm.search_car()
    # res = cm.update_car()
    res = cm.delete_car()
    print(res)