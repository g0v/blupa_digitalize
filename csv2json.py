import csv, json

out = []
with open('data.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  headers = reader.fieldnames
  for row in reader:
    _data = {}
    for header in headers:
      _data[header] = row[header].split(', ')
    _data.pop('時間戳記')
    _data['專案名稱'] = _data['專案名稱'][0]
    out.append(_data)

with open('out.json', 'w', encoding="utf-8") as outfile:
  json.dump(out, outfile, ensure_ascii=False, indent=4)