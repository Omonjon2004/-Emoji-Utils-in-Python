import demoji

# Find emoji and special
def find_emojis(text):
    return demoji.findall(text)

print("\n\n")

# Test text
text = " IN 🥳 🥂 👀 🥸 🤝 "
result = find_emojis(text)

# Output the result
print("Emojis and their images:", result)

print("\n\n")

# Only output emojis
emojis = list(result.keys())
print("Only emojis:", emojis)

print("\n\n")

