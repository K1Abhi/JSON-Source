import requests
import json


API_URL = "https://www.andybek.com/api/data/books"
ORIGINAL_FILE = 'books-original.json'
CLEANED_FILE = 'books-cleaned.json'

def fetch_and_clean_books():

    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        books_data = response.json()

        with open(ORIGINAL_FILE, "w") as f:
            json.dump(books_data, f, indent=2)

        for book in books_data:
            print(book)
            del book["rank"]
            del book["release_date"]

        with open(CLEANED_FILE, "w") as f:
            json.dump(books_data, f, indent=2)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_and_clean_books()


