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

def get_commit_activity(username, token = None):
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/users/{username}/repos"
    repos_resp = requests.get(url, headers = headers)

    data = []
    for repo in repos_resp.json():
        repo_url = f"https://api.github.com/users/{username}/{repo['name']}/stats/commit_activity"
        r = requests.get(repo_url, headers = headers)
        if r.status_code == 202:
            print("GitHub is calculating stats, need to try later")
            continue
        if r.ok:
            weeks = r.json()
            total = sum(week["total"] for week in weeks)
            data.append({"repo": repo["name"], "commits": total})
    return data