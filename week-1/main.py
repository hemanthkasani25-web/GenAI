from google import genai
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing!")
    exit()

client = genai.Client(api_key=api_key)

print("\n================================")
print("       GEMINI LLM RUNNING")
print("================================")
print("Type exit to stop.\n")

while True:
    try:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            print("Gemini LLM stopped.")
            break

        if not prompt.strip():
            continue

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nGemini:", response.text, "\n")

    except KeyboardInterrupt:
        print("\nGemini LLM stopped.")
        break

    except Exception as e:
        print("\nError:", e, "\n")
