import requests
import json
import sys

def parse_bookmarks(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    post_ids = []
    for item in content.split('-'):
        if 'q' in item:
            post_id = item.split('q')[0]
            post_ids.append(post_id)

    return post_ids

def fetch_hn_post_details(post_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 parse_harmonic_bookmarks.py <bookmark_files>")
        sys.exit(1)

    post_ids = []
    for bookmarks_file in sys.argv[1:]:
        post_ids = post_ids + parse_bookmarks(bookmarks_file)

    bookmarks_data = {}
    for post_id in post_ids:
        post_details = fetch_hn_post_details(post_id)
        if post_details:
            post_title = post_details.get('title', 'N/A')
            post_url = post_details.get('url', 'N/A')
            hn_post_link = f"https://news.ycombinator.com/item?id={post_id}"

            bookmarks_data[hn_post_link] = {
                'title': post_title,
                'url': post_url,
                'hn_link': hn_post_link
            }

    output_filename = "static/harmonic_bookmarks.json"

    with open(output_filename, 'w') as f:
        json.dump(list( bookmarks_data.values() ), f, indent=4)

    print(f"Successfully created {output_filename}")

if __name__ == '__main__':
    main()
