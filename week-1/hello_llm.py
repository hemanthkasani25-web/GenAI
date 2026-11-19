import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("ANTHROPIC_API_KEY"):
    raise SystemExit("API key is missing. Check your .env file.")

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Explain Python in two simple sentences.",
        }
    ],
)

print(response.content[0].text)
print(f"\nTokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
