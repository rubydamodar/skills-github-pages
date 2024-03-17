import os
import git
import datetime
import random
import time

# 🔥 अपना सही repo path डालो
repo_path = "C:/Users/abhis/Documents/GitHub/walmart sales forecasting/skills-github-pages"

# Git Repo को access करो
repo = git.Repo(repo_path)

# 1 साल के लिए रोज़ाना commit करने का loop
start_date = datetime.datetime(2024, 3, 16)  # 1 साल पहले की डेट
end_date = datetime.datetime(2025, 3, 16)    # आज की डेट

current_date = start_date

while current_date <= end_date:
    file_path = os.path.join(repo_path, "log.txt")

    # 🔥 3000 बार commit करो
    for _ in range(random.randint(2000, 3000)):  
        with open(file_path, "a") as file:
            file.write(f"Commit on {current_date.strftime('%Y-%m-%d')} at {datetime.datetime.now().strftime('%H:%M:%S')}\n")

        # Git Commands - Add, Commit
        repo.index.add([file_path])
        commit_message = f"Commit on {current_date.strftime('%Y-%m-%d')} at {datetime.datetime.now().strftime('%H:%M:%S')}"
        repo.index.commit(commit_message, 
                          author_date=current_date.strftime("%Y-%m-%d %H:%M:%S"),
                          commit_date=current_date.strftime("%Y-%m-%d %H:%M:%S"))

    print(f"✅ {current_date.strftime('%Y-%m-%d')} - {random.randint(2000, 3000)} commits done")

    # अगले दिन पर जाओ
    current_date += datetime.timedelta(days=1)

    # GitHub API limit से बचने के लिए थोड़ा रुको
    time.sleep(3)

# सब कुछ push कर दो
origin = repo.remote(name="origin")
origin.push()
print("🚀 All commits pushed successfully!")
