print("Enter user information. Leave blank and press Enter to finish.")
user = {}
while True:
    key = input("Enter key (e.g., fname, lname): ")
    if not key:
        break
    value = input(f"Enter value for {key}: ")
    user[key] = value
keys_to_check = input("\nEnter keys to check (comma-separated, e.g., fname,email,lname): ").split(',')
print("\nKey presence in the dictionary:")
for key in keys_to_check:
    key = key.strip()
    if key in user:
        print(f"{key} => {user[key]}")
    else:
        print(f"{key} is not present in the dictionary.")
