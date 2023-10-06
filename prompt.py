#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Learner Gamebot Rex
# Beta Version Developed by Kevin Kim (October 3rd, 2023)
import openai


# In[36]:


# Use your key here
openai.api_key = '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'


# In[37]:


def process_input(user_input):
    # Send user input to OpenAI for processing
    response = openai.Completion.create(
      model="gpt-3.5-turbo",
      prompt=user_input,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def game_logic(user_input, ai_response):
    # Implement game logic based on user input and AI response
    # Update game state as necessary
    
    pass

def get_response_from_openai(user_input):
    # Send user input to OpenAI for processing
    response = openai.Completion.create(
      model="gpt-4.0-turbo",
      prompt=user_input,
      max_tokens=150
    )
    return response.choices[0].text.strip()


# In[43]:


def main():
    while True:
        print("You:", end=" ")
        user_input = input()
        
        if not user_input:
            break

        if user_input.lower() == "hi":
            print("Hello")
        else:
            print(user_input)


# In[44]:


if __name__ == "__main__":
    main()


# In[ ]:




