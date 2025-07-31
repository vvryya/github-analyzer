from  github_api import get_user_repos
from github_api import get_commit_activity

def help_window():
    print("""
    Welcome to GitHub Repository Analyzer!
    Here you can:
    - Fetch public repositories for any GitHub user
    - Visualize language usage in charts
    - List top-starred repositories
    - Export basic report
        
    Commands:
        "repos" - get user's public repos
        "activity" - get user's commit activity
        "stop" - end session
    """)

help_window()
username = input("Enter GitHub username: ", end = "")
command = input("Command: ", end = "")

while command != "stop":
    if command == "repos":
        repos = get_user_repos(username)
        print(*repos)
    elif command == "activity":
        repos = get_commit_activity(username)
    else:
        help_window()