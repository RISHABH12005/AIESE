from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say hello in one sentence."
)

print(interaction.output_text)