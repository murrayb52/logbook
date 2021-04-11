from django.http import request
import requests
import json


# the get_book service fetches book metadata from external API using the ISBN search term
def get_book(isbn_num):
    isbn_url = "https://openlibrary.org/isbn/"
    fetch_url = isbn_url + isbn_num + '.json'
    response = requests.get(fetch_url).json()
    return response
"""
    #url = 'https://openlibrary.org/isbn/'
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    book_details = json.loads(response.text)
    return book_details
"""
