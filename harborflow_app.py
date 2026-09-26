#Task 3
def calculate_quote(distance, weight, service_code):
    #Basic components for the quote and subtotal
    base_charge = 45.00
    distance = float(distance)
    weight = float(weight)
    service_code = service_code.upper()
    
    # Conditions for the service code
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6
    else:
        print("Invalid service code. Please enter S, X, or P.")
        return None

    # Calculation for subtotal and delivery quote
    subtotal = base_charge + (distance * 6.5) + (weight * 4)
    quote = subtotal * service_multiplier
    return quote

# Printing values for the quote and subtotal
distance = float(input("Distance (km): "))
weight = float(input("Weight (kg): "))
service_code = input("Service code: ")

quote = calculate_quote(distance, weight, service_code)
if quote is not None:
    print(f"Delivery quote: {quote:.2f} SEK")

#Task 4 - Consolidate parcel labels
# list, distinct label once, preserving the order, 
# splitting, loops, normalization, memberships checks, ordered output

scanned_labels = input("Scanned labels: ")
scanned_labels = scanned_labels.split(",")

unique_labels = []

for label in scanned_labels:
    label = label.upper()
    label = label.strip()
    if label not in unique_labels:
        unique_labels.append(label)

print(f"Unique load list:")

for number, label in enumerate(unique_labels, start = 1):
    print(f"{number}. {label}")

print(f"Total unique parcels: {len(unique_labels)}")
     

# Started Task 5 ( Checling Van Capacity )

# Created a function named Check Van Capacity

def check_van_capacity():
    capacity = float(input("What is Van Capacity in KG: "))
    weights = input("Enter parcel weights in KG: ").split(",")

    remaining_capacity = capacity
    accepted_count = 0
    loaded_weight = 0

    # Used For Lopp and If-Else statement

    for i in range(len(weights)):
        weight = float(weights[i])

        if weight <= remaining_capacity:
            print(f"Parcel {i + 1}: Accepted")
            accepted_count = accepted_count + 1
            loaded_weight = loaded_weight + weight
            remaining_capacity = remaining_capacity - weight
        else:
            print(f"Parcel {i + 1}: Rejected")

    print(f"Accepted Parcels: {accepted_count}")
    print(f"Loaded Weight: {loaded_weight:.2f} KG")
    print(f"Remaining Capacity: {remaining_capacity:.2f} KG")


# Started Task 6 ( Classify Service Performance )

# Created a function named Classify Performance

def classify_performance(promised, actual, damaged):
    delay = actual - promised

# Using If-Else Statements 

    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    return delay, status

# Created another function named Service Performance 

def service_performance():
    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged = int(input("Damaged parcels: "))

    delay, status = classify_performance(promised, actual, damaged)

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")












"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.
    pass


if __name__ == "__main__":
    main()
