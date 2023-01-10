from bs4 import BeautifulSoup
import requests
import time
import re

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
sub_string = "citation needed"


def get_citations_needed_count(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    paragraph_list = soup.find_all('p')
    citation_count = 0

    for item in paragraph_list:
        for string in item.strpped_strings:
            if sub_string in repr(string):
                citation_count += 1
    print(f'Number of Citation: {citation_count}\n')


def get_citations_needed_report(url):
    res = requests.get(url)
    list_with_citation = []
    results_to_display = []
    soup = BeautifulSoup(res.content, 'html.parser')

    paragraph_list = soup.find_all('p')

    for paragraph in paragraph_list:
        if sub_string in paragraph.text:
            list_with_citation.append(paragraph.text)

    for paragraph in list_with_citation:
        head, sep, tail = paragraph.rpartition('[citation needed]')
        if sub_string in head:
            new_head, sep, new_tail = head.rpartition('[citation needed]')
            results_to_display.append(new_head)
            results_to_display.append(new_tail)
        else:
            results_to_display.append(head)
    print('paragraph with Citation:\n')
    for paragraph in results_to_display:
        print(paragraph)
        print()
        time.sleep(3)

        # print(items.replace("[citation needed]", "\n\n"))


get_citations_needed_count()
get_citations_needed_report()
