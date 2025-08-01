import matplotlib.pyplot as plt
from collections import Counter

def plot_language_distribution(repos, output_path):
    all_languages = []
    for repo in repos:
        all_languages.extend(repo["languages"].keys())

    if not all_languages:
        print("Nothing to plot.")
        return

    lang_count = Counter(all_languages)
    labels = list(lang_count.keys())
    sizes = list(lang_count.values())

    plt.figure(figsize=(12,10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Language Distribution")
    plt.axis('equal')
    plt.savefig(output_path)
    plt.close()

def plot_commit_activity(data, output_path):
    if not data:
        print("Nothing to plot.")
        return
    
    names = [d["repo"] for d in data]
    commits = [d["commits"] for d in data]

    plt.figure(figsize=(12, 8))
    plt.bar(names, commits, color="green")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Commits")
    plt.title("Commit Activity by Repository")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()