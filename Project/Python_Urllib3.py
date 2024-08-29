import urllib3

http = urllib3.PoolManager()
resp = http.request('GET', 'http://httpbin.org/robots.txt')
print(resp.status)
print(resp.data)
