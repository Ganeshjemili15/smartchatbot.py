
# COLLEGE FAQ CHATBOT 

print("                                                            ")
print("       SMART COLLEGE CHATBOT")
print("                                                            ")

print("Hello! Welcome to College FAQ Chatbot.")
print("Ask me anything about college.")
print("Type 'help' for topics.")

# 1. Store college information
faq = {
    "college": {
        "keywords": ["college name", "name of college", "which college","college"],
        "answer": "RVR & JC College of Engineering."
    },

    "library": {
        "keywords": ["library", "books", "reading room"],
        "answer": "Our college has a library for students."
    },

    "courses": {
        "keywords": ["courses", "branches", "departments"],
        "answer": "Our college offers different engineering courses, like CSM,CSE,IT,AIDS,DS,QUANTUM,MECH,CIVIL,CHEMICAL ENGINEERING."
    },

    "hostel": {
        "keywords": ["hostel", "accommodation", "stay"],
        "answer": "Please contact the college hostel office for details,there are hostels for both boys and girls and boys hostel is near the campus and girls hostel is in guntur."
    },

    "timings": {
        "keywords": ["timings", "college time", "working hoirs"],
        "answer": "when it comes to timings of the college for 1st,3rd year students college runs from 10am to 5pm,whereas for 2nd,4th year students college runs from 8am to 5pm."
    },

    "placements": {
        "keywords": ["placements", "jobs", "companies", "recruitment"],
        "answer": "Please check the official placement cell for current details."
    },

    "transport": {
        "keywords": ["transport", "bus", "college bus"],
        "answer": "For transportation there are many buses for both chilakaluripet and guntur routes."
    }
}


# 2. Create a function to find answers
def find_answer(question):

    question = question.lower().strip()

    # Check each topic
    for topic, details in faq.items():

        for keyword in details["keywords"]:

            if keyword in question:
                return details["answer"]

    return None


# 3. Start chatbot
while True:

    question = input("\nYou: ").lower().strip()

    if question in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif question == "help":
        print("Bot: You can ask about:")
        for topic in faq:
            print("-", topic)

    elif question in ["bye", "exit", "quit"]:
        print("Bot: Thank you! Have a nice day.")
        

    else:
        answer = find_answer(question)

        if answer is not None:
            print("Bot:", answer)

        else:
            print("Bot: Sorry, I couldn't understand.")
            print("Bot: Try asking about library, hostel, courses or placements or ask help.")
