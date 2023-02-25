import json
import time
import requests
import json

def lambda_handler(event, context):

    vinylArr = []
    
    cookies = {
        'TealeafAkaSid': 'mh7cYCXaQAo5_tQqQAzb89Hydi38el3Q',
        'visitorId': '0186612F72AD020192513D4B25087EDC',
        'sapphire': '1',
        'UserLocation': '79364|33.440|-101.650|TX|US',
        'fiatsCookie': 'DSI_83|DSN_Lubbock%20University%20Ave|DSZ_79423',
        'ci_pixmgr': 'other',
        '_gcl_au': '1.1.538189206.1676667753',
        '_ga': 'GA1.2.1619494967.1676668624',
        '__gads': 'ID=745146e152674252:T=1676750262:S=ALNI_MazrU5IZnHEVSWlbvC_m-K10KC25g',
        '__gpi': 'UID=0000094a135050e5:T=1676750262:RT=1676750262:S=ALNI_MZWX-O5SR8Z59c8VgHNHpd6TJ2geQ',
        'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMWU1NjFhZi1hNThjLTRkYWItODdjMS04YTkwMDIxMGZjY2YiLCJpc3MiOiJNSTYiLCJleHAiOjE2NzY4NDA3NDAsImlhdCI6MTY3Njc1NDM0MCwianRpIjoiVEdULjgwMWViZmViNjU4NzRmZmFiZTA3ZDk1OTIxMGMxOTk0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImM0Njg3NzIwMDY4ZmVmODBiNjZjZDk0NDIzZTEzZTA4NTk2N2JkYzUxOTI1NmQ2OGM4MTk3OGRhNzUzNDcwMTMiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.iiHVg0I8wSD2hI9yROUMolqcjUOUyQqMSNWh26zaOLwn0ZKJkQ8Njc2RxjuzWOvvzIhh4nBGUsfISnELBeInEi_AzC1P1sC-RO_DuN4xMZrUteNDpVFaKwh9gZ-GrU9bLoIBUj3xndBPekbwRdZS5TazCZUhjo5T7Yqr5x38wG3zsbOu4JUNHvMJfPStu8dpfh3dARk2xbNKBQA40bgyyh-P93qCTLdEMfUhs2kPm7DSwUE8EPCX4PoJtZ_J9TJ1Iyy0VmjDDRJ4k2cjvAREl5dKKZnUD0DRLmgfVgZEYE7rmNQk2J3E502Jl4YdSA4wecsX2gqWMxE2X8gA0pTp7w',
        'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIwMWU1NjFhZi1hNThjLTRkYWItODdjMS04YTkwMDIxMGZjY2YiLCJpc3MiOiJNSTYiLCJleHAiOjE2NzY4NDA3NDAsImlhdCI6MTY3Njc1NDM0MCwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
        'refreshToken': 'FmGlKqNPshkQPpEDDyjF0nl5CmyN_y7EY060Gh6SRnOK4xKhrRutqALxoOm-FLQmovZ9aHhBhj90Pk8M-x3vSg',
        '_mitata': 'MGFlMzI4YWE3ZDYwZDNlOTBmMjY5MmM4M2NmMDM2ZDA2NGVkODg0YWUzNGE5ZGQ4M2VkZWJmNTVlMzA4NDNkOQ==_/@#/1676761227_/@#/ctnXdTClgORooqSD_/@#/MDZjNGNmYWFlYjhmOTNjZGQ5NTgyMDcxOGE0ZWVmOWY3YTgwMDE3MWNhYzdjODYyZjZiMTY1MDQyY2FkMDM4OQ==_/@#/000',
        'ffsession': '{%22sessionHash%22:%229316a55e22a721676667747678%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=vinyl%22%2C%22prevSearchTerm%22:%22vinyl%22%2C%22sessionHit%22:31}',
        '_uetsid': '65a1dad0af0611ed8f463541a41dd873',
        '_uetvid': '65a1f630af0611edafaeeb821e37aa76',
    }
    
    headers = {
        'authority': 'redsky.target.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'TealeafAkaSid=mh7cYCXaQAo5_tQqQAzb89Hydi38el3Q; visitorId=0186612F72AD020192513D4B25087EDC; sapphire=1; UserLocation=79364|33.440|-101.650|TX|US; fiatsCookie=DSI_83|DSN_Lubbock%20University%20Ave|DSZ_79423; ci_pixmgr=other; _gcl_au=1.1.538189206.1676667753; _ga=GA1.2.1619494967.1676668624; __gads=ID=745146e152674252:T=1676750262:S=ALNI_MazrU5IZnHEVSWlbvC_m-K10KC25g; __gpi=UID=0000094a135050e5:T=1676750262:RT=1676750262:S=ALNI_MZWX-O5SR8Z59c8VgHNHpd6TJ2geQ; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMWU1NjFhZi1hNThjLTRkYWItODdjMS04YTkwMDIxMGZjY2YiLCJpc3MiOiJNSTYiLCJleHAiOjE2NzY4NDA3NDAsImlhdCI6MTY3Njc1NDM0MCwianRpIjoiVEdULjgwMWViZmViNjU4NzRmZmFiZTA3ZDk1OTIxMGMxOTk0LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImM0Njg3NzIwMDY4ZmVmODBiNjZjZDk0NDIzZTEzZTA4NTk2N2JkYzUxOTI1NmQ2OGM4MTk3OGRhNzUzNDcwMTMiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.iiHVg0I8wSD2hI9yROUMolqcjUOUyQqMSNWh26zaOLwn0ZKJkQ8Njc2RxjuzWOvvzIhh4nBGUsfISnELBeInEi_AzC1P1sC-RO_DuN4xMZrUteNDpVFaKwh9gZ-GrU9bLoIBUj3xndBPekbwRdZS5TazCZUhjo5T7Yqr5x38wG3zsbOu4JUNHvMJfPStu8dpfh3dARk2xbNKBQA40bgyyh-P93qCTLdEMfUhs2kPm7DSwUE8EPCX4PoJtZ_J9TJ1Iyy0VmjDDRJ4k2cjvAREl5dKKZnUD0DRLmgfVgZEYE7rmNQk2J3E502Jl4YdSA4wecsX2gqWMxE2X8gA0pTp7w; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIwMWU1NjFhZi1hNThjLTRkYWItODdjMS04YTkwMDIxMGZjY2YiLCJpc3MiOiJNSTYiLCJleHAiOjE2NzY4NDA3NDAsImlhdCI6MTY3Njc1NDM0MCwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=FmGlKqNPshkQPpEDDyjF0nl5CmyN_y7EY060Gh6SRnOK4xKhrRutqALxoOm-FLQmovZ9aHhBhj90Pk8M-x3vSg; _mitata=MGFlMzI4YWE3ZDYwZDNlOTBmMjY5MmM4M2NmMDM2ZDA2NGVkODg0YWUzNGE5ZGQ4M2VkZWJmNTVlMzA4NDNkOQ==_/@#/1676761227_/@#/ctnXdTClgORooqSD_/@#/MDZjNGNmYWFlYjhmOTNjZGQ5NTgyMDcxOGE0ZWVmOWY3YTgwMDE3MWNhYzdjODYyZjZiMTY1MDQyY2FkMDM4OQ==_/@#/000; ffsession={%22sessionHash%22:%229316a55e22a721676667747678%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=vinyl%22%2C%22prevSearchTerm%22:%22vinyl%22%2C%22sessionHit%22:31}; _uetsid=65a1dad0af0611ed8f463541a41dd873; _uetvid=65a1f630af0611edafaeeb821e37aa76',
        'origin': 'https://www.target.com',
        'referer': 'https://www.target.com/s?searchTerm=vinyl',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    }
    
    
    
    
    def requestTarget(offset=0):
      response = requests.get(
        'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
        params = {
        'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
        'channel': 'WEB',
        'count': '24',
        'default_purchasability_filter': 'true',
        'include_sponsored': 'true',
        'keyword': 'vinyl',
        'offset': f'{offset}',
        'page': '/s/vinyl',
        'platform': 'mobile',
        'pricing_store_id': '83',
        'store_ids': '83,2190,770',
        'useragent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
        'visitor_id': '0186612F72AD020192513D4B25087EDC',
        'zip': '79364',
        },
        cookies=cookies,
        headers=headers,
      )
      formatAsJson(response, offset)
    
    def formatAsJson(response, offset):
      json_formatted_str = json.loads(response.text)
    
      turnJSONintoReadable(json_formatted_str, offset)
    
    
    def turnJSONintoReadable(json_formatted_str, offset):
      products = json_formatted_str['data']['search']['products']
      for product in products:
        vinylArr.append(product['item']['product_description']['title'])
      offset+=24
      time.sleep(.1)
      try:
        requestTarget(offset)
      except:
        print(vinylArr)
    
    requestTarget()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
