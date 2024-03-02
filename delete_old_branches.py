import os
import datetime
from git import Repo

def delete_old_branches(repo_path, weeks_threshold=1):
    repo = Repo(repo_path)
    current_date = datetime.datetime.now()

    for branch in repo.branches:
        if branch.name not in ['main', 'master', 'developer']:
            branch_commit = repo.commit(branch.name)
            commit_date = datetime.datetime.fromtimestamp(branch_commit.committed_date)

            delta = current_date - commit_date
            if delta.days > weeks_threshold * 7:
                print(f"Deleting old branch: {branch.name}")
                repo.delete_head(branch.name, force=True)

if __name__ == "__main__":
    # Replace 'path/to/your/repository' with the actual path to your Git repository
    repository_path = 'git@github.com:slarry07/deleting_branches.git'

    if os.path.exists(repository_path):
        delete_old_branches(repository_path)
    else:
        print("Invalid repository path.")
