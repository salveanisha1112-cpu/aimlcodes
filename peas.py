# Simple Chatbot Intelligent Agent

print("----- CHATBOT -----")
print("Hello! I am a Chatbot.")

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "your name":
        print("Bot: I am a Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")





# Smart Home Intelligent Agent

print("----- SMART HOME CONTROLLER -----")

temperature = int(input("Enter Temperature: "))
light = input("Enter Light (dark/bright): ").lower()
motion = input("Motion Detected (yes/no): ").lower()

# Fan Control
if temperature > 30:
    print("Fan: ON")
else:
    print("Fan: OFF")

# Light Control
if light == "dark":
    print("Light: ON")
else:
    print("Light: OFF")

# Security Control
if motion == "yes":
    print("Alarm: ON")
else:
    print("Alarm: OFF")

    



# Recommendation Assistant

print("----- RECOMMENDATION ASSISTANT -----")

print("1. Movies")
print("2. Music")
print("3. Books")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Recommended: 3 Idiots")

elif choice == 2:
    print("Recommended: Motivational Songs")

elif choice == 3:
    print("Recommended: Wings of Fire")

else:
    print("Invalid Choice")