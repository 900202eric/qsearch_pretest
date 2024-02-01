startTimeStamp = 1706533200 # GMT TIME: 29 Jan 2024 01:00:00 PM => +8: 29 Jan 2024 09:00:00 PM

base_url = "https://www.tiktok.com/api/post/item_list/"

params = "?WebIdLastTime=1706513065&\
aid=1988&app_language=zh-Hant-TW&\
app_name=tiktok_web&\
browser_language=zh-TW&\
browser_name=Mozilla&\
browser_online=true&\
browser_platform=MacIntel&\
browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36&\
channel=tiktok_web&\
cookie_enabled=true&\
count=35&\
coverFormat=2&\
cursor=0&\
device_id=7329417736777172482&\
device_platform=web_pc&\
focus_state=true&\
from_page=user&\
history_len=3&\
is_fullscreen=false&\
is_page_visible=true&\
language=zh-Hant-TW&\
os=mac&\
priority_region=&\
referer=&\
region=TW&\
screen_height=1154&\
screen_width=909&\
secUid=MS4wLjABAAAAJIomeXV1JCW4_bS7h6mx4Ftf4pM9eYpW30KW1f3834SvpVXO0vHfuwBUGSWjE0PY&\
tz_name=Asia%2FTaipei&\
webcast_language=zh-Hant-TW&\
msToken=kfu2m-qLwSkajAtIJddTjAgq_1sXLVW5IGSg5STNf8dPmeXmPohMD7ly5hTm5LmWmjwsSz3BWnbQ__IlOerlg4u2U3DHP9tTWy1DMJ3l0GcjgaLVYjaOZCuVdPuS-FBLvyiKnS4Bt9Xl9YU=&\
X-Bogus=DFSzswVO11XANcNgtE/vOt9WcBn3&\
_signature=_02B4Z6wo00001YbmW2wAAIDBhuZbb-S4Q.GG5l.AAAQPac"

headers = {
  'authority': 'www.tiktok.com',
  'accept': '*/*',
  'accept-language': 'zh-TW,zh;q=0.6',
  'referer': 'https://www.tiktok.com/@geevideo',
  'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


# visual.py const
dataPath = '/Users/huangweichen/Desktop/job/qsearch/problem3/pull_data/data'
filePath = '/Users/huangweichen/Desktop/job/qsearch/problem3/'
order = [
  'fetchDataTime',
  'id',
  'colors',
  'createTime',
  'collectCount',
  'delta_collectCount',
  'commentCount',
  'delta_commentCount',
  'diggCount',
  'delta_diggCount',
  'playCount',
  'delta_playCount',
  'shareCount',
  'desc'
]