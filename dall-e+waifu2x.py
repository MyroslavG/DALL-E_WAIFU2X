import openai
import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

PROMPT = "YOUR PROMPT"
openai.api_key = "YOUR DALL-E API KEY"
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)

r = requests.post(
    "https://api.deepai.org/api/waifu2x",
    data={
        'image': response["data"][0]["url"],
    },
    headers={'api-key': 'YOUR WAIFU2X API KEY'}
)
#print(r.json())
if r.status_code == 200:
    data = r.json()
    url = data["output_url"]
    print(url)
else:
    print("API request failed")

@app.route('/')
def index():
    #url = 'https://example.com'  # Replace with your desired URL
    return render_template('index.html', url=url)

if __name__ == '__main__':
    app.run()
