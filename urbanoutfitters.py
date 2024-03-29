import json
import time
import requests
from pymongo import MongoClient

print("start")

cookies2 = {
    'localredirected': 'False',
    'siteId': 'uo-us',
    'urbn_channel': 'web',
    'urbn_currency': 'USD',
    'urbn_site_id': 'uo-us',
    'urbn_language': 'en-US',
    'akacd_ss1': '3819242590~rv=94~id=425eec0ece81466c92805b3fa28c479c',
    '_dy_csc_ses': 't',
    'urbn_mbr_market_b': 'true',
    'urbn_device_type': 'LARGE',
    'urbn_browser_notification_permission': 'default',
    'pxcts': 'a60fd34c-1165-11ed-9816-4762756e6c61',
    'SSLB': '1',
    'urbn_data_center_id': 'US-NV',
    'urbn_geo_region': 'US-NV',
    'urbn_tracer': 'MBV3SBWBIH',
    'urbn_uuid': '7ffa354e-7de1-45e4-b49c-5f8e36e262bc',
    'urbn_clear': 'true',
    'AKA_A2': 'A',
    'urbn_device_info': 'web%7Cother%7Cdesktop',
    '_pxvid': 'b73e3179-cc17-11ed-b9c9-76715945484c',
    'urbn_page_visits_count': '%7B%22uo-us%22%3A4%7D',
    'urbn_bypass_email_signup': 'true',
    'urbn_email_signup_marketing_optin': 'true',
    'ss-disable-dy': '1',
    'urbn_disable_dy': '1',
    'SSSC': '472.G7214959945752517267.2|60555.2150500:69548.2338073:69595.2339335:70403.2359051:72936.2404430:73038.2406240:73128.2408241:73447.2414759:73487.2415428:73639.2418160',
    'urbn_auth_payload': '%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY3OTg2Njc5Ny4zMTgxNTE3LCJpYXQiOjE2Nzk4NjYxOTcuMzE4MTUxNywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE2Nzk4NjM3NjguMzI4MTg5OCwgXCJwcm9maWxlSWRcIjogXCJGeUkvcTZGVjZsS1R6NGQwUEFWZDlyb0c0VUlvcDNYWnNTaHFWZ3JIcEZlYzE0N1ZLTjJXWmpQdzFJQTlRUUltNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09OWJlMmQ1Y2Q1YzE5YWU5Y2Q3NmRmOGEwN2E2MmFlM2YxMDk2ZjlkZTg2ZTA4ZmFhZjdlNmJlMzc4MzEyYjJkM1wiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIk1CVjNTQldCSUhcIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJVUy1OVlwiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiVFhcIn0sIFwiY2FydElkXCI6IFwiMGgrUWxnTG1OcndQTWtMQWViU2NpWkpCdW9XZ0RVYjZqSGs0cFVCRXJBNWMrYWpYaHpjZmowQUhUZFd4M00vRDVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PThhMGZhNDAzN2ViZTNhZjcwM2IyZTc5YWM2NjM0NDA2MWQ1MjMwZmM0NmEyZGMxYWE1Mzg0OTUxZmY3ZTQ5NWZcIn0ifQ.v2xYzUkPW84eS6u4ctpNqv8rOti6e_yM0Bh2fs7H840%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY5NTQxODE5Ny4zMTg1MTEsImlhdCI6MTY3OTg2NjE5Ny4zMTg1MTEsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNjc5ODY2MTk3LjMxODQ5ODEsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwidHJhY2VyXCI6IFwiTUJWM1NCV0JJSFwiLCBcInByb2ZpbGVJZFwiOiBcIkZ5SS9xNkZWNmxLVHo0ZDBQQVZkOXJvRzRVSW9wM1hac1NocVZnckhwRmVjMTQ3VktOMldaalB3MUlBOVFRSW01VSszcnMycnhoam00cEQzMENjSUJ3PT05YmUyZDVjZDVjMTlhZTljZDc2ZGY4YTA3YTYyYWUzZjEwOTZmOWRlODZlMDhmYWFmN2U2YmUzNzgzMTJiMmQzXCJ9In0.-zjrHu8caluCHHU4cLJ_eCGMlLwx-64dM4sjgYjInJ8%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22MBV3SBWBIH%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22US-NV%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22TX%22%2C%22country%22%3A%22US%22%2C%22city%22%3A%22LUBBOCK%22%2C%22zipCodes%22%3A%2279401-79404%2C79406-79416%2C79423-79424%2C79430%2C79452-79453%2C79457%2C79464%2C79490-79491%2C79493%2C79499%22%7D%2C%22trueClientIp%22%3A%2266.205.103.87%22%2C%22createdAt%22%3A1679866197324%2C%22authExpiresTime%22%3A1679866677.324%2C%22reauthExpiresTime%22%3A1695418197.324%7D',
    'SS_IMAGE_VIEWER_VARIANT': '0',
    'SSRT': 'd7sgZAADAA',
    'urbn_uuid_session': 'ed028cba-bd29-4126-8c6a-7e7fab23b3ad',
    'urbn_edgescape_site_id': 'uo-uk',
    'urbn_inventory_pool': 'INTL_DIRECT',
    'urbn_country': 'NL',
    'SSID': 'CQCZFB2MAAAAAADYryBkkxpAG9ivIGQCAAAAAAAETftlVbkgZAAU-eceAQOn2CQA2K8gZAIApx8BAfDlJABVuSBkAQDbDwEDB7IjANivIGQCAKgdAQMxvyQA2K8gZAIATh0BA2C3JADYryBkAgCsDwEDGa0jANivIGQCAAMTAQML_yMA2K8gZAIAi-wAAWTQIABVuSBkAQDoHAEBTrAkAFW5IGQBAA8fAQNE2yQA2K8gZAIA',
    '_px3': '55fd915dee92ff34f26de9db86c52624b218e3e11a0ef2170aca383b9fd58f7d:Kax8iE3fFLC/j5qY617MvNOawZ2A80bq+65sdSZpIzXkoe+RTqJHTM4ba646oIrh9IsQaIZDYwj0XXgP0+zXUg==:1000:aUC1RJKB6UU2nBv8FyIsC3uGHuZEJX1b/uL0RYSAN/iqdSgyHmePW8r4WDRTHcs9WJvoVVBCf9J6d/AhvTaTOj9HVFPnyFKlngyiwOLYlcwY4BLH56vgkyxDb7tLhOZ61MmT6WzG5X6NRm3VhsUSjT06Z8HfqKVlMySvyzqeH9qNexXcsrasjWVWM9uqNqRqCc8X0i/Uxd3NT0pZNwKerg==',
    'akavpau_a15_urbanoutfitters_vp_us': '1679867050~id=9a1395b1b6dd5a853a07ee9d15bb5cf3',
    'utag_main': 'v_id:01871faef8fa00a5352d54b46e480406f002d06700bd0$_sn:2$_se:6$_ss:0$_st:1679868545952$dc_visit:2$ses_id:1679866202663%3Bexp-session$_pn:2%3Bexp-session$isLoggedIn:false%3Bexp-session$dc_event:3%3Bexp-session',
}

headers2 = {
    'authority': 'www.urbanoutfitters.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY3OTg2Njc5Ny4zMTgxNTE3LCJpYXQiOjE2Nzk4NjYxOTcuMzE4MTUxNywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE2Nzk4NjM3NjguMzI4MTg5OCwgXCJwcm9maWxlSWRcIjogXCJGeUkvcTZGVjZsS1R6NGQwUEFWZDlyb0c0VUlvcDNYWnNTaHFWZ3JIcEZlYzE0N1ZLTjJXWmpQdzFJQTlRUUltNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09OWJlMmQ1Y2Q1YzE5YWU5Y2Q3NmRmOGEwN2E2MmFlM2YxMDk2ZjlkZTg2ZTA4ZmFhZjdlNmJlMzc4MzEyYjJkM1wiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIk1CVjNTQldCSUhcIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJVUy1OVlwiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiVFhcIn0sIFwiY2FydElkXCI6IFwiMGgrUWxnTG1OcndQTWtMQWViU2NpWkpCdW9XZ0RVYjZqSGs0cFVCRXJBNWMrYWpYaHpjZmowQUhUZFd4M00vRDVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PThhMGZhNDAzN2ViZTNhZjcwM2IyZTc5YWM2NjM0NDA2MWQ1MjMwZmM0NmEyZGMxYWE1Mzg0OTUxZmY3ZTQ5NWZcIn0ifQ.v2xYzUkPW84eS6u4ctpNqv8rOti6e_yM0Bh2fs7H840',
    'content-type': 'application/json',
    # 'cookie': 'localredirected=False; siteId=uo-us; urbn_channel=web; urbn_currency=USD; urbn_site_id=uo-us; urbn_language=en-US; akacd_ss1=3819242590~rv=94~id=425eec0ece81466c92805b3fa28c479c; _dy_csc_ses=t; urbn_mbr_market_b=true; urbn_device_type=LARGE; urbn_browser_notification_permission=default; pxcts=a60fd34c-1165-11ed-9816-4762756e6c61; SSLB=1; urbn_data_center_id=US-NV; urbn_geo_region=US-NV; urbn_tracer=MBV3SBWBIH; urbn_uuid=7ffa354e-7de1-45e4-b49c-5f8e36e262bc; urbn_clear=true; AKA_A2=A; urbn_device_info=web%7Cother%7Cdesktop; _pxvid=b73e3179-cc17-11ed-b9c9-76715945484c; urbn_page_visits_count=%7B%22uo-us%22%3A4%7D; urbn_bypass_email_signup=true; urbn_email_signup_marketing_optin=true; ss-disable-dy=1; urbn_disable_dy=1; SSSC=472.G7214959945752517267.2|60555.2150500:69548.2338073:69595.2339335:70403.2359051:72936.2404430:73038.2406240:73128.2408241:73447.2414759:73487.2415428:73639.2418160; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY3OTg2Njc5Ny4zMTgxNTE3LCJpYXQiOjE2Nzk4NjYxOTcuMzE4MTUxNywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE2Nzk4NjM3NjguMzI4MTg5OCwgXCJwcm9maWxlSWRcIjogXCJGeUkvcTZGVjZsS1R6NGQwUEFWZDlyb0c0VUlvcDNYWnNTaHFWZ3JIcEZlYzE0N1ZLTjJXWmpQdzFJQTlRUUltNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09OWJlMmQ1Y2Q1YzE5YWU5Y2Q3NmRmOGEwN2E2MmFlM2YxMDk2ZjlkZTg2ZTA4ZmFhZjdlNmJlMzc4MzEyYjJkM1wiLCBcImFub255bW91c1wiOiB0cnVlLCBcInRyYWNlclwiOiBcIk1CVjNTQldCSUhcIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJVUy1OVlwiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiVFhcIn0sIFwiY2FydElkXCI6IFwiMGgrUWxnTG1OcndQTWtMQWViU2NpWkpCdW9XZ0RVYjZqSGs0cFVCRXJBNWMrYWpYaHpjZmowQUhUZFd4M00vRDVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PThhMGZhNDAzN2ViZTNhZjcwM2IyZTc5YWM2NjM0NDA2MWQ1MjMwZmM0NmEyZGMxYWE1Mzg0OTUxZmY3ZTQ5NWZcIn0ifQ.v2xYzUkPW84eS6u4ctpNqv8rOti6e_yM0Bh2fs7H840%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY5NTQxODE5Ny4zMTg1MTEsImlhdCI6MTY3OTg2NjE5Ny4zMTg1MTEsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNjc5ODY2MTk3LjMxODQ5ODEsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwidHJhY2VyXCI6IFwiTUJWM1NCV0JJSFwiLCBcInByb2ZpbGVJZFwiOiBcIkZ5SS9xNkZWNmxLVHo0ZDBQQVZkOXJvRzRVSW9wM1hac1NocVZnckhwRmVjMTQ3VktOMldaalB3MUlBOVFRSW01VSszcnMycnhoam00cEQzMENjSUJ3PT05YmUyZDVjZDVjMTlhZTljZDc2ZGY4YTA3YTYyYWUzZjEwOTZmOWRlODZlMDhmYWFmN2U2YmUzNzgzMTJiMmQzXCJ9In0.-zjrHu8caluCHHU4cLJ_eCGMlLwx-64dM4sjgYjInJ8%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22MBV3SBWBIH%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22US-NV%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22TX%22%2C%22country%22%3A%22US%22%2C%22city%22%3A%22LUBBOCK%22%2C%22zipCodes%22%3A%2279401-79404%2C79406-79416%2C79423-79424%2C79430%2C79452-79453%2C79457%2C79464%2C79490-79491%2C79493%2C79499%22%7D%2C%22trueClientIp%22%3A%2266.205.103.87%22%2C%22createdAt%22%3A1679866197324%2C%22authExpiresTime%22%3A1679866677.324%2C%22reauthExpiresTime%22%3A1695418197.324%7D; SS_IMAGE_VIEWER_VARIANT=0; SSRT=d7sgZAADAA; urbn_uuid_session=ed028cba-bd29-4126-8c6a-7e7fab23b3ad; urbn_edgescape_site_id=uo-uk; urbn_inventory_pool=INTL_DIRECT; urbn_country=NL; SSID=CQCZFB2MAAAAAADYryBkkxpAG9ivIGQCAAAAAAAETftlVbkgZAAU-eceAQOn2CQA2K8gZAIApx8BAfDlJABVuSBkAQDbDwEDB7IjANivIGQCAKgdAQMxvyQA2K8gZAIATh0BA2C3JADYryBkAgCsDwEDGa0jANivIGQCAAMTAQML_yMA2K8gZAIAi-wAAWTQIABVuSBkAQDoHAEBTrAkAFW5IGQBAA8fAQNE2yQA2K8gZAIA; _px3=55fd915dee92ff34f26de9db86c52624b218e3e11a0ef2170aca383b9fd58f7d:Kax8iE3fFLC/j5qY617MvNOawZ2A80bq+65sdSZpIzXkoe+RTqJHTM4ba646oIrh9IsQaIZDYwj0XXgP0+zXUg==:1000:aUC1RJKB6UU2nBv8FyIsC3uGHuZEJX1b/uL0RYSAN/iqdSgyHmePW8r4WDRTHcs9WJvoVVBCf9J6d/AhvTaTOj9HVFPnyFKlngyiwOLYlcwY4BLH56vgkyxDb7tLhOZ61MmT6WzG5X6NRm3VhsUSjT06Z8HfqKVlMySvyzqeH9qNexXcsrasjWVWM9uqNqRqCc8X0i/Uxd3NT0pZNwKerg==; akavpau_a15_urbanoutfitters_vp_us=1679867050~id=9a1395b1b6dd5a853a07ee9d15bb5cf3; utag_main=v_id:01871faef8fa00a5352d54b46e480406f002d06700bd0$_sn:2$_se:6$_ss:0$_st:1679868545952$dc_visit:2$ses_id:1679866202663%3Bexp-session$_pn:2%3Bexp-session$isLoggedIn:false%3Bexp-session$dc_event:3%3Bexp-session',
    'origin': 'https://www.urbanoutfitters.com',
    'referer': 'https://www.urbanoutfitters.com/',
    'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data2 = {
    'reauthToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY5NTQxODE5Ny4zMTg1MTEsImlhdCI6MTY3OTg2NjE5Ny4zMTg1MTEsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNjc5ODY2MTk3LjMxODQ5ODEsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwidHJhY2VyXCI6IFwiTUJWM1NCV0JJSFwiLCBcInByb2ZpbGVJZFwiOiBcIkZ5SS9xNkZWNmxLVHo0ZDBQQVZkOXJvRzRVSW9wM1hac1NocVZnckhwRmVjMTQ3VktOMldaalB3MUlBOVFRSW01VSszcnMycnhoam00cEQzMENjSUJ3PT05YmUyZDVjZDVjMTlhZTljZDc2ZGY4YTA3YTYyYWUzZjEwOTZmOWRlODZlMDhmYWFmN2U2YmUzNzgzMTJiMmQzXCJ9In0.-zjrHu8caluCHHU4cLJ_eCGMlLwx-64dM4sjgYjInJ8',
}

response2 = requests.put(
    cookies=cookies2,
    headers=headers2,
    json=json_data2,
    url = 'https://www.urbanoutfitters.com/slipstream/api/token/v0/uo-us/auth' 
)

print(f'Auth Token Response: {response2.status_code} {response2.reason}')

class Vinyl:
    def __init__(self, title, price, url):
        self.title = title
        self.price = price
        self.url = url

def getAuthToken():
    response = requests.get(
        'https://www.urbanoutfitters.com/slipstream/api/token/v0/uo-us/auth'
    )

    return response.cookies['authToken']

def getDB():
    CONNECTION_STRING = "mongodb+srv://Pacforever:Pacforever@cluster0.xfgz9lp.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client.get_database('webscrapingDb')

db = getDB()
uoTable = db['uo']
vinylArr = []

def getVinylJson(offset,token):
    time.sleep(10)
    response = requests.get(
    'https://www.urbanoutfitters.com/api/catalog/v2/uo-us/pools/US_DIRECT/navigation-items/vinyl-records/products',
    params={
    'page-size': '100',
    'skip': f'{offset}',
    'projection-slug': 'categorytiles',
    'personalization': '0',
    'customer-consent': 'true',
    'countryCode': 'US',
    },
    headers={
    'authority': 'www.urbanoutfitters.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {token}',
    # 'cookie': 'urbn_disable_dy=1; ss-disable-dy=1; SSLB=1; SSSC=472.G7204174183419395435.1|60555.2150500:69489.2336916:69595.2339335:70403.2359051:72863.2402774:72936.2404299:73076.2407129:73095.2407568:73106.2407715:73128.2408241; urbn_clear=true; urbn_language=en-US; urbn_tracer=KBTF361ZZS; urbn_data_center_id=US-NV; siteId=uo-us; urbn_uuid=76a60314-c0fe-4aa5-bf23-040507cb5c07; urbn_site_id=uo-us; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY3NzM1MzExMi4zODMyNDksImlhdCI6MTY3NzM1MjUxMi4zODMyNDksImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNjc3MzUyNTEyLjM3ODI1MTYsIFwicHJvZmlsZUlkXCI6IFwiMmwwOUtpVW55K1lldk9TY3dBOTlwajc5Zm1sOTVCb0ltQ1MzeGFMbW50eVp2cDlWVzJVUEZGeXoyR056TzZkeTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTFjMmM1NTRlMWY1MjQ0MjE5ZTYxYTAxOTFkNTc5NzNjNGU4NDQ5MGEwYTY4NzkwNWVmYzNjZmRmN2IxZDc2ODhcIiwgXCJhbm9ueW1vdXNcIjogdHJ1ZSwgXCJ0cmFjZXJcIjogXCJLQlRGMzYxWlpTXCIsIFwiY2FydElkXCI6IFwiZXFJOTlOdjBLcXA3amdmdGVFajBvcXkzcmlXMko0VGhuZE5hVGJTcWErMmNBVm1jR2ozdWp2RitBMGRlTzhWMTVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTdkY2Q5OWNlOWU1M2NmYjRiYTcyZTIxNDZkYzg3MjFkNTA2ZmQ2Mjg5Y2JiYjgxOGZlZTFiZjM0ZjliN2MxM2ZcIiwgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJzaXRlSWRcIjogXCJ1by11c1wiLCBcImJyYW5kSWRcIjogXCJ1b1wiLCBcInNpdGVHcm91cFwiOiBcInVvLXVzXCIsIFwiZGF0YUNlbnRlcklkXCI6IFwiVVMtTlZcIiwgXCJnZW9SZWdpb25cIjogXCJVUy1OVlwiLCBcImVkZ2VzY2FwZVwiOiB7XCJyZWdpb25Db2RlXCI6IFwiVFhcIn19In0.K34Md6gVZ3DxzGyytr3okxacIslK2vZsBLFti5SAx78%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTY5MjkwNDUxMi4zODM3NTQzLCJpYXQiOjE2NzczNTI1MTIuMzgzNzU0MywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE2NzczNTI1MTIuMzgzNzM3LCBcInNjb3BlXCI6IFtcIkdVRVNUXCJdLCBcInRyYWNlclwiOiBcIktCVEYzNjFaWlNcIiwgXCJwcm9maWxlSWRcIjogXCIybDA5S2lVbnkrWWV2T1Njd0E5OXBqNzlmbWw5NUJvSW1DUzN4YUxtbnR5WnZwOVZXMlVQRkZ5ejJHTnpPNmR5NVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09MWMyYzU1NGUxZjUyNDQyMTllNjFhMDE5MWQ1Nzk3M2M0ZTg0NDkwYTBhNjg3OTA1ZWZjM2NmZGY3YjFkNzY4OFwifSJ9.lojrBgIkpSZTNlQXjQe40oBeV5_e5gUadMDVs1JvUCU%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22KBTF361ZZS%22%2C%22dataCenterId%22%3A%22US-NV%22%2C%22geoRegion%22%3A%22US-NV%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22TX%22%2C%22country%22%3A%22US%22%2C%22city%22%3A%22LUBBOCK%22%2C%22zipCodes%22%3A%2279401-79404%2C79406-79416%2C79423-79424%2C79430%2C79452-79453%2C79457%2C79464%2C79490-79491%2C79493%2C79499%22%7D%2C%22trueClientIp%22%3A%22104.184.110.218%22%2C%22createdAt%22%3A1677352512388%2C%22authExpiresTime%22%3A1677352992.388%2C%22reauthExpiresTime%22%3A1692904512.388%7D; urbn_inventory_pool=US_DIRECT; urbn_edgescape_site_id=uo-us; urbn_currency=USD; urbn_uuid_session=d76d30f7-9a09-41e7-8793-cb36e66de3a3; urbn_geo_region=US-NV; urbn_channel=web; urbn_country=US; localredirected=False; AKA_A2=A; akacd_ss1=3854805311~rv=57~id=fa223ed1e2ef3a6263e88ed71b53d629; urbn_browser_notification_permission=default; urbn_device_info=web%7Cother%7Ctablet; pxcts=bafcdb7c-b540-11ed-8daf-517846727944; _pxvid=bafccbcd-b540-11ed-8daf-517846727944; _px3=8a47775d99114cd5286bcbbda05e738847c507b410bc0a64b4219e7682a68fac:vmq9swF1cXyTDpRJA33GyUMiSIPsWrFijZj6PkcqLSFYnXxDM9qQWQVOmR5MuFgpYyE3nH3LqpybQEySRMls9w==:1000:TlZrj1/FtKHxgd3M0eN5dKiFYhFZo6AMVGgPMnOAKeyt0irXYjdw0m3giHnALvbmxtl/vRrde4nF9UX0ufXRlNHsI9xG1dxl/pD6u8CE5g5De8sLaluVtFS+mkc/MVZ/3+nH6kSPgxjDkcIqnWgC/I4IYAOt40XH0nODmAOujPh/swkCULr0Y5H7HtE1GoxJfnsDY2FpYC4T5jOg7tUkug==; _gid=GA1.2.812090327.1677352517; _gac_UA-45103817-1=1.1677352517.Cj0KCQiAgOefBhDgARIsAMhqXA61SU-PbRW9tenTIqgNTNK-rzAN6OEXyEr_q1v5AuBBIxXqEZXBnAwaAup0EALw_wcB; rmStore=amid:43176; _uetsid=bcd953f0b54011ed9f02759b0c2b736f; _uetvid=0edd0f30433511ed86c939f78d7e7e4a; _rdt_uuid=1677352517004.3f7b5191-d273-4fcc-a518-f1f0614d1de5; _svsid=051345df110db107b23a8e96b25f7b9e; btIdentify=02d123eb-d06c-48ad-dfb7-50a01cbe6647; _bts=d59016c3-8b7b-4c95-fd4c-d65f2bf2c044; _gat_tealium_0=1; tpc_a=70933ea5316944108961382dc5a3f006.1677352517.3EO.1677352517; __attentive_id=ef7387abea4747d795a4d9ae43969c03; _attn_=eyJ1Ijoie1wiY29cIjoxNjc3MzUyNTE3Njg4LFwidW9cIjoxNjc3MzUyNTE3Njg4LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImVmNzM4N2FiZWE0NzQ3ZDc5NWE0ZDlhZTQzOTY5YzAzXCJ9In0=; __attentive_cco=1677352517692; __attentive_utm_param_medium=cpc; __attentive_utm_param_source=google; __attentive_utm_param_campaign=%255BBrand%2520Text%255D%2520-%2520UO%2520-%2520Lifestyle%2520-%2520Music%2520-%2520Exact; __attentive_utm_param_content=UO%2520-%2520Vinyl; __attentive_utm_param_term=urban%2520outfitters%2520vinyl; _bti=%7B%22app_id%22%3A%22urban-outfitters%22%2C%22bsin%22%3A%22dQ37M1sABOK7Iw37y%2FU7pXMc9NSo0vhkzOM7MpyyOxBR6cyy3CWvi8avZgghlJb2rrlljTOMK%2FF9SS5Lzt68fw%3D%3D%22%2C%22is_identified%22%3Afalse%7D; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+25+2023+13%3A15%3A18+GMT-0600+(Central+Standard+Time)&version=6.38.0&isIABGlobal=false&hosts=&consentId=76a60314-c0fe-4aa5-bf23-040507cb5c07&interactionCount=0&landingPath=https%3A%2F%2Fwww.urbanoutfitters.com%2Fvinyl-records-cassettes%3Futm_medium%3Dcpc%26utm_source%3Dgoogle%26utm_campaign%3D%255BBrand%2520Text%255D%2520-%2520UO%2520-%2520Lifestyle%2520-%2520Music%2520-%2520Exact%26utm_content%3DUO%2520-%2520Vinyl%26utm_term%3Durban%2520outfitters%2520vinyl%26creative%3D537551982924%26device%3Dm%26matchtype%3De%26network%3Dg%26utm_kxconfid%3Dvx6q4l3b6%26gclid%3DCj0KCQiAgOefBhDgARIsAMhqXA61SU-PbRW9tenTIqgNTNK-rzAN6OEXyEr_q1v5AuBBIxXqEZXBnAwaAup0EALw_wcB%26gclsrc%3Daw.ds&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _gcl_au=1.1.1088257095.1677352519; _ga=GA1.1.1262285152.1677352517; _pin_unauth=dWlkPU1UWTJZMlk0TkdVdFpXUXdPQzAwTWpnMkxUaG1NbUl0WVRCbFptSTFORGMzTWpVMA; __attentive_dv=1; _tt_enable_cookie=1; _ttp=68j_DENn7iZ5Kp_qMFGe2TjfLRH; __attentive_ss_referrer=https://www.google.com/; cebs=1; _ce.s=v~8b4afea754108b0c1071739af2d4840f451e4bac~vpv~0; _ce.clock_event=1; _ce.clock_data=225%2C104.184.110.218; _gcl_aw=GCL.1677352531.Cj0KCQiAgOefBhDgARIsAMhqXA61SU-PbRW9tenTIqgNTNK-rzAN6OEXyEr_q1v5AuBBIxXqEZXBnAwaAup0EALw_wcB; _gcl_dc=GCL.1677352531.Cj0KCQiAgOefBhDgARIsAMhqXA61SU-PbRW9tenTIqgNTNK-rzAN6OEXyEr_q1v5AuBBIxXqEZXBnAwaAup0EALw_wcB; urbn_page_visits_count=%7B%22uo-us%22%3A2%7D; cebsp_=2; urbn_email_signup_marketing_optin=true; akavpau_a15_urbanoutfitters_vp_us=1677352860~id=ecdb87f03b0de62096892011df0cb688; RT="z=1&dm=www.urbanoutfitters.com&si=2c9125e1-5153-4679-b5e6-fa59fff2d598&ss=lekcdl7a&sl=1&tt=113q&rl=1&ld=114i&nu=1fbtr143e&cl=1aod"; SSRT=fl76YwADAA; SSID=CQBpxh2MAAAAAABAXvpja73AHkBe-mMBAAAAAABs-9RlQF76YwAU-egcAQPLryQAQF76YwEAi-wAAWTQIABAXvpjAQCfHAED1qkkAEBe-mMBAJIdAQEjvSQAQF76YwEAcQ8BA5SoIwBAXvpjAQCoHQEDMb8kAEBe-mMBANsPAQMHsiMAQF76YwEAhx0BAZC8JABAXvpjAQB0HQEB2bokAEBe-mMBAAMTAQEL_yMAQF76YwEA; _ga_BBMWPLK0E5=GS1.1.1677352518.1.1.1677352574.4.0.0; utag_main=v_id:01868a0034b80021948dd1ce93b00008301a407b006ca$_sn:1$_se:5$_ss:0$_st:1677354374930$ses_id:1677352514746%3Bexp-session$_pn:1%3Bexp-session$isLoggedIn:false%3Bexp-session$dc_visit:1$dc_event:3%3Bexp-session$dc_region:us-east-1%3Bexp-session; __attentive_pv=6',
    'referer': 'https://www.urbanoutfitters.com/vinyl-records',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'x-urbn-channel': 'web',
    'x-urbn-country': 'US',
    'x-urbn-currency': 'USD',
    'x-urbn-experience': 'ss',
    'x-urbn-geo-region': 'US-NV',
    'x-urbn-language': 'en-US',
    'x-urbn-primary-data-center-id': 'US-NV',
    'x-urbn-site-id': 'uo-us',
    },
    )
    
    print(f'Urban Response Code: {response.status_code} {response.reason}')
    insertVinylInfo(response.json(), offset, token)

def insertVinylInfo(data, offset, token):

    for record in data['records']:
      vinyl = {
        'title': record['allMeta']['tile']['product']['displayName'],
        'url': f"https://www.urbanoutfitters.com/shop/{record['allMeta']['tile']['product']['productSlug']}",
        'price': str(record['allMeta']['tile']['skuInfo']['listPriceLow']),
        'image': f"https://images.urbndata.com/is/image/UrbanOutfitters/{record['allMeta']['tile']['faceOutImage']}"
      }
      print(json.dumps(record, indent=2))
      vinylArr.append(vinyl)
      
    if offset == 2000:
        uoTable.delete_many({})
        uoTable.insert_many(vinylArr)
        return
    print(offset)

    try:
        getVinylJson(offset + 100, token)
    except:
        uoTable.delete_many({})
        uoTable.insert_many(vinylArr)
        print('done')
    
getVinylJson(0,response2.json()["authToken"])