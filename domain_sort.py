import os

def get_email_domain(string):
    # Split the string and return the email domain
    email = string.split("|")[1]
    domain = email.split("@")[1]
    return domain

# Read the file and extract the strings
with open("file.txt", "r") as file:
    strings = file.readlines()

# Sort the strings by email domain using the custom sorting key
sorted_strings = sorted(strings, key=get_email_domain)

# Write the sorted strings back to the file
with open("sorted_file.txt", "w") as file:
    file.writelines(sorted_strings)

# Create files per domain name
file_dict = {}

for string in sorted_strings:
    domain = get_email_domain(string)

    # If a new domain is encountered, create a new file
    if domain not in file_dict:
        os.makedirs(domain, exist_ok=True)
        file_dict[domain] = open(f"{domain}/{domain}.txt", "a")

    # Write the record to the file
    file_dict[domain].write(string)

# Close all files
for file in file_dict.values():
    file.close()
