import requests
from flask import Flask, request
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

# Set your OpenAI API key and base URL
nova_api_key = 'NOVA_AI_KEY'

# Function to extract video ID from a YouTube URL
def extract_video_id(url):
    parts = url.split("?")
    if len(parts) > 1:
        params = parts[1].split("&")
        for param in params:
            key, value = param.split("=")
            if key == "v":
                return value
    return None

# Function to get transcript for a video using its ID
def get_youtube_transcript(video_url):
    video_id = extract_video_id(video_url)

    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return transcript
        except Exception as e:
            print(f"Error fetching transcript: {str(e)}")
            return None
    else:
        return None

# Function to get video title using pytube
def get_video_title(video_url):
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Error fetching video title: {str(e)}")
        return None

# Function to summarize text using Nova AI with a custom system prompt
def summarize_text_with_nova_ai(video_title, text):
    if text:
        system_prompt = f"Title: **{video_title}**\n" + (
            "Your output should use the following template:\n"
            "### Title\n"
            "### Summary\n"
            "### Highlights\n"
            "- [Emoji] Bulletpoint\n\n"
            "Your task is to summarize the text I have given you in up to seven concise bullet points, starting with a short highlight. Choose an appropriate emoji for each bullet point."
        )
    else:
        system_prompt = f"Title: **{video_title}**\n" + (
            "Your output should use the following template:\n"
            "### Title\n"
            "### Summary\n"
            "####Highlights\n"
            "- [Emoji] Bulletpoint\n\n"
            "Your task is to summarize the video title with the information you know. I have given you in up to seven concise bullet points, starting with a short highlight. Choose an appropriate emoji for each bullet point."
        )

    nova_api_url = 'https://api.nova-oss.com/v1/chat/completions'
    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
    }

    # Include the user message content only if there's text available
    if text:
        data["messages"].append({
            "role": "user",
            "content": f"{video_title} {text}"
        })

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {nova_api_key}"
    }
    response = requests.post(nova_api_url, json=data, headers=headers)

    print("Nova AI API Response:", response.json())  # Print API response to the console

    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data:
            assistant_message = response_data['choices'][0]['message']
            completion_message = assistant_message['content']
            return completion_message

    return video_title  # Return video title if no summary is available

@app.route('/', methods=['POST'])
def index():
    youtube_url = request.form.get('youtube_url')
    transcript = get_youtube_transcript(youtube_url)
    video_title = get_video_title(youtube_url)

    if transcript:
        # Extract text from the transcript
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        summary = summarize_text_with_nova_ai(video_title, transcript_text)
    else:
        summary = summarize_text_with_nova_ai(video_title, None)

    return summary

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
