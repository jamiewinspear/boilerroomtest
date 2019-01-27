import requests
from boilerroomyoutube.models import YoutubeVideo

BASE_URL = 'https://www.googleapis.com/youtube/v3/search'


def get_latest_youtube_video(channel_id, api_key):
    extras = "maxResults=1&order=date&type=video"
    return requests.get(BASE_URL + '?part=snippet&channelId={}&{})&key={}'
                        .format(channel_id, extras, api_key)).json()


def create_youtube_video(resp_json):
    etag = resp_json['etag']
    url = resp_json['items'][0]['snippet']['thumbnails']['default']['url']
    title = resp_json['items'][0]['snippet']['title']
    published_at = resp_json['items'][0]['snippet']['publishedAt']
    channel_id = resp_json['items'][0]['snippet']['channelId']
    return YoutubeVideo.objects.create(etag=etag, url=url, title=title,
                                       published_at=published_at,
                                       channel_id=channel_id)
