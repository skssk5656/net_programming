import re
import requests

url = "https://labs.sch.ac.kr/department/iot/01.php#department-professorS"

response = requests.get(url)
text = response.text

email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_addresses = re.findall(email_regex, text)

for email in email_addresses:
    print(email)
