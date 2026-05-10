import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6-20260218",
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)

print(response.content[0].text)