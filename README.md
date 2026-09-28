# lab04-Urban
# Group Name: Urban

## Who Did What
| Member | GitHub Username | File |
|---|---|---|
| Aung Chan Myae | Rowan10-uzzz | test_teardown.py |
| Toe Twel Tar Htut | YollaYollie | conftest.py |
| Thida Khaing | Thida-Khaing-may | test_deposit.py |
| Kyaw San | KyawSanAlpha | test_withdraw.py |
| Sai Wanna Htoo | lelouchlynx | test_shared.py |

## Our Merge Conflict

During Round 3, all group members edited the `README.md` at around the same time and added their own information to the same section. The first team member successfully pushed their changes, while the other members received merge conflicts because they had also changed the same part of the file.

The conflict markers we encountered were:

Kyaw San
<<<<<<< HEAD
=======
>>>>>>> 757bba87544c98e4fd3e1a03fdde57653a444a51
>>>>>>> 01b5c5bef1744ef349baab814713f8890b20b2bf

Thida Khaing
<<<<<<< HEAD
=======
>>>>>>> 04133a55adec7c9f98dc8c17acdba27b4604ad11

Toe Twel Tar Htut
<<<<<<< HEAD
=======
>>>>>>> 757bba87544c98e4fd3e1a03fdde57653a444a51
>>>>>>> 757bba87544c98e4fd3e1a03fdde57653a444a51
After resolving the conflict, we kept the information for all group members and added each member's name to the final `README.md`. 

Final lines kept:

| Member | GitHub Username | File |
|---|---|---|
| Aung Chan Myae | Rowan10-uzzz | test_teardown.py |
| Toe Twel Tar Htut | YollaYollie | conftest.py |
| Thida Khaing | Thida-Khaing-may | test_deposit.py |
| Kyaw San | KyawSanAlpha | test_withdraw.py |
| Sai Wanna Htoo | lelouchlynx | test_shared.py |

During the conflict resolution process, one member accidentally pulled the repository before properly resolving the conflict and then made changes, which caused the `README.md` to contain only that member's information. As a result, the team had to restart the process and repeat the conflict-resolution steps.

Git could not resolve the conflict automatically because multiple team members had modified the same section of `README.md`. Git could detect that the versions were different, but it could not determine which members' lines should be kept, so the team had to manually resolve the conflicting changes. This is consistent with the lab's explanation that Git stops when changes overlap and it cannot determine which version should remain. 

## Reflection Questions
1. Why was your push rejected, and how did you fix it? 
The push was rejected because remote changes were pushed by a teammate while local work was being done, putting the local branch behind main. It was fixed by running git pull, resolving the merge conflicts in README.md, committing the resolved changes, and pushing again.

2. Why could Git not resolve the README conflict automatically? 
Git could not resolve the conflict automatically because multiple team members edited the exact same lines in README.md simultaneously. Git stops when changes overlap in the same location because it cannot determine which version to keep without human intervention.

3. What is the difference between committing and pushing? 
Committing saves a local snapshot of staged changes to your local Git repository history, while pushing uploads those local commits to a remote repository on GitHub so collaborators can see them.

4. How do fixtures reduce duplicated setup code in tests? 
Fixtures allow common setup and teardown logic (such as initializing a test database or Bank object) to be written once and passed as arguments directly into test functions, eliminating boilerplate across test modules.