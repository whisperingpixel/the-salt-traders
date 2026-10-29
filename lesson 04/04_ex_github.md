# Git - Exercises
In this exercise, you will create a repository on Github, clone the repository, make some changes on your local desktop and push them to Github.
However, you will first take a look at the Git repository of this course and explore the readme.md-file, the licence and the commits.

## Part 1: Explore the Salt Traders Git
Open https://github.com/whisperingpixel/the-salt-traders/ on your browser.
Explore the page and answer the following questions:

- What is the purpose of a README.md file?
- Which license belongs to the project?
- Why is it important to add a license?
- How many commits are there?
- How are the commit messages formulated?
- Are any commit messages not sufficiently informative and concise?

## Part 2: Work with Git

### Log in and create a repository
- Go to <https://github.com/>  in your browser
- Click on "Sign up" and follow the steps to create an account. Use your private Email instead of your student Email, so that you can use your Github account in the future as well.
- After Email verification, sign in. You will now be redirected to your "dashboard". 
- Open the side menu and click on “All repositories”

<img width="1855" height="630" alt="image" src="https://github.com/user-attachments/assets/c7e6bdb1-4bb7-44cd-9bf2-1b615b1fd512" />

- Click on “New repository”

<img width="2521" height="403" alt="image" src="https://github.com/user-attachments/assets/4d531b2e-0734-4b6f-b852-b20ca419dc1d" />

- Fill in the details, including a name, description and configuration settings. Select private visibility, so that your repository is not visible to everyone. Add a README, but do not add .gitignore. We will do that later as an exercise. Lastly, it is important to select a license. The GNU Affero General Public Licence v3.0 can be used for free and open source software.
- When finished, select ‘Create repository’

<img width="2526" height="1037" alt="image" src="https://github.com/user-attachments/assets/0f87879e-2104-45be-8d7e-609a3a401bb4" />

- You will now be redirected to the homepage of the repository.

<img width="1629" height="634" alt="image" src="https://github.com/user-attachments/assets/76f1137d-867d-457b-9bab-0e675efcfe32" />


- Click on the README.md-file and select “Edit this file”.
- Now, update the README.md-file:
  - Add some information about the repository
  - Add your name and affiliation
  - Make sure the file is nicely formatted. More information on Markdown formatting can be found online, e.g.: [on this website](https://www.markdownguide.org/cheat-sheet/).
  - Switch from "Edit" to "Preview" mode to see what the README will look like on the homepage of your repository.

<img width="2528" height="526" alt="image" src="https://github.com/user-attachments/assets/11b72b34-e9f3-40aa-9589-b4495297496d" />

- When finished, select "Commit changes" and write an appropriate commit message before again clicking "Commit changes".

<img width="661" height="670" alt="image" src="https://github.com/user-attachments/assets/8565a8d5-0239-423d-9d86-ef995c0e7d0a" />

- You can now safely return to the project homepage and you should see there your updated README.

<img width="2523" height="1017" alt="image" src="https://github.com/user-attachments/assets/6fcaeeb5-6db4-4e7b-9e2e-65092c824e3f" />


### Create SSH keys
First, we ensure that the remote host and your local desktop have a safe way to communicate, by using a private and a public SSH key. 
The private key is like a password: it should not be shared with anyone and it should not be used outside of your desktop.
It is used to decrypt messages.
The public key is like a bank account number: you can share it without problems, because it is worthless without the password (i.e., the private key).
The public key is used to encrypt messages.
As you might have guessed already, we will upload the public key to Git.
First, create a pair of keys. Open the command prompt by typing `command prompt` in the Explorer and hitting </kbd>Enter</kbd>.
The command prompt window will open.

<img width="1114" height="624" alt="image" src="https://github.com/user-attachments/assets/a4d697b9-4854-4304-8e9a-bb9bf4951fdd" />

Type 'ssh-keygen' and hit </kbd>Enter</kbd>.
The terminal asks for a file to save the key.

Hit </kbd>Enter</kbd> to save the key in the default location, which is also shown in the terminal.
Now, the terminal asks for a passphrase.
The passphrase is an extra layer of security to ensure that only you, who knows the passphrase, uses your private key.
If you are working on a shared desktop, this might be a good idea.
However, you will be asked to provide your passphrase anytime Git communicates with the server, which can be annoying.
If you are using your private computer, it is fine to skip the passphrase and just hit </kbd>Enter</kbd> (twice), keeping the passphrase empty.
Now, you should see a random art image, indicating a pair of keys has been generated succesfully.

<img width="1115" height="550" alt="image" src="https://github.com/user-attachments/assets/be1649ef-67f0-46d0-8002-b09e9c4e9ce7" />

Still in the command prompt, type
```shell
notepad ./.ssh/id_ed25519.pub
```
to open your public key in Notepad.
Note: replace `id_ed25519.pub` with the correct filename, which was shown in the terminal after creating the keys.
Now, copy the content of the .pub-file by using the shortcut </kbd>Ctrl</kbd> + </kbd>A</kbd> to select all contents and </kbd>Ctrl</kbd> + </kbd>V</kbd> to copy them.
The key should start with ssh, followed by a random sequence of characters and ending with your username.
Now, open your browser and navigate back to your project homepage on the university's Gitlab.

### Add the key to Git
- Navigate to the page with your account settings.

<img width="388" height="819" alt="image" src="https://github.com/user-attachments/assets/5edd9c40-22f8-4e96-8046-d3f1fc859259" />

- In your account settings, click 'New SSH Key'.

<img width="2528" height="986" alt="image" src="https://github.com/user-attachments/assets/97b0d9e3-85c8-435c-b761-87598003fbb5" />

- Insert the value of your key, which you have created and opened in Notepad previously, and a title (which helps to remember which machine it belongs to).
- Leave the 'Key type' as "Authentication Key".
- Once finished, click 'Add key'. Github will show a message: *You have succesfully added the key 'name_of_key'* and the key should now be visible in your account settings.

Now, navigate back to your project homepage.

- CLick on the green "Code"-menu and copy the URL that is displayed under SSH.

<img width="2527" height="985" alt="image" src="https://github.com/user-attachments/assets/34bcd520-9ccd-4929-88ee-2bd62cb2e58b" />


### Clone the repository
- Open Visual Studio Code, open the ‘source control’ window and select ‘clone repository’

<img width="1083" height="681" alt="image" src="https://github.com/user-attachments/assets/0d32f495-c975-4f4d-a21a-225c3334b84f" />

- Paste the link, which you just copied, and press Enter.
- You will be redirected to Github in your browser, where you have to authorize Visual Studio Code.
- Go back to Visual Studio Code and, if needed, again clone the repository with the URL.
- Choose a folder.
- Select 'Yes' when Visual Studio Code shows the fingerprint.
- If you have set a passphrase, Visual Studio Code will now ask for it.
Visual Studio Code will open your repository. Browse through the Windows file explorer to ensure that your README.md-file is indeed saved on your desktop now, together with a folder called '.git' and a license file.
Congratulations, you have just cloned your Git repository using a secure connection between your desktop and Git!

### Make some changes, commits and pushes
You will make a new file, save it and push it to Git.
You will also make a file, save it and ensure that is is not pushed to Git by using a .gitignore file.
In the end, you will confirm in Git that your work was indeed uploaded.
We start by creating a new folder and some files, all in the local repository on your desktop:
- Create a folder called 'data', containing a file 'big_data.txt'
- Create a folder called 'output', containing a file 'big_output.txt' and a file 'table.csv'
- Create a file called 'processing.py'
You can leave the files empty or add a few random lines.


Before committing these changes, we create a .gitignore file to make sure that our big data files are not included in our commits.
A .gitignore file is used to prevent large (binary) files from taking up all space in your Git repository.
- In the Windows file explorer, navigate to the local repository and create a file by clicking on the right mouse button and selecting 'New' and 'Text Document'.
- Rename the file to '.gitignore'. The file type will change to GITIGNORE.

In this file, you can specify which files should be ignored by Git.
Each line points to a single file, folder or to multiple files, by using a file pattern.
Blank lines and lines starting with # are ignored.
For information on file patterns, take a look at the Official docs: <https://git-scm.com/docs/gitignore>.
We will specify that we do not want Git to include our data folder and the .txt-files in our output folder.

- Copy the following content to your .gitignore file and then save it.

```shell
# Ignore data folder
/data/*
# Ignore .txt files in the output folder
/output/*txt
```

Now, your folder should look like this:

<img width="636" height="240" alt="image" src="https://github.com/user-attachments/assets/edcfee58-87a4-4911-8921-cb28acc7702a" />


Go back to Visual Studio Code and navigate to your local repo.
Before committing, you have to tell Git your username and email address.
This information is essential and saved with each commit, so that it is clear which person made each commit in your project.
To do this, open 'Terminal' from the top menu.

<img width="410" height="35" alt="image" src="https://github.com/user-attachments/assets/7701f084-c2a0-4b6e-ae2c-412b57ea271c" />

In the terminal, run the following lines, with your name and email address:

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Now, open the 'Source Control' window.
Note that the changes we made, are included here, except for the changes that should be ignored.

<img width="492" height="272" alt="image" src="https://github.com/user-attachments/assets/8eb26eb8-d7b8-430b-9f9d-2f11993470fc" />

Click on the </kbd>+</kbd> sign next to the listing of .gitignore to stage the change made to this file.
Then, write a commit message, such as `Create .gitignore` and press commit.
Also do this for the other changes.
The commits will appear under 'Graph' in the 'Source Control' Menu.
Finally, select 'Push' to push the changes to your remote Git repository.

<img width="430" height="809" alt="image" src="https://github.com/user-attachments/assets/839fa4fd-8325-4ea5-967e-7dc577e720ab" />

Now, go back to your browser and the remote repository to confirm that:
- Your files have been succesfully uploaded.
- The data folder is not uploaded.
- The file 'big_output.txt' is not uploaded, but 'table.csv' is.
If you have already started working on the assignment, you can already make a first commit.
