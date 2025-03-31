recipient_name = input("Please enter the recipient name ")
year_of_birth = input("Please enter the date of birth ")
personlised_message = input("Please enter a personlised message ")
sender_name = input("Please enter sender's name ")

year_as_int = int(year_of_birth)

age = 2025 - year_as_int

print(f"🎉 Happy Birthday, {recipient_name}! 🎉\n")
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!\n")
print(f"{personlised_message}\n")
print(f"With love and best wgit ishes,\n{sender_name}")