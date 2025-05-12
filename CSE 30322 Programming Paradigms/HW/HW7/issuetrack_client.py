import requests
import csv
from collections import defaultdict


def get_info(url, arg):
  data = []
  while url:
    response = requests.get(url, params=None)
    response_json = response.json()
    url = response_json['next']
    data += response_json['results']

  counts = defaultdict(int)
  for row in data:
    counts[row[arg]] += 1
  return dict(counts)
def create_csv(data, filename, col1, col2):
  with open(filename, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    csv_writer.writerow([col1, col2])
    for key in data:
      csv_writer.writerow([key, data[key]])

# print(len('https://jcssdev.pythonanywhere.com/bugs/'))
package_data = get_info('https://jcssdev.pythonanywhere.com/bugs/','package')
bug_data = get_info('https://jcssdev.pythonanywhere.com/comments/','bug')
new_bug_data = {}
for bug, count in bug_data.items():
  new_bug_data[bug[40:-1]] = count
bug_data = new_bug_data
create_csv(package_data,'total_bugs_per_package.csv','package','total')
create_csv(bug_data,'total_comments_per_bug.csv','bug_id','total')
  