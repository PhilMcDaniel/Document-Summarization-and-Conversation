import os
import openai

# set environment variable for OpenAI API Key


# Access the environment variable
openai.api_key = os.getenv("OPENAI_DOCSUMMARY")

prompt_prefix = 'Summarize the content below with 3 bullet points:\n'
content = 'The Lichess qualifier will have three stages. The first will comprise twelve open-entry arena tournaments, aimed especially towards the timezones of North and South America, Europe, and Central Asia / India. The top 20 players from each arena will then play a single 11-round Swiss tournament, where they may be joined by up to ten wildcard players. Finally, the top seven finishers from the Swiss tournament will be joined by a wildcard player, and the qualifiers will be determined by single-encounter Round Robin Tournament. Everyone who makes it to the knockout stage will receive a share of a $2,000 prize fund.'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt_prefix+content,
  max_tokens=100,
  temperature=0.5,
  n=1,
  stream=False,
)

print(response['choices'][0]['text'])

