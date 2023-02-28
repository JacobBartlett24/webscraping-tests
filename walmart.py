import requests
import json
from bs4 import BeautifulSoup

class Vinyl:
    def __init__(self, title = "N/A", artist = "N/A", price = "N/A", image = "N/A", url = "N/A", type = "N/A"):
        self.title = title
        self.artist = artist
        self.price = price
        self.image = image
        self.url = url
        self.type = type

    def __str__(self):
        return f'title: {self.title}\n Artist: {self.artist} \n Price: {self.price} \n Image: {self.image} \n URL: {self.url} \n Type: {self.type}'

    def __repr__(self):
        return f'{self.title} by {self.artist}'

cookies = {
    'brwsr': 'b682b7b2-16f2-11ed-905d-db42317697d2',
    'ACID': '9503cb9c-db52-40bf-a005-4b182c4907fc',
    'hasACID': 'true',
    'assortmentStoreId': '945',
    'hasLocData': '1',
    'vtc': 'fhajfpsin3KbMovN2EJC8s',
    '_pxhd': 'e7ce84974cf97d298a4df3b8d3c177157b5dfb69a8acdc206e783428e9e7de68:bf9707ab-b542-11ed-9529-72646973574d',
    'pxcts': 'c159597b-b542-11ed-81a4-774f78537869',
    '_pxvid': 'bf9707ab-b542-11ed-9529-72646973574d',
    'TBV': '7',
    'WLM': '1',
    'wmtboid': '1677540577-6983876452-23774898560-74296558',
    'bm_mi': '8D92494A5FA978F9AE0131E660926692~YAAQxjovF5+sF4qGAQAAltA1lRJCW8CZia8IUUWRWFvI3GiBhP+wbkYPpeHTHSPhnescQPfA06vayla7y2o6aNOwjlE0kcJrHAWXDvdQf7dkeZHLCBiXYH4qA+54zUiZWDoK0FjpHTPetfhezb/+GUQNHJ9D3+2eWPM7ZEmdKOVhLtSD4l1XgDwnCNE+4rG/+4xtDCwVAg3UZa8uPcv48L09O/NSlw1bTT1AwxUd8KGyO27hBtV5/j9S6bN0LhByezcUFtwU6LlkNOODbn62M7+yB6/6Th9jVjpI4VfTNiJvidG73162lGVvaZjB3Qof6NlxAMBk~1',
    'ak_bmsc': '7C92A20160826BA5D45A9685430E7E74~000000000000000000000000000000~YAAQxjovF6utF4qGAQAAedQ1lRJK75GuuqHwb4TAdjxO7DIl9z/w1DlQTsZEOXU/S18NReWExgygafMFl9eK3RjuqtpL12Jc2Ln5/TqS+kihCBa8RgfReOwccr3Q3ELIV8Wolp0oztC7sMZEPxopMY0rWbR5XzV2BTtNizTttkMXi5djVdde0msxPP/ynhV1AHntYnIVxnTa15OLdymrdJ8Ps3FH27CzWOoZkV87X/PygTSjO5AQbnE8qawaMwo2iVCVOpMva93P27g16triFzdGpoUPnQhluV6/qSVKW3u7/Ejwm4HcXK4VabaWV56aGX6m+QbkWznuP8twDGK6KA3Fy/tZeysxOwtPLp2YsjeXuRv/7ksnqPkYCXtj7q60NMkjtelnzVr+GTLilmq/bwydhqfy2KsyhHAbMEPlcheZ7czoZ+U=',
    '_pxff_rf': '1',
    '_pxff_fp': '1',
    '_pxff_cfp': '1',
    'AID': 'wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1677540587253',
    'auth': 'MTAyOTYyMDE47jUIPBSYan5gh4xxvBpDX%2FESH6%2FMVbk015TlzW4SO3IRoTeL3uy0rSvxJKfgqPySwYPFCgyTCPZPvYwxUVyYxsbdtWs%2FQNopXrXMkH7MgsZnGSIZzv3tHJG9WAuITDnw767wuZloTfhm7Wk2KcjygglTqinKgSpV0hco0QKmh1D5w%2FG7nzzkQDgmbTz3AE8onSuWomgQV42SI1mYw6gZH73ekYM4ZVaM9HO7WPdsTwAUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHX5SoQN31%2Bt4260jOR%2BHv3tprAL%2B9ZpnHCHvB88kOdCNG4ejgB%2B3AreqnpAlINrsYpliqeSY4XSLjNRjVsU2tUuZU563vej9qFVoX%2F4jZjP%2BgHD6cXNDkzidOMpKjg06OEjyrOXbKKhH072NS%2FW0j%2FU%3D',
    'locDataV3': 'eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiI5NDUiLCJkaXNwbGF5TmFtZSI6Ikx1YmJvY2sgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiNzk0MTYiLCJhZGRyZXNzTGluZTEiOiI3MDIgVyBMb29wIDI4OSIsImNpdHkiOiJMdWJib2NrIiwic3RhdGUiOiJUWCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiNzk0MTYtNDIwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzMuNTg5MjQyLCJsb25naXR1ZGUiOi0xMDEuOTM4MTEyfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiOTQ1Iiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfQkFLRVJZIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozMy41OTY4LCJsb25naXR1ZGUiOi0xMDEuOTQ0MywicG9zdGFsQ29kZSI6Ijc5NDE2IiwiY2l0eSI6Ikx1YmJvY2siLCJzdGF0ZSI6IlRYIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6Ijk0NSIsImRpc3BsYXlOYW1lIjoiTHViYm9jayBTdXBlcmNlbnRlciIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiOTQ1IiwiZGlzcGxheU5hbWUiOiJMdWJib2NrIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijc5NDE2IiwiYWRkcmVzc0xpbmUxIjoiNzAyIFcgTG9vcCAyODkiLCJjaXR5IjoiTHViYm9jayIsInN0YXRlIjoiVFgiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijc5NDE2LTQyMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjU4OTI0MiwibG9uZ2l0dWRlIjotMTAxLjkzODExMn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6Ijk0NSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2Nzc1NjIxODc0NjgsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo5NTAzY2I5Yy1kYjUyLTQwYmYtYTAwNS00YjE4MmM0OTA3ZmMifQ%3D%3D',
    'locGuestData': 'eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiOTQ1IiwidGltZXN0YW1wIjoxNjc3NTQwNTg3NDY1fSwic2hpcHBpbmdBZGRyZXNzIjp7InRpbWVzdGFtcCI6MTY3NzU0MDU4NzQ2NSwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI3OTQxNiIsImNpdHkiOiJMdWJib2NrIiwic3RhdGUiOiJUWCIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiI5NDUiLCJ0eXBlIjoiREVMSVZFUlkifV19LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY3NzU0MDU4NzQ2NSwiYmFzZSI6Ijc5NDE2In0sIm1wIjpbXSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjk1MDNjYjljLWRiNTItNDBiZi1hMDA1LTRiMTgyYzQ5MDdmYyJ9',
    'TB_Latency_Tracker_100': '1',
    'TB_Navigation_Preload_01': '1',
    'TB_SFOU-100': '',
    'bstc': 'WAwI-ddFvkjvVG6pcLnuyM',
    'mobileweb': '0',
    'xptc': 'assortmentStoreId%2B945',
    'xpth': 'x-o-mart%2BB2C~x-o-mverified%2Bfalse',
    'xpa': '0dn-S|14us3|2FrnP|2epfI|4PdWF|4ifl2|52Kub|8XEBl|B0dNz|CUZkH|Ce2NS|D8jju|Eq7vl|F4DEO|FVa_h|GK20V|Ho3eT|O1WSp|R2zaD|RFZpx|WwWoM|XZIx3|YJZ_N|YUOnt|YnYws|ZwAjn|_09Xe|_j--W|aJO3a|eNo8c|kNvPV|mPKhl|moJ3J|ruskL|sWzrk|vcaUF|zfgv8',
    'exp-ck': '0dn-S12FrnP14PdWF14ifl2252Kub18XEBl1Ce2NS1D8jju1Eq7vl1F4DEO1Ho3eT1RFZpx1WwWoM1XZIx31YJZ_N1YnYws1ZwAjn1_09Xe1_j--W1kNvPV2mPKhl1sWzrk3vcaUF1zfgv82',
    'xptwj': 'rq:a08674a7b93bf1bdf936:BUGwW36Ypu+rvlt2FWu2owF6OewXiIa8vXl7NctvcyNUn/7XmlOyIhrOXOdRhnpzWbcxVhTj2lcUr2/rWriuaJuXSlgTyg2wst8/fiaGhrhZvsorTSev8O2pOw==',
    'akavpau_p2': '1677541188~id=6e55348b9abba86ea53de1251e2c347c',
    '_astc': '0b8b0744d66eb03afc478f1913b4e080',
    'xpm': '1%2B1677540587%2Bfhajfpsin3KbMovN2EJC8s~%2B0',
    'adblocked': 'true',
    'com.wm.reflector': '"reflectorid:0000000000000000000000@lastupd:1677540591000@firstcreate:1677540587253"',
    '_px3': '4f5b249873e9990aa5a966b7660189606f3cd363b7c4090a7b6a42d600938010:hx1ljOnyum8LK9tGQaUs6zxRCiklYziNLCSnEGuPaE80rPAwQECCdMHQt+G1+UG53JU3BdyCDRH82V2iSk3osQ==:1000:qjq5dVW7iMkpe419zclQwinrAVfR40vJtJYDhKYS9X66ubmsvJidO5i2FZuwVV9mRceIobKxI7CcRGTTC49P7G/uycGY+Cpxlkwd0iVcbmAGQadmK4hyhXhfC056fMsg4OV48XFBT78dFNP0NUWqt3KgsqmRK4Uw5/4AaJTZj4osBKJ/rZAfYnzdX4KaBuAiHUIvHMWjGZJ58aBefn3DnA==',
    '_pxde': 'c685fbe94c05f2c952dc343d57774397f806e295e23f7a3839ecd2821a52784c:eyJ0aW1lc3RhbXAiOjE2Nzc1NDA1OTIwMTB9',
    'xptwg': '3550212817:77D7E554F3D2A0:132D502:A274D3A6:E760B32E:44774722:',
    'TS012768cf': '01873afedc645bd1e29b8a47d2b4a9aa79a33229a3df5b141f3e560723ef24e076789a173fe1497b59b0e084dbd6f47ccdfb4df21b',
    'TS01a90220': '01873afedc645bd1e29b8a47d2b4a9aa79a33229a3df5b141f3e560723ef24e076789a173fe1497b59b0e084dbd6f47ccdfb4df21b',
    'TS2a5e0c5c027': '0851c6ff15ab20000580bb5d716d25b6d9f2eb922be44e64fe3f154953860de75abbe4ae3e51560108beee70001130003bc9b12ab4019e520c0635826c7036934a64bbe994c653c53fe2656b61936b7df6e822bd5d2f64358bd5ee569661535b',
    'bm_sv': '99874105C5C59AC7C2C1E09C3C413EA8~YAAQxjovFwW6F4qGAQAAZBM2lRLQ19HknEuohKne7d3/7DOijBcqERo6biWPxZHeZgyeTOTi7N9JYYjowFp0PzQPjaMEL28KpVTSZEPpnf0wLeSaIWIsY0goLphDsPOW1RjgIO3u2uGOghH1FIt4KNgaFkCDezkp+5pU0+ExBJcykkan3W97bnIwgyqpL1xdaeKcejC9hyazv0U2JOxx+82cBRGkZ5o92nQ47TP11mpdhKDdeAU37SBr7iTAMsC25g==~1',
}

headers = {
    'authority': 'www.walmart.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'brwsr=b682b7b2-16f2-11ed-905d-db42317697d2; ACID=9503cb9c-db52-40bf-a005-4b182c4907fc; hasACID=true; assortmentStoreId=945; hasLocData=1; vtc=fhajfpsin3KbMovN2EJC8s; _pxhd=e7ce84974cf97d298a4df3b8d3c177157b5dfb69a8acdc206e783428e9e7de68:bf9707ab-b542-11ed-9529-72646973574d; pxcts=c159597b-b542-11ed-81a4-774f78537869; _pxvid=bf9707ab-b542-11ed-9529-72646973574d; TBV=7; WLM=1; wmtboid=1677540577-6983876452-23774898560-74296558; bm_mi=8D92494A5FA978F9AE0131E660926692~YAAQxjovF5+sF4qGAQAAltA1lRJCW8CZia8IUUWRWFvI3GiBhP+wbkYPpeHTHSPhnescQPfA06vayla7y2o6aNOwjlE0kcJrHAWXDvdQf7dkeZHLCBiXYH4qA+54zUiZWDoK0FjpHTPetfhezb/+GUQNHJ9D3+2eWPM7ZEmdKOVhLtSD4l1XgDwnCNE+4rG/+4xtDCwVAg3UZa8uPcv48L09O/NSlw1bTT1AwxUd8KGyO27hBtV5/j9S6bN0LhByezcUFtwU6LlkNOODbn62M7+yB6/6Th9jVjpI4VfTNiJvidG73162lGVvaZjB3Qof6NlxAMBk~1; ak_bmsc=7C92A20160826BA5D45A9685430E7E74~000000000000000000000000000000~YAAQxjovF6utF4qGAQAAedQ1lRJK75GuuqHwb4TAdjxO7DIl9z/w1DlQTsZEOXU/S18NReWExgygafMFl9eK3RjuqtpL12Jc2Ln5/TqS+kihCBa8RgfReOwccr3Q3ELIV8Wolp0oztC7sMZEPxopMY0rWbR5XzV2BTtNizTttkMXi5djVdde0msxPP/ynhV1AHntYnIVxnTa15OLdymrdJ8Ps3FH27CzWOoZkV87X/PygTSjO5AQbnE8qawaMwo2iVCVOpMva93P27g16triFzdGpoUPnQhluV6/qSVKW3u7/Ejwm4HcXK4VabaWV56aGX6m+QbkWznuP8twDGK6KA3Fy/tZeysxOwtPLp2YsjeXuRv/7ksnqPkYCXtj7q60NMkjtelnzVr+GTLilmq/bwydhqfy2KsyhHAbMEPlcheZ7czoZ+U=; _pxff_rf=1; _pxff_fp=1; _pxff_cfp=1; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1677540587253; auth=MTAyOTYyMDE47jUIPBSYan5gh4xxvBpDX%2FESH6%2FMVbk015TlzW4SO3IRoTeL3uy0rSvxJKfgqPySwYPFCgyTCPZPvYwxUVyYxsbdtWs%2FQNopXrXMkH7MgsZnGSIZzv3tHJG9WAuITDnw767wuZloTfhm7Wk2KcjygglTqinKgSpV0hco0QKmh1D5w%2FG7nzzkQDgmbTz3AE8onSuWomgQV42SI1mYw6gZH73ekYM4ZVaM9HO7WPdsTwAUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHX5SoQN31%2Bt4260jOR%2BHv3tprAL%2B9ZpnHCHvB88kOdCNG4ejgB%2B3AreqnpAlINrsYpliqeSY4XSLjNRjVsU2tUuZU563vej9qFVoX%2F4jZjP%2BgHD6cXNDkzidOMpKjg06OEjyrOXbKKhH072NS%2FW0j%2FU%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiI5NDUiLCJkaXNwbGF5TmFtZSI6Ikx1YmJvY2sgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiNzk0MTYiLCJhZGRyZXNzTGluZTEiOiI3MDIgVyBMb29wIDI4OSIsImNpdHkiOiJMdWJib2NrIiwic3RhdGUiOiJUWCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiNzk0MTYtNDIwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzMuNTg5MjQyLCJsb25naXR1ZGUiOi0xMDEuOTM4MTEyfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiOTQ1Iiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfQkFLRVJZIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozMy41OTY4LCJsb25naXR1ZGUiOi0xMDEuOTQ0MywicG9zdGFsQ29kZSI6Ijc5NDE2IiwiY2l0eSI6Ikx1YmJvY2siLCJzdGF0ZSI6IlRYIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6Ijk0NSIsImRpc3BsYXlOYW1lIjoiTHViYm9jayBTdXBlcmNlbnRlciIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiOTQ1IiwiZGlzcGxheU5hbWUiOiJMdWJib2NrIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijc5NDE2IiwiYWRkcmVzc0xpbmUxIjoiNzAyIFcgTG9vcCAyODkiLCJjaXR5IjoiTHViYm9jayIsInN0YXRlIjoiVFgiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijc5NDE2LTQyMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjU4OTI0MiwibG9uZ2l0dWRlIjotMTAxLjkzODExMn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6Ijk0NSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2Nzc1NjIxODc0NjgsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo5NTAzY2I5Yy1kYjUyLTQwYmYtYTAwNS00YjE4MmM0OTA3ZmMifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiOTQ1IiwidGltZXN0YW1wIjoxNjc3NTQwNTg3NDY1fSwic2hpcHBpbmdBZGRyZXNzIjp7InRpbWVzdGFtcCI6MTY3NzU0MDU4NzQ2NSwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI3OTQxNiIsImNpdHkiOiJMdWJib2NrIiwic3RhdGUiOiJUWCIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiI5NDUiLCJ0eXBlIjoiREVMSVZFUlkifV19LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY3NzU0MDU4NzQ2NSwiYmFzZSI6Ijc5NDE2In0sIm1wIjpbXSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjk1MDNjYjljLWRiNTItNDBiZi1hMDA1LTRiMTgyYzQ5MDdmYyJ9; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; bstc=WAwI-ddFvkjvVG6pcLnuyM; mobileweb=0; xptc=assortmentStoreId%2B945; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=0dn-S|14us3|2FrnP|2epfI|4PdWF|4ifl2|52Kub|8XEBl|B0dNz|CUZkH|Ce2NS|D8jju|Eq7vl|F4DEO|FVa_h|GK20V|Ho3eT|O1WSp|R2zaD|RFZpx|WwWoM|XZIx3|YJZ_N|YUOnt|YnYws|ZwAjn|_09Xe|_j--W|aJO3a|eNo8c|kNvPV|mPKhl|moJ3J|ruskL|sWzrk|vcaUF|zfgv8; exp-ck=0dn-S12FrnP14PdWF14ifl2252Kub18XEBl1Ce2NS1D8jju1Eq7vl1F4DEO1Ho3eT1RFZpx1WwWoM1XZIx31YJZ_N1YnYws1ZwAjn1_09Xe1_j--W1kNvPV2mPKhl1sWzrk3vcaUF1zfgv82; xptwj=rq:a08674a7b93bf1bdf936:BUGwW36Ypu+rvlt2FWu2owF6OewXiIa8vXl7NctvcyNUn/7XmlOyIhrOXOdRhnpzWbcxVhTj2lcUr2/rWriuaJuXSlgTyg2wst8/fiaGhrhZvsorTSev8O2pOw==; akavpau_p2=1677541188~id=6e55348b9abba86ea53de1251e2c347c; _astc=0b8b0744d66eb03afc478f1913b4e080; xpm=1%2B1677540587%2Bfhajfpsin3KbMovN2EJC8s~%2B0; adblocked=true; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1677540591000@firstcreate:1677540587253"; _px3=4f5b249873e9990aa5a966b7660189606f3cd363b7c4090a7b6a42d600938010:hx1ljOnyum8LK9tGQaUs6zxRCiklYziNLCSnEGuPaE80rPAwQECCdMHQt+G1+UG53JU3BdyCDRH82V2iSk3osQ==:1000:qjq5dVW7iMkpe419zclQwinrAVfR40vJtJYDhKYS9X66ubmsvJidO5i2FZuwVV9mRceIobKxI7CcRGTTC49P7G/uycGY+Cpxlkwd0iVcbmAGQadmK4hyhXhfC056fMsg4OV48XFBT78dFNP0NUWqt3KgsqmRK4Uw5/4AaJTZj4osBKJ/rZAfYnzdX4KaBuAiHUIvHMWjGZJ58aBefn3DnA==; _pxde=c685fbe94c05f2c952dc343d57774397f806e295e23f7a3839ecd2821a52784c:eyJ0aW1lc3RhbXAiOjE2Nzc1NDA1OTIwMTB9; xptwg=3550212817:77D7E554F3D2A0:132D502:A274D3A6:E760B32E:44774722:; TS012768cf=01873afedc645bd1e29b8a47d2b4a9aa79a33229a3df5b141f3e560723ef24e076789a173fe1497b59b0e084dbd6f47ccdfb4df21b; TS01a90220=01873afedc645bd1e29b8a47d2b4a9aa79a33229a3df5b141f3e560723ef24e076789a173fe1497b59b0e084dbd6f47ccdfb4df21b; TS2a5e0c5c027=0851c6ff15ab20000580bb5d716d25b6d9f2eb922be44e64fe3f154953860de75abbe4ae3e51560108beee70001130003bc9b12ab4019e520c0635826c7036934a64bbe994c653c53fe2656b61936b7df6e822bd5d2f64358bd5ee569661535b; bm_sv=99874105C5C59AC7C2C1E09C3C413EA8~YAAQxjovFwW6F4qGAQAAZBM2lRLQ19HknEuohKne7d3/7DOijBcqERo6biWPxZHeZgyeTOTi7N9JYYjowFp0PzQPjaMEL28KpVTSZEPpnf0wLeSaIWIsY0goLphDsPOW1RjgIO3u2uGOghH1FIt4KNgaFkCDezkp+5pU0+ExBJcykkan3W97bnIwgyqpL1xdaeKcejC9hyazv0U2JOxx+82cBRGkZ5o92nQ47TP11mpdhKDdeAU37SBr7iTAMsC25g==~1',
    'referer': 'https://www.walmart.com/blocked?url=L2Jyb3dzZS9tdXNpYy92aW55bC1yZWNvcmRzLzQxMDRfMTIwNTQ4MQ==&uuid=998bce28-b6f6-11ed-9088-52436e4c5678&vid=bf9707ab-b542-11ed-9529-72646973574d&g=b',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://www.walmart.com/browse/music/vinyl-records/4104_1205481', cookies=cookies, headers=headers)

rawResponse = response.text.replace(" ", "")

def formatToJson(rawResponse, start = 0, end = 0):
    for i in range(len(rawResponse)):
        if(rawResponse[i] == '{'
         and rawResponse[i-1] == '>'
         and start == 0
         and rawResponse[i+1] == '"'
         and rawResponse[i+2] == 'p'
         and rawResponse[i+3] == 'r'):
            start = i
        elif(rawResponse[i] == '}' and rawResponse[i+1] == '<' and start != 0):
            end = i + 1
            formattedResponse = rawResponse[start:end]
            findProducts(json.loads(formattedResponse))
            return
            
def findProducts(formattedResponse):
  for product in formattedResponse['props']['pageProps']['initialData']['searchResult']['itemStacks'][0]['items']:
    productInfo = product['name'].split('-')
    
    if(len(productInfo) == 1):
        vinyl = Vinyl(title = productInfo[0])
    elif(len(productInfo) == 2):
        vinyl = Vinyl(title = productInfo[1], artist = productInfo[0])
    elif(len(productInfo) == 3):
        vinyl = Vinyl(title = productInfo[1], artist = productInfo[0], type = productInfo[2])
    else:
        vinyl = Vinyl()
    
    print(vinyl)

        

    

formatToJson(rawResponse)


