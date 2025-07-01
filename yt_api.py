import requests

API_KEY = 'YOUR_YOUTUBE_API_KEY'  # Replace this with your actual key

def get_video_data(video_id):
    # Get video details
    video_url = (
        f"https://www.googleapis.com/youtube/v3/videos"
        f"?part=snippet,statistics&id={video_id}&key={API_KEY}"
    )
    try:
        video_response = requests.get(video_url)
        video_data = video_response.json()
        if not video_data["items"]:
            return None
        video = video_data["items"][0]
        channel_id = video["snippet"]["channelId"]

        # Get channel details
        channel_url = (
            f"https://www.googleapis.com/youtube/v3/channels"
            f"?part=statistics&id={channel_id}&key={API_KEY}"
        )
        channel_response = requests.get(channel_url)
        channel_data = channel_response.json()
        subscribers = channel_data["items"][0]["statistics"].get("subscriberCount", "Hidden")

        return {
            "title": video["snippet"]["title"],
            "channel": video["snippet"]["channelTitle"],
            "views": video["statistics"]["viewCount"],
            "likes": video["statistics"].get("likeCount", "Hidden"),
            "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
            "published": video["snippet"]["publishedAt"][:10],
            "subscribers": subscribers
        }
    except Exception as e:
        return {"error": str(e)}
