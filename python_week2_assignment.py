# Simple Bill Calculator

def main():
    print("=== Simple Bill Calculator ===")
    
    # Get user inputs
    total_bill = float(input("Enter total bill amount (KSh): "))
    tip_percentage = float(input("Enter tip percentage (e.g., 10, 15): "))
    number_of_people = int(input("Enter number of people splitting bill: "))
    
    # Perform calculations
    tip_amount = (tip_percentage / 100) * total_bill
    final_total = total_bill + tip_amount
    amount_per_person = final_total / number_of_people
    
    # Display results
    print("\n--- Bill Summary ---")
    print(f"Original Bill: KSh {total_bill:.2f}")
    print(f"Tip Amount ({tip_percentage}%): KSh {tip_amount:.2f}")
    print(f"Total Amount Due: KSh {final_total:.2f}")
    print(f"Amount Per Person: KSh {amount_per_person:.2f}")

if __name__ == "__main__":
    main()