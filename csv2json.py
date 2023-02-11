import csv, json, datetime

out = []

def parseTime2days(string):
  days = 0
  if "y" in string:
    days = int(string.split("y")[0])*365
  elif "m" in string:
    days = int(string.split("m")[0])*30
  elif "d" in string:
    days = int(string.split("d")[0])
  elif "h" in string:
    days = int(string.split("h")[0])/24
  return days

with open('data.csv', newline='', encoding="utf-8-sig") as csvfile:
  reader = csv.DictReader(csvfile)
  headers = reader.fieldnames
  for row in reader:
    _data = {}
    for header in headers:
      if header == '時間戳記': continue
      elif header == '專案名稱':
        _data[header] = row[header]
      elif header == '數位性 Digital ':
        _data['數位性 Digital'] = row[header].split(', ')
      elif '推動歷程與時間(' in header:
        _data[header] = parseTime2days(row[header])
      else:
        _data[header] = row[header].split(', ')
    out.append(_data)

def counter(dataarray, colname):
  count = {}
  for data in dataarray:
    for opt in data[colname]:
      if opt in count:
        count[opt] += 1
      else:
        count[opt] = 1
  return count
        
with open('out.json', 'w', encoding="utf-8") as outfile:
  final = {
    '坑主與團隊屬性(複選)_count': counter(out, '坑主與團隊屬性(複選)'),
    '專案目標設定(複選)_count': counter(out, '專案目標設定(複選)'),
    '複雜度 Complexity_count': counter(out, '複雜度 Complexity'),
    '重用性 Modular_count': counter(out, '重用性 Modular'),
    '數位性 Digital_count': counter(out, '數位性 Digital'),
    '公開性 Public_count': counter(out, '公開性 Public'),
    '軸向_count': counter(out, '軸向'),
    'data': out
  }
  json.dump(final, outfile, ensure_ascii=False, indent=4)