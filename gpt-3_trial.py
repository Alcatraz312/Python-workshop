#gpt-3 codex model

import os
import openai
import api_key

openai.api_key = os.getenv(api_key.api_key)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

