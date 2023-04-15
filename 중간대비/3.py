str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'
item = str.split('?')[1].split('&')
result = {}
for items in item:
    key, value = items.split('=')
    result[key] = value
print(result)