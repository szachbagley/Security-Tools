import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    return forms

def fuzz(url, forms, payloads):
    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all('input')
        for payload in payloads:
            data = {}
            for input_tag in inputs:
                name = input_tag.get('name')
                if name:
                    data[name] = payload
            if method == 'post':
                response = requests.post(url + action, data=data)
            else:
                response = requests.get(url + action, params=data)
            if "error" in response.text.lower():
                print(f"Potential vulnerability found with payload: {payload}")