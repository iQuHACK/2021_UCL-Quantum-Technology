"""geocoding test for travelling salesman"""
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

print(conn)

params = urllib.parse.urlencode({
    'access_key': 'ba86c5995bebed17ed2705f9fa2e2569',
    'query': 'Copacabana',
    'region': 'Rio de Janeiro',
    'limit': 1,
    })

print(params)

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
print(res)
data = res.read()

print(data.decode('utf-8'))