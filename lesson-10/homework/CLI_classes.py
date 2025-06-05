#1  ToDo List Application
class Task:
    def __init__(self, title, description, due_date, status = "Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'{self.title}, {self.description}, {self.due_date}, {self.status}'

    def mark_complete(self):
        self.status ='Completed'

class ToDoList:
    
    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, task: Task):
        self.list_of_tasks.append(task)
        print(f"\nNew task'{task.title}' was created")

    def complete_task(self, index):
        self.list_of_tasks[index-1].mark_complete()
        print(f"\nTask '{self.list_of_tasks[index-1].title}' was marked complete")

    def list_all(self):
        if self.list_of_tasks:
            for index, task in enumerate(self.list_of_tasks):
                print(f"{index+1}. {task}")
        else:
            print("\nThere are no tasks in your to-do list, yet.")
        
    def list_incomplete(self):
        for index, task in enumerate(self.list_of_tasks):
            if task.status == 'Incomplete':
                print(f"{index}. {task}")
        else:
            print("\nYou don't have any uncompleted tasks")


def print_menu():
    print('\nTo-Do List Menu: ')
    print('1. Add a task')
    print('2. Mark a task as complete')
    print('3. List all tasks')
    print('4. Display incomplete tasks')  
    print('5. Exit')  

def main():
    task1 = Task('Reading', 'Finishing 13th chapter of "Demon haunted world"', '2025-06-05', 'Incomplete')
    To_Do = ToDoList()
    To_Do.add_task(task1)


    while True:
        
        print_menu()
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            title = input('Please, enter the title of your task: ')
            description = input('Please, enter the description of your task: ')
            due_date = input('Please, enter the deadline of your task: ')
            new_task = Task(title, description, due_date)
            To_Do.add_task(new_task)

        elif choice == '2':
            print('\n')
            To_Do.list_all()
            print('\n')
            ind = int(input('Select the number of the task you want to mark as complete: '))
            To_Do.complete_task(ind)

        elif choice == '3':
            print('\nYour tasks:')
            To_Do.list_all()

        elif choice == '4':
            print('\nIncomplete tasks:')
            To_Do.list_incomplete()

        elif choice == '5':
            print('\nGoodbye!\n')
            break
        
        else:
            print('Invalid choice')

if __name__=="__main__":
    main()

#Blog system
class Post:


    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"\nAbout: {self.title}.\nContent: {self.content}.\nBy: {self.author}\n"
    
    
class Blog:


    def __init__(self):
        self.all_posts = []

    def add_post(self, post: Post):
        self.all_posts.append(post)
    
    def list_posts(self):
        if self.all_posts:
            for num, post in enumerate(self.all_posts, 1):
               print(f"{num}. {post}")
        else:
            print("\nThere are no posts in the blog")
    
    def list_by_author(self, author):
        for i in self.all_posts:
            if i.author == author:
                print(i)
        else:
            print(f"\nThere are no posts by this author '{author}'.")

    def delete_post(self, post_ind):
        if 1 <= post_ind <= len(self.all_posts):
            deleted_post = self.all_posts.pop(post_ind - 1)
            print(f"\nPost '{deleted_post.title}' by {deleted_post.author} was deleted.")
        else:
            print('\nInvalid post number.')

    def edit_post(self, post_ind, new_title, new_content):
        if 1 <= post_ind <= len(self.all_posts):
            post = self.all_posts[post_ind - 1]
            post.title = new_title
            post.content = new_content
            print(f"\nThe post '{post.title}' by {post.author} was updated succesfully.")
        else:
            print('\nInvalid post number.')

    def display_latest(self, count = 3):
        if not self.all_posts:
            print('\nThere are no posts in this blog, yet')
            return
        if count > len(self.all_posts):
            print(f'There are only {len(self.all_posts)} posts!')
            
        print(f'The latest {min(count, len(self.all_posts))} posts:')
        latest_posts  = self.all_posts[-count:]
        for ind, post in enumerate(reversed(latest_posts), 1):
            print(f'{len(self.all_posts) - (ind - 1)}. {post}')


def print_menu():
    print('\nBlog management manu:')
    print('1. Add a post')
    print('2. List all posts')
    print('3. Display posts by an author')
    print('4. Delete a post')
    print('5. Edit a post')
    print('6. View recent posts')
    print('7. Exit')

def main():

    post = Post('Aliens among us!', 'blah blah blah blah blah', 'Psychopath')
    blog = Blog()
    blog.add_post(post)

    while True:
        print_menu()
        try:
            choice = int(input('\nEnter your choice (1-7): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4.')
            continue  # skip to the next loop iteration

        if choice == 1:
            title = input('Please, enter the title of the post: ')
            contents = input('Please, enter the contents of the post: ')
            author = input('Please, enter the author of the post: ')
            new_post = Post(title, contents, author)
            blog.add_post(new_post)
            print(f"\nNew post '{new_post.title}' was added!")
        
        elif choice == 2:
            print('\nAll posts:')
            blog.list_posts()
        
        elif choice == 3:
            author = input('\nWhose posts do you want to see?: ')
            print(f'\nPosts by {author}:\n')
            blog.list_by_author(author)

        elif choice == 4:
            blog.list_posts()
            try:
                ind = int(input('\nPlease enter the number of the post you want to delete: '))
                blog.delete_post(ind)
            except ValueError:
                print('\nInvalid input. Please enter a valid post number.')
        elif choice == 5:
            blog.list_posts
            try:
                ind = input('\nPlease enter the number of the post you want to edit: ')
                new_title = input('\nPlease enter the new title for the post: ')
                new_content = input('\nPlease enter the new content for the post: ')
                blog.edit_post(ind, new_title, new_content)
            except ValueError:
                print('\nInvalid input. Please enter a valid post number')

        elif choice == 6:
            try:
                count = int(input('\nHow many latest posts do you want to see?: '))
                blog.display_latest(count)
            except ValueError:
                print('\nInvalid input. Please, enter a number')

        elif choice == 7:
            print('\nGoodbye!👋👋\n')
            break

        else:
            print('Invalid option. Please choose a number between 1 and 4')

if __name__ == '__main__':
    main()
