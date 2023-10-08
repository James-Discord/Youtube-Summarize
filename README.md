
# YouTube Video Summarizer

This YouTube video summarizer tool uses Nova AI (formerly known as GPT-3.5 Turbo) to generate concise summaries of YouTube videos. It extracts the transcript of a given YouTube video, summarizes the content using Nova AI, and provides a structured summary in a predefined format. You can interact with it through curl requests.

# Features

- Extracts video transcripts using the YouTube Transcript API.
- Utilizes Nova AI to generate video summaries.
- Provides a structured summary with titles, summary, and highlights.
- Can handle videos with or without transcripts.

# Getting Started

Follow these steps to set up and use the YouTube Video Summarizer:

# Clone this GitHub repository to your local machine:
```git clone https://github.com/James-Discord/Youtube-Summarize```

# Install the required Python libraries using pip:
```pip install flask requests pytube youtube-transcript-api```

# Obtain your Nova AI API key by signing up at Nova AI. Replace 'NOVA_AI_KEY' in the nova_api_key variable within the code with your actual Nova AI API key.

# Start the Flask application:
```python app.py```


# Usage with curl

You can use curl to interact with the YouTube Video Summarizer as follows:

# Summarize a YouTube video by providing its URL:
```curl -X POST -d "youtube_url=https://www.youtube.com/watch?v=VIDEO_ID" http://localhost:5000/```

Replace VIDEO_ID with the actual video ID you want to summarize.
The tool will return the summarized content in the predefined format.
Structure of Summaries

The generated summaries follow this structure:

Title
The title of the YouTube video.

Summary
A concise summary of the video's content.

Highlights
[Emoji] Bulletpoint
[Emoji] Bulletpoint
...
Each highlight is a brief, bullet-pointed summary of a key point in the video content, starting with a short highlight and an appropriate emoji.

# Example Response

Here's an example response you might receive when using curl:

```### Jan Böhmermann ist Humor Polizist, Richter und Henker | SinansWoche DIE SHOW

### Summary
This video is an episode of the show "SinansWoche" where the comedian Sinan G talks about Jan Böhmermann, who is known for his satirical and political commentary. Sinan G discusses Böhmermann's role as a humor "policeman," "judge," and "executioner." He dives into Böhmermann's controversial actions, such as his poem about Turkish President Erdogan, and debates whether his provocative style of comedy is necessary or too far-reaching.

#### Highlights
- 🎤 Jan Böhmermann's role as a humor "policeman," "judge," and "executioner"
- 🗣️ Discussing Böhmermann's controversial actions, including his poem about Erdogan
- 🤔 Debating if Böhmermann's style of comedy is necessary or excessive
You now have a YouTube Video Summarizer set up and ready for use with curl requests. Enjoy summarizing your favorite YouTube videos with ease.

Note: Keep your Nova AI API key confidential and secure.```
