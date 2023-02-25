import requests

cookies = {
    'aws-ubid-main': '947-1320082-7103424',
    'lwa-context': 'e232e57ed50d1b3220955613ca759fad',
    'ubid-main': '134-8272146-7859437',
    'lc-main': 'en_US',
    'i18n-prefs': 'USD',
    'av-timezone': 'America/Chicago',
    'skin': 'noskin',
    'aws_lang': 'en',
    'AMCVS_7742037254C95E840A4C98A6%40AdobeOrg': '1',
    'aws-target-data': '%7B%22support%22%3A%221%22%7D',
    's_cc': 'true',
    'aws-target-visitor-id': '1676671525426-205783.35_0',
    'aws-mkto-trk': 'id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1676671526054-74988',
    'aws-reg-aid': '2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb',
    'aws-reg-guid': '2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb',
    'regStatus': 'registered',
    'aws-userInfo-signed': 'eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjA5ZDVmMGY5LWEzZWQtNDRkYS04Mzk3LWZmMTk5OTg5NGZkMyJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiXC9CXC85MHZ4S0lCcWhPWGNDaytpY0YrTkRZVEtpaWZRZ2hsaUN4MnJYUUtVPSIsImFybiI6ImFybjphd3M6aWFtOjo2Nzk0MTI5MTA5NjI6cm9vdCIsInVzZXJuYW1lIjoic2NyZWVubmFtZTIxIn0.yngmzI2A8FwbVg7rPUg0F_8V-p2W7lawgKoVzBp9z8h3ujnnwzaa52yQE6uQXYvkcZfw6Zzc0rdrx5ZEuTiygvNmk7anZORSPo8Ha5QEgJGKo_NU9Lb8HFR22uGt59LO',
    'aws-userInfo': '%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A679412910962%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22screenname21%22%2C%22keybase%22%3A%22%2FB%2F90vxKIBqhOXcCk%2BicF%2BNDYTKiifQghliCx2rXQKU%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D',
    'noflush_awsccs_sid': 'd3d4c171a049bf83dc8f926ddc7adb025d9fcb4167e24a8aeb0f35e458f6c248',
    'AMCV_7742037254C95E840A4C98A6%40AdobeOrg': '1585540135%7CMCIDTS%7C19411%7CMCMID%7C38290926789321501664128838660354062552%7CMCAAMLH-1677719418%7C7%7CMCAAMB-1677719418%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677121818s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
    's_sq': '%5B%5BB%5D%5D',
    'session-id-apay': '133-6836462-1605452',
    'session-id': '143-7434432-9626530',
    'session-id-time': '2082787201l',
    'session-token': '9CP13kNqZjslb4lUGEF8lmlb25tsEB1uiZDL/YVLk+funRchE88D+H8p68S2ge4K4vMyce1nd9U0RiYQWRmosz8ma0+QbJ4yggNJ1i7e/SdwHbXr0tzhQGYwckVovnNkgHNMiO7hx3Jn8l0aiYhchOCC5M1OCGjrq6Zcc2wdPSeRPihqgBCq/K/QMHL2aeifVea9kKRSt+S4Y002USF0GZQazZbzDzuY3YCnminLpfg',
    'csm-hit': 's-THZQYZ230HT84NF8VFMN|1677351232566',
}

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'aws-ubid-main=947-1320082-7103424; lwa-context=e232e57ed50d1b3220955613ca759fad; ubid-main=134-8272146-7859437; lc-main=en_US; i18n-prefs=USD; av-timezone=America/Chicago; skin=noskin; aws_lang=en; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; aws-target-data=%7B%22support%22%3A%221%22%7D; s_cc=true; aws-target-visitor-id=1676671525426-205783.35_0; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1676671526054-74988; aws-reg-aid=2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb; aws-reg-guid=2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb; regStatus=registered; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjA5ZDVmMGY5LWEzZWQtNDRkYS04Mzk3LWZmMTk5OTg5NGZkMyJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiXC9CXC85MHZ4S0lCcWhPWGNDaytpY0YrTkRZVEtpaWZRZ2hsaUN4MnJYUUtVPSIsImFybiI6ImFybjphd3M6aWFtOjo2Nzk0MTI5MTA5NjI6cm9vdCIsInVzZXJuYW1lIjoic2NyZWVubmFtZTIxIn0.yngmzI2A8FwbVg7rPUg0F_8V-p2W7lawgKoVzBp9z8h3ujnnwzaa52yQE6uQXYvkcZfw6Zzc0rdrx5ZEuTiygvNmk7anZORSPo8Ha5QEgJGKo_NU9Lb8HFR22uGt59LO; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A679412910962%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22screenname21%22%2C%22keybase%22%3A%22%2FB%2F90vxKIBqhOXcCk%2BicF%2BNDYTKiifQghliCx2rXQKU%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; noflush_awsccs_sid=d3d4c171a049bf83dc8f926ddc7adb025d9fcb4167e24a8aeb0f35e458f6c248; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19411%7CMCMID%7C38290926789321501664128838660354062552%7CMCAAMLH-1677719418%7C7%7CMCAAMB-1677719418%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677121818s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_sq=%5B%5BB%5D%5D; session-id-apay=133-6836462-1605452; session-id=143-7434432-9626530; session-id-time=2082787201l; session-token=9CP13kNqZjslb4lUGEF8lmlb25tsEB1uiZDL/YVLk+funRchE88D+H8p68S2ge4K4vMyce1nd9U0RiYQWRmosz8ma0+QbJ4yggNJ1i7e/SdwHbXr0tzhQGYwckVovnNkgHNMiO7hx3Jn8l0aiYhchOCC5M1OCGjrq6Zcc2wdPSeRPihqgBCq/K/QMHL2aeifVea9kKRSt+S4Y002USF0GZQazZbzDzuY3YCnminLpfg; csm-hit=s-THZQYZ230HT84NF8VFMN|1677351232566',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '2',
    'ect': '4g',
    'origin': 'https://www.amazon.com',
    'referer': 'https://www.amazon.com/s?rh=n%3A14772275011&fs=true&ref=lp_14772275011_sar',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '2',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-viewport-width': '921',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'viewport-width': '921',
    'x-amazon-rush-fingerprints': 'AmazonRushAssetLoader:FA8C7663B3FF77B8D395892611BD8B51E11DDC9A|AmazonRushFramework:CA41335B681F294A3B1E0058B3275D5B04EA30BB|AmazonRushRouter:0C480B6E6ADDE302CE1DA35FD38AA37A5B28C583',
    'x-amazon-s-fallback-url': 'https://www.amazon.com/s?fs=true&i=popular&page=3&ref=is_ps_2&rh=n%3A14772275011',
    'x-amazon-s-mismatch-behavior': 'FALLBACK',
    'x-amazon-s-swrs-version': '770BD429BFBF7C4B452530EF59060EBC,D41D8CD98F00B204E9800998ECF8427E',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'fs': 'true',
    'i': 'popular',
    'page': '3',
    'ref': 'is_ps_2',
    'rh': 'n:14772275011',
}

json_data = {
    'progressiveScroll': True,
    'wIndexMainSlot': 48,
    'customer-action': 'query',
}

response = requests.get('https://www.amazon.com/s/query', params=params, cookies=cookies, headers=headers, json=json_data)

text = response.json()

print(text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"progressiveScroll":true,"wIndexMainSlot":48,"customer-action":"query"}'
#response = requests.post('https://www.amazon.com/s/query', params=params, cookies=cookies, headers=headers, data=data)