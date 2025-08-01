from  github_api import get_user_repos
from github_api import get_commit_activity
from exporter import save_as_csv

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
print("Enter GitHub username: ", end = "")
username = input()
print("Command: ", end = "")
command = input()

while command != "stop":
    if command == "repos":
        repos = get_user_repos(username)
        save_as_csv(repos, f"reports/{username}_repos.csv")
    elif command == "activity":
        repos = get_commit_activity(username)
        save_as_csv(repos, f"reports/{username}_activity.csv")
    else:
        help_window()
    
    print("Command: ", end = "")
    command = input()