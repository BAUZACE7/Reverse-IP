import concurrent.futures
import requests
from bs4 import BeautifulSoup




def process_line(line, f):
    r = requests.get(f'http://ip.yqie.com/iptodomain.aspx?ip={line}')
    soup = BeautifulSoup(r.content, 'html.parser')
    for i in soup.findAll('td', {'width': '90%'}):
        result = i.text
        print(result)
        f.write(result + '\n')

def main(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()

    with open('output.txt', 'a', encoding="utf-8") as output_file:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for line in lines:
                futures.append(executor.submit(process_line, line, output_file))

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)
banner = """
BBBBB  AAAAA  U   U  ZZZZZ   AAAAA  CCCCC  EEEEE   777
B   B  A   A  U   U     Z    A   A  C      E         7
BBBBB  AAAAA  U   U    Z    AAAAA  C      EEEE      7
B   B  A   A  U   U   Z    A   A  C      E         7
BBBBB  A   A   UUU   ZZZZ A   A  CCCCC  EEEEE  77777
"""

print(banner)

filename = input('IP File: ')
main(filename)
