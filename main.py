# SanCap Calculator

# Sets the base price for small, medium, large and estate property
BASE_RATE_BY_SIZE = {
    'small': 200,  # <= 1500 sq ft
    'medium': 250,  # <= 2500 sq ft
    'large': 280,  # <= 3500sq ft
    'estate': 350  # > 3500sq ft
}

# Percent applied for select uplifts
UPLIFT_PERCENT = {
    'First Time Clean': (0.25, 0.30),
    'Deep Clean': (0.40, 0.50),
    'Move In/Out': (0.50, 0.70),
    'Maintenance': (0.00, 0.00)
}

# Create a list of cleaning types
CLEANING_OPTIONS = [
    "First Time Clean",
    "Deep Clean",
    "Move In/Out",
    "Maintenance"
]

# Creates a dictionary for addon options
ADDONS = {
    0: ("None", 0),
    1: ("Inside Fridge", 25),
    2: ("Inside Oven", 30),
    3: ("Windows (Interior)", 40),
    4: ("Blinds Dusting", 20)
    # Add more items here
}


def run_calculator():
    while True:
        while True:
            try:
                square_footage = int(input("Enter the square footage: "))
                if square_footage > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Display cleaning type menu
        print("\nSelect the cleaning type:")
        for idx, option in enumerate(CLEANING_OPTIONS, start=1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice = int(input("Enter your choice (1–4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        cleaning_type = CLEANING_OPTIONS[choice - 1]

        if square_footage <= 1500:
            base_rate = BASE_RATE_BY_SIZE['small']
        elif square_footage <= 2500:
            base_rate = BASE_RATE_BY_SIZE['medium']
        elif square_footage <= 3500:
            base_rate = BASE_RATE_BY_SIZE['large']
        else:
            base_rate = BASE_RATE_BY_SIZE['estate']

        uplift_low, uplift_high = UPLIFT_PERCENT.get(cleaning_type, (0.00, 0.00))

        print("\nSelect any add-on services (enter numbers separated by commas, e.g. 2,4):")
        for key, (name, price) in ADDONS.items():
            print(f"{key}. {name} - ${price}")

        addon_choices = input("Your choices: ")

        addon_total = 0
        selected_addons = []

        for choice_str in addon_choices.split(","):
            try:
                choice = int(choice_str.strip())
                if choice in ADDONS and ADDONS[choice][0] != "None":
                    selected_addons.append(ADDONS[choice][0])
                    addon_total += ADDONS[choice][1]
            except ValueError:
                print(f"Invalid input: '{choice_str.strip()}' ignored.")

        estimate_low = base_rate * (1 + uplift_low) + addon_total
        estimate_high = base_rate * (1 + uplift_high) + addon_total

        print("\n--- Estimate Breakdown ---")
        print(f"Square Footage: {square_footage}")
        print(f"Base Rate: ${base_rate:.2f}")
        print(f"Cleaning Type: {cleaning_type} (+{int(uplift_low * 100)}% – {int(uplift_high * 100)}%)")

        if selected_addons:
            print("Add-ons Selected:")
            for addon in selected_addons:
                print(f"  - {addon}")
            print(f"Total Add-on Cost: ${addon_total:.2f}")
        else:
            print("No Add-ons Selected.")

        print(f"\nEstimated Price Range: ${estimate_low:.2f} – ${estimate_high:.2f}")
        print("This range is an estimate for the level of detail involved in this type of cleaning.")

        # Restart prompt
        restart = input("\nDo you want to start over? (Y/n): ").strip().lower()
        if restart not in ['', 'y', 'yes']:
            print("Goodbye!")
            break


if __name__ == '__main__':
    run_calculator()
