import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("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")

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)