# publications

Publications from the CogRob Group at UC San Diego.

The initial list was adopted from Henrik Christensen
and as such date much further back than the creation of 
the group at UC San Diego

We will maintain the list to enabel simple reporting 
and for update of the website. 

The files are organized in reverse cronological order, 
but can easily be reformatted as needed with bibtools
  
# Steps to update your publications to the website

1. Fork this repository.
2. Fetch the branches and their respective commits from the upstream repository. Commits to BRANCHNAME will be stored in the local branch upstream/BRANCHNAME.
```
    git checkout master
```
3. Pull the latest changes and checkout a new branch for your addition.
```
    git pull
    git checkout -b "branch_name"
```
4. Add your publication to the respective files (for example, for conferences, add in "conf-papers.bib").
5. Add, commit and push your changes.
```
    git add .
    git commit -m "message"
    git push remote_branch branch_name -u
```
6. Create a pull request. This should trigger CI. Monitor it by clicking on details. If the CI fails, download the patch file from artifacts and apply it.
```
    git apply filename.patch
```
7. Repeat step 5 and see your refreshed new commits after patch. This time the CI should pass.
8. If CI passes without errors, merge the PR.
9. Check the publications page of website for the updated publications.

In case you face any problems, please consult Ruffin or Anwesan.
