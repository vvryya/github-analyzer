import requests

def get_user_repos(username, token = None):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    headers = {"Authorization": f"token {token}"} if token else {}
    repos = response.json()

    results = []
    for repo in repos:
        lang_url = repo.get("languages_url")
        lang_resp = requests.get(lang_url, headers=headers)
        languages = lang_resp.json() if lang_resp.ok else {}

        results.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "languages": languages
        })

    return results


# data not generated yet
'''
def get_repo_commits(username, repo_name, token = None):
    response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/stats/commit_activity")
    data = response.json() '''