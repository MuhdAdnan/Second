import json


def load_data():
    try:
        with open('blog_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'posts': []}


def save_data(data):
    with open('blog_data.json', 'w') as file:
        json.dump(data, file, indent=2)


def create_post():
    title = input("Enter the post title: ")
    content = input("Enter the post content: ")
    post = {'title': title, 'content': content}

    data = load_data()
    data['posts'].append(post)
    save_data(data)
    print("Post created successfully!")


def view_all_posts():
    data = load_data()
    if not data['posts']:
        print("No posts available.")
    else:
        for i, post in enumerate(data['posts'], start=1):
            print(f"\nPost {i} - {post['title']}:\n{post['content']}")


def delete_post():
    view_all_posts()
    data = load_data()

    if not data['posts']:
        print("No posts available to delete.")
    else:
        try:
            post_index = int(input("Enter the post number to delete: ")) - 1
            deleted_post = data['posts'].pop(post_index)
            save_data(data)
            print(f"Post '{deleted_post['title']}' deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid post number.")


def main():
    while True:
        print("\nBlog Options:")
        print("1. Create a new post")
        print("2. View all posts")
        print("3. Delete a post")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_all_posts()
        elif choice == '3':
            delete_post()
        elif choice == '4':
            print("Quitting the blog program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()