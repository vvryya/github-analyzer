from  github_api import get_user_repos

print("""
Welcome to GitHub Repository Analyzer!
Here you can:
- Fetch public repositories for any GitHub user
- Visualize language usage in charts
- List top-starred repositories
- Export basic report
""")

username = input("Enter GitHub username: ")

repos = get_user_repos(username)