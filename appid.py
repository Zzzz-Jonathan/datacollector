import openpyxl
import re

wb = openpyxl.load_workbook("url_list.xlsx")

sheet = wb['Sheet2']

col = 0
urls = []
slug = []
reg1 = r"https://www.appannie.com/apps/ios/app/(.*)/rank-history.*"
reg2 = r"https://www.data.ai/apps/ios/app/(.*)/rank-history.*"
target = []

for cell in sheet['B']:
    if cell.value is not None:
        urls.append(cell.value)
    col += 1
    if col > 500:
        break

print('Total %d urls.' % len(urls))

for url in urls:
    s = re.findall(reg1, url)
    if len(s) == 0:
        s = re.findall(reg2, url)
        if len(s) == 0:
            print(url)
    else:
        slug.append(s[0])

for s in slug:
    target.append(
        'https://www.data.ai/apps/ios/app/' + s + '/rank-history?app_slug=' + 's' + '&market_slug=ios&vtype=day&countries=CN&device=iphone&view=rank&legends=2222&date=2022-01-22~2022-04-20')

with open('urls.txt', 'w') as f:
    for t in target:
        f.write(t + '\n')

with open('urls.txt', 'r') as f:
    for each in f:
        print(each.strip('\n'))
