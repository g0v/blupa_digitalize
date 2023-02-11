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

with open('data.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  headers = reader.fieldnames
  for row in reader:
    _data = {}
    for header in headers:
      if header == '時間戳記': continue
      if header == '專案名稱':
        _data[header] = row[header]
      if '推動歷程與時間(' in header:
        _data[header] = parseTime2days(row[header])
      else:
        _data[header] = row[header].split(', ')
    out.append(_data)

with open('out.json', 'w', encoding="utf-8") as outfile:
  json.dump(out, outfile, ensure_ascii=False, indent=4)