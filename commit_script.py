import os
import git
import datetime
import random

# Set the correct repo path
repo_path = "C:/Users/abhis/Documents/GitHub/walmart sales forecasting/skills-github-pages"

# Initialize the Git repo
repo = git.Repo(repo_path)

# File to modify
file_path = os.path.join(repo_path, "log.txt")

# Define start and end dates (past 1 year)
start_date = datetime.datetime(2024, 12, 1)
end_date = datetime.datetime(2026, 1, 1)

current_date = start_date

print("🔥 Starting backfilling commits for past year...")

while current_date <= end_date:
    daily_commits = random.randint(1, 12)  # Random commits per day (1-12)
    
    for i in range(daily_commits):
        with open(file_path, "a") as file:
            file.write(f"Commit on {current_date.strftime('%Y-%m-%d')} #{i+1}\n")

        repo.index.add([file_path])
        commit_message = f"Automated Commit #{i+1} on {current_date.strftime('%Y-%m-%d')}"
        repo.index.commit(commit_message, 
                          author_date=current_date.strftime("%Y-%m-%d %H:%M:%S"),
                          commit_date=current_date.strftime("%Y-%m-%d %H:%M:%S"))

    print(f"✅ {daily_commits} commits done for {current_date.strftime('%Y-%m-%d')}")

    # Move to the next day
    current_date += datetime.timedelta(days=1)

print("🚀 All past-year commits completed! Pushing to GitHub...")

# Push everything to GitHub
repo.remote(name="origin").push()
print("✅ All commits pushed successfully!")
