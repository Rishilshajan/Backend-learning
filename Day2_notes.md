🗓️ Day 2 — Git & Version Control + Syntax Refresher
🎯 Focus:

Understanding Git & GitHub, version control workflow, JavaScript ES6 basics, HTML/CSS layout concepts, and implementing a Stack using Python.


🧩 1. Git & Version Control Concepts
🔹 What is Git?
   => Git is a distributed version control system that tracks changes in source code, allowing multiple developers to collaborate efficiently.

🔹 What is GitHub?
   => GitHub is a cloud-based platform for hosting Git repositories.
   => It enables collaboration, pull requests, issues tracking, and version control over the web.


⚙️ Common Git Commands & Syntax

Command	                                             Description
git init	                                           Initialize a new Git repository.
git add .	                                           Stage all changes for commit.
git status	                                         Check modified/untracked files.
git commit -m "message"	                             Save staged changes with a message.
git branch branch_name	                             Create a new branch.
git checkout branch_name	                           Switch to another branch.
git merge branch_name	                               Merge a branch into the main branch.
git remote add origin <repo_URL>	                   Link local repo to GitHub remote.
git push origin main	                               Push commits to GitHub main branch.
git pull origin main	                               Pull updates from remote repository.    
git log/ git log --oneline --graph --all             View Commit History
git fetch origin                                     Download Remote Changes
git diff                                             Shows Unstaged Changes


⚙️  .gitignore
A .gitignore file specifies which files and folders Git should ignore while tracking.
Common examples:
 __pycache__/
 node_modules/
 .env
 .DS_Store


🔀 Branching and Merging
Branching allows you to create an independent line of development — useful for testing, adding features, or 
fixing bugs without disturbing the main codebase.

# Create a new branch
git branch featureX

# Switch to it
git checkout featureX

# Merge featureX into main
git checkout main
git merge featureX


⚔️ Merge Conflict - A merge conflict occurs when two branches modify the same part of a file, 
and Git cannot automatically decide which version to keep.


Example Scenario:
Branch main changes line 10 in app.py
Branch featureX also changes line 10 in app.py
When merging featureX into main, Git stops and asks you to resolve the conflict manually.


To Resolve:
1.Edit the file manually and keep the correct code.
2.Save and stage changes:
  git add app.py
3.Complete the merge:
  git commit -m "Resolved merge conflict between main and featureX"


⚡ Fast-Forward Merge
A fast-forward merge happens when the branch being merged has no new commits since the feature branch started.
Git simply moves the branch pointer forward — no new merge commit is created.


Example:
 git checkout main
 git merge featureX  # If main had no new commits, it will fast-forward

Diagramatic Representation:
 A --- B --- C         (main)
           \
            D --- E   (feature)

 After Merging:
 A --- B --- C --- D --- E   (main, feature)


🧩 Merge Commit
When branches diverge, Git cannot fast-forward.
In such cases, Git creates a new commit (called a merge commit) that has two parents — combining both histories.

Example: 
 git checkout main
 git merge featureX

Diagrammatic Representation:
       D --- E   (feature)
     /
 A --- B --- C   (main)

 After Merging:
       D --- E
     /       \
 A --- B --- C --- M   (main)


💻 2. GitHub Hands-On Steps

1.Create Repository:

  Name: backend-learning

  Add a README (optional).

2.Local Setup:

  git init
  git remote add origin <repo_URL>

3.Make Three Commits:
  git add .
  git commit -m "Day 1 Notes Added"
  git push origin main
  # Make changes again and commit two more times

4.Create a new Branch:
  git checkout -b Day2

5.Add New File:
  git add Day2_notes.md
  git commit -m "Added Day 2 Notes"
  git push origin Day2

6.Create Pull Request (PR):

  Go to GitHub → Compare & Pull Request → Merge into main.

7.Pull Updated Main Branch:	
  git checkout main
  git pull origin main


⚡ 3. Syntax Hour
🟨 JavaScript ES6 Basics

🧠 Variable Declarations
  var name = "John";   // function-scoped
  let age = 25;        // block-scoped
  const pi = 3.14;     // constant, cannot be reassigned

⚡ Arrow Functions
  const greet = name => `Hello ${name}`;
  console.log(greet("John"));

💬 Template Literals
  let city = "Paris";
  console.log(`${city} is a beautiful place.`);


🟦 HTML & CSS Refresher
🧱 Semantic Tags - Provide meaning to the content for browsers and developers.

Examples:
<header>Header Section</header>
<nav>Navigation Bar</nav>
<section>Main Content</section>
<article>Article Section</article>
<footer>Footer Section</footer>


🧩 Flexbox vs Grid

| Feature | Flexbox         | Grid              |
| ------- | --------------- | ----------------- |
| Type    | 1D (Row/Column) | 2D (Row + Column) |
| Usage   | Aligning items  | Full-page layout  |

Flex Example:
.container {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

Grid Example:
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

🧠 4. DSA Task — Stack Implementation in Python(Backend_learning.ipynb)  

* DSA Tasks are present in Backend_Learning.ipynb


