import os
import git
import time

# Set the correct repo path
repo_path = "C:/Users/abhis/Documents/GitHub/walmart sales forecasting/skills-github-pages"

# Initialize the Git repo
repo = git.Repo(repo_path)

# File to modify
file_path = os.path.join(repo_path, "log.txt")

# Number of commits
total_commits = 100000

# Start commit process
print(f"🔥 Generating {total_commits} commits...")

for i in range(total_commits):
    with open(file_path, "a") as file:
        file.write(f"Commit #{i+1}\n")

    repo.index.add([file_path])
    commit_message = f"Automated Commit #{i+1}"
    repo.index.commit(commit_message)

    if i % 5000 == 0:
        print(f"✅ {i} commits done...")

print("🚀 All commits completed! Pushing to GitHub...")

# Push everything to GitHub
repo.remote(name="origin").push()
print("✅ All commits pushed successfully!")
