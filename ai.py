import openai

class AI:
    def __init__(self, openai_key):
        pass

    
    # Define a function that takes user input and sends it to ChatGPT
    def ask_gpt(self, prompt):
        response = openai.Completion.create(
            engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7,
        )

        # Return the first choice of response text
        message = response.choices[0].text.strip()
        return message