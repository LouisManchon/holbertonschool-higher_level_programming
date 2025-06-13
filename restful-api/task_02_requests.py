import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()  # 👈 Maintenant seulement si la requête a réussi
        fieldnames = ['id', 'title', 'body']
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
