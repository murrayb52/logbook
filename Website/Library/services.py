from django.http import request
import requests
import json


# the get_book service fetches book metadata from external API using the ISBN search term
def get_book(isbn_num):
    isbn_url = "https://openlibrary.org/isbn/"
    fetch_url = isbn_url + isbn_num + '.json'
    response = requests.get(fetch_url).json()
    return response


def get_author_name(author_code):
    base_url = "https://openlibrary.org/"
    fetch_url = base_url + author_code + '.json'
    response = requests.get(fetch_url).json()
    author_name = response["name"]
    return author_name
