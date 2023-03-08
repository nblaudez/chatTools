import openai
openai.api_key = "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"

class ChatGPT:
    def __init__(self):
        self.prompt = ">>"
        self.model = "text-davinci-003"
        self.temperature = 0.1
        self.max_tokens = 1024
        self.top_p = 1
        self.frequency_penalty = 0
        self.presence_penalty = 0
        self.stop = ">>"
    
    def generate_response(self, message):
        prompt = f"{self.prompt}You: {message}\nAI assistant:"
        completions = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            stop=self.stop,
        )
        message = completions.choices[0].text.strip()
        return message
