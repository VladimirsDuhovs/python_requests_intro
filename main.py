import requests

# https://jsonplaceholder.typicode.com/posts

def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    for item in data:
        # print(f"User ID: {item['userId']} \t Title: {item['title']}")

        if item['userId'] == 1:
            print("Found user with UserId #1")
            print("Here's his data:", item['body'])
            print()

            with open('user_data.txt', 'a') as file:
                file.write(f"{item['body']}\n")

def main():
    print(get_posts())


if __name__ == "__main__":
    main()
