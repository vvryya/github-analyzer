# 📊GitHub Repository Analyzer

This CLI tool fetches data using the GitHub API and visualizes:
- most used programming languages
- stars/forks per repository
- commit activity

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)

---

## 🖊️Features

- 📥Fetch public repositories for any GitHub user
- 📈Visualize language usage in charts
- 🌟List top-starred repositories
- 📝Export basic report

---

## 🛠️Tech stack

- Python
- 'requests', 'matplotlib', 'pandas'
- GitHub REST API

---

## 🛠️Installation

```bash
git clone https://github.com/vvryya/github-analyzer.git
cd github-analyzer
```

No external dependencies required

---

## 👀Usage

![usage](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3hwejU1amxja29sNjl0ajFvdGwyaXMxcW85b2Vka3lkYjExajN2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OrGombmLdJ4QH6FGUE/giphy.gif)

Will generate:

```bash
github-analyzer/
├── reports/
│   ├── username_repos.csv
│   ├── username_activity.csv
├── charts/
│   ├── username_languages.png
│   ├── username_activity.png
```

---

## 📂Project Structure

```bash
todo-cli/
├── analyzer.py        # Main CLI logic
├── exporter.py        # Exporting to CSV
├── github_api.py      # GitHub API methods
├── plots.py
├── charts/            # directory with plots
├── reports/           # directory with CSV reports
└── README.md
```

--- 

## 👩🏼‍💻Author

### Varvara Pavlova

[GitHub Profile](https://github.com/vvryya)