#Numbers Translator Rapid Api

import http.client
import sys, json

conn = http.client.HTTPSConnection("numbers-spell.p.rapidapi.com")

headers = {
    'X-FunTranslations-Api-Secret': "<REQUIRED>",
    'X-RapidAPI-Key': "62457c2b65mshabfa50d155b5754p13f85ajsn99c1ef83f4ce",
    'X-RapidAPI-Host': "numbers-spell.p.rapidapi.com"
    }
try:
    number = int(input('Enter your Number : '))
except:
    print("Please enter number only.")
    sys.exit()

conn.request("GET", f"/numbers?text={number}", headers=headers)

res = conn.getresponse()
data = res.read().decode('utf-8')
# print(data)
# print(type(data))
data = json.loads(data)
# print(type(data))
error = data['error']['code']
if (error == 429):
    print(data['error']['message'])
else:
    wordNum = data['contents']['translated']
    print('''
    -------------------------------------------
            In num: {} 
    -------------------------------------------
            In word:{}
    '''.format(number, wordNum))