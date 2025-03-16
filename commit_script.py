import os
import git
import datetime
import random
import time

# Repo का path (अपने repo के path से बदल सकते हो)
repo_path = "C:/Users/abhis/Documents/GitHub/walmart sales forecasting/skills-github-pages"
  # 🔥 अपना सही path डालो

# Git Repo को access करो
repo = git.Repo(repo_path)

# 1 साल के लिए रोज़ाना commit करने का loop
start_date = datetime.datetime(2024, 3, 16)  # 1 साल पहले की डेट
end_date = datetime.datetime(2025, 3, 16)    # आज की डेट

current_date = start_date

while current_date <= end_date:
    file_path = os.path.join(repo_path, "log.txt")

    # एक फ़ाइल में कुछ random text लिखो (Commit Message को अलग-अलग दिखाने के लिए)
    with open(file_path, "a") as file:
        file.write(f"Commit on {current_date.strftime('%Y-%m-%d')}\n")

    # Git Commands - Add, Commit
    repo.index.add([file_path])
    commit_message = f"Commit on {current_date.strftime('%Y-%m-%d')}"
    repo.index.commit(commit_message, author_date=current_date.strftime("%Y-%m-%d %H:%M:%S"),
                      commit_date=current_date.strftime("%Y-%m-%d %H:%M:%S"))

    print(f"✅ Commit done for {current_date.strftime('%Y-%m-%d')}")

    # अगले दिन पर जाओ (कभी-कभी कुछ commits skip करने के लिए randomize कर सकते हो)
    current_date += datetime.timedelta(days=random.randint(1, 2))  # कुछ दिनों को skip करने के लिए 1-2 days increment

    # कुछ सेकंड रुको ताकि GitHub API पर ज्यादा load न पड़े
    time.sleep(1)

# सब कुछ push कर दो
origin = repo.remote(name="origin")
origin.push()
print("🚀 All commits pushed successfully!")
