import requests

session = requests.Session()

r = session.get('http://httpbin.org/get', cookies={'my-cookie': 'browser'})
print(r.text)


r = requests.get('http://httpbin.org/stream/20', stream=True)

for line in r.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))