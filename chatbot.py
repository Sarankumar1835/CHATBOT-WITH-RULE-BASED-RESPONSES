#!/usr/bin/env python
# coding: utf-8

# In[2]:


def chatbot():
    print("Hello! I am a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input in ['how are you?', 'what are you doing?']:
            print("Chatbot: I'm just a bot, but I'm here to help you!")
        elif user_input in ['what is your name?', 'who are you?']:
            print("Chatbot: I am a simple rule-based chatbot.")
        elif user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
            
if __name__ == "__main__":
    chatbot()

