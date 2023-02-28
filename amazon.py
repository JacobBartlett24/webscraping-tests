from bs4 import BeautifulSoup
import requests

import requests

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'max-age=0',
    'cookie': 'aws-ubid-main=947-1320082-7103424; lwa-context=e232e57ed50d1b3220955613ca759fad; ubid-main=134-8272146-7859437; lc-main=en_US; i18n-prefs=USD; av-timezone=America/Chicago; skin=noskin; aws_lang=en; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1676671525426-205783.35_0; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1676671526054-74988; aws-reg-aid=2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb; aws-reg-guid=2f20aa7796fc7693a36041774e08b0b280c9d47172bacd49de2794b3b88b37eb; regStatus=registered; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjA5ZDVmMGY5LWEzZWQtNDRkYS04Mzk3LWZmMTk5OTg5NGZkMyJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiXC9CXC85MHZ4S0lCcWhPWGNDaytpY0YrTkRZVEtpaWZRZ2hsaUN4MnJYUUtVPSIsImFybiI6ImFybjphd3M6aWFtOjo2Nzk0MTI5MTA5NjI6cm9vdCIsInVzZXJuYW1lIjoic2NyZWVubmFtZTIxIn0.yngmzI2A8FwbVg7rPUg0F_8V-p2W7lawgKoVzBp9z8h3ujnnwzaa52yQE6uQXYvkcZfw6Zzc0rdrx5ZEuTiygvNmk7anZORSPo8Ha5QEgJGKo_NU9Lb8HFR22uGt59LO; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A679412910962%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22screenname21%22%2C%22keybase%22%3A%22%2FB%2F90vxKIBqhOXcCk%2BicF%2BNDYTKiifQghliCx2rXQKU%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; noflush_awsccs_sid=d3d4c171a049bf83dc8f926ddc7adb025d9fcb4167e24a8aeb0f35e458f6c248; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19411%7CMCMID%7C38290926789321501664128838660354062552%7CMCAAMLH-1677719418%7C7%7CMCAAMB-1677719418%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677121818s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_sq=%5B%5BB%5D%5D; session-id-apay=133-6836462-1605452; session-id=143-7434432-9626530; x-main="Xh1vS@RQhYnipPF18GvNk@EUXIcvBJ76F?Qao9yb75EjOCfA0E3OzNqgcGZ6zi2t"; at-main=Atza|IwEBINnuy0QAv4IswCjogZmvqAHy-hXRLtxmdTrefGgzhtm3xgAncCsPMdfFtNjDyl_acXAW_WBuwpWfi35vyKkZyx-K72ZBSj_EyoB7qFKOtZaqbsHHr3tdCYn8-JraV2AAD3eYKKIgdf1uQtVhxWwjJqIqWz9iAG9nWN8fn9OiEj1ZA_jPSFl0JyrhiZA9FoDXL0lFF5QARotnSuMjyO40QdY1gXZLOjUYIKATwknY4oGt2g; sess-at-main="lJN8r/H14jvCtAkrVrUIdEmZoWVb6FmHhkLLcueqpmU="; sst-main=Sst1|PQEYSOUm6b66zC0OtJ7mHcI-CeIGCa69GtN_xQgv_4N2RGqbqevoEFJDaiScT2ZeDrqInEJUtMK0sSdF0qTNUzaed4p9Vp9-5Ew70C4QDu-HiKT3fivG0JagtOysvasmzhRachMZ62CEbKH5FAnkkI_xLvXqpE5SWYawvatZGnUWm8sKzbDZaf3xZbz60JfUg9yjWh0Dwz8g68YmHbPF8n9V8gBZWibrEYMnhd4LnOeguj9VMpoAFQC6zMgyMVGxyh_e9m4MVFc8GAo50jI8oMfNd-SvIaMBYzD-hQC6G8Gznk4; ubid-acbus=134-8272146-7859437; x-acbus=f96vMZJqzanJhf?NrP5BLEL9qFNvByH9w5Z6OMBdUAMjCBLTa7oaJwW4Wkg2?xvR; session-id-time=2082787201l; s_pers=%20s_fid%3D0D5D6BA244E3BA36-101708CAD5171D3A%7C1835305721010%3B%20s_dl%3D1%7C1677541121012%3B%20gpv_page%3DUS%253ASD%253ASOA-home%7C1677541121015%3B%20s_ev15%3D%255B%255B%2527ELUSSOA-sellercentral.amazon.com%2527%252C%25271677539321027%2527%255D%255D%7C1835305721027%3B; s_sess=%20s_cc%3Dtrue%3B%20s_ppvl%3DUS%25253ASD%25253ASOA-home%252C10%252C10%252C937%252C1920%252C937%252C1920%252C1080%252C1%252CL%3B%20s_ppv%3DUS%25253ASD%25253ASOA-home%252C10%252C10%252C937%252C1920%252C937%252C1920%252C1080%252C1%252CL%3B; session-token=H/uQXLQl2lleLjHFNutm6H/4NAxtwF3xcrgGCcFMNpwaNy9u1rq1toDnj4H5IU/vd+ZPeQpyv5AzJKIiscbifgO7kKdy1aXm0OHxJ8SRqMArtPYfAQek+sNLFKZuQ4YZWwCEpae3SYEFY28/JieIVXC0bCTt3VpvNP79Aklddmf/AmInaIa9zNBIMKoCufaQZuwXXTVSVmfI2lvbhx+W5T4jYi7Ia5j/tq+/CyjsfaK4i0VvX3qq/AoEUKEnaBvj; csm-hit=tb:s-04RWWNRERQ8NZNF0NYWG|1677539790454&t:1677539792634&adb:adblk_yes',
    'device-memory': '8',
    'downlink': '1.35',
    'dpr': '1',
    'ect': '3g',
    'referer': 'https://www.amazon.com/Electronics/dp/',
    'rtt': '550',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-ch-viewport-width': '672',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'viewport-width': '672',
}

params = {
    'k': 'Vinyl Records',
}

response = requests.get('https://www.amazon.com/s', params=params, headers=headers)
print (response)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())