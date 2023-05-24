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

filename = input('IP File: ')
main(filename)
