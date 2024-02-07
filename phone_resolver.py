import re
import requests
import phonenumbers

def search_in_html(text: str) -> set:
    results = set()
    for match in phonenumbers.PhoneNumberMatcher(text, "RU"):
        results.add(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
    return results

def search_no_city_code(text: str) -> set:
    results = re.findall(r'\"(\d{3}-\d{4}|\d{3}-\d{2}-\d{2})\"', text)
    return results

def format_numbers(numbers: set) -> set:
    results = set()
    for number in numbers:
        clean_number = re.sub(r'\D', '', number)

        if len(clean_number) == 7:
            clean_number = '8495' + clean_number
        elif clean_number[0] == '7' and len(clean_number) == 11:
            clean_number = clean_number.replace('7', '8', 1)
        elif clean_number[0] != '8' and len(clean_number) == 10:
            clean_number = '8' + clean_number
        else:
            continue

        results.add(clean_number)
    return results

def resolve_phone_numbers(adress: str, path: list) -> set:
    results = set()
    for p in path:
        url = adress + p
        response = requests.get(url)
        text = response.text
        results = results.union(search_in_html(text))
        results = results.union(search_no_city_code(text))

    return results

#Функция на вход получает адрес веб-страницы и список путей
def resolve_and_format(adress: str, path: list) -> set:
    results = resolve_phone_numbers(adress, path)
    return format_numbers(results)
