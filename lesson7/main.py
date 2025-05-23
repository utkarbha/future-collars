csv_content = """door,3,7,0
sand,12,5,1
brush,22,34,5
poster,red,8,stick
"""

# Write to in.csv in the current directory
with open("in.csv", "w", encoding="utf-8") as file:
    file.write(csv_content)

print("✅ 'in.csv' created successfully.")