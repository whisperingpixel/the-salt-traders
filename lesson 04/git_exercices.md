# Git - Exercises
In this exercise, you will create a repository on the university's Gitlab, clone the repository, make some changes on your local desktop and push them to Git.
However, you will first take a look at the Git repository of this course and explore the readme.md-file, the licence and the commits.

## Part 1: Explore the Salt Traders Git
Open https://github.com/whisperingpixel/the-salt-traders/ on your browser.
Explore the page and answer the following questions:

- What is the purpose of a README.md file?
- Which license belongs to the project?
- Why is it important to add a license?
- How many commits are there?
- How does Prof. Sudmanns format his commit messages?
- Are any commit messages not sufficiently informative and concise?



## Part 2: Work with Git

### Log in and create a repository
- Go to https://git.sbg.ac.at/  in your browser
- Log in with your student account
<img width="991" height="790" alt="image" src="https://github.com/user-attachments/assets/6a345634-3940-43c4-9c5d-06e8bfd70853" />

- Click on “Projects”
- Click on “Create a project”
<img width="1301" height="691" alt="image" src="https://github.com/user-attachments/assets/325cd279-816b-48a6-a2c3-006b3992d588" />

- Select “Create blank project”
<img width="1301" height="683" alt="image" src="https://github.com/user-attachments/assets/552ecde3-7355-4f84-86e7-c2d57fe15391" />

- Fill in the details
- Select ‘create project’
<img width="1301" height="691" alt="image" src="https://github.com/user-attachments/assets/5a75133c-e2fe-4743-9eb3-955f431dca48" />

- Click on the README.md-file, select “Edit” and “Open in Web IDE”
- Now, update the README.md-file:
-- Delete everything above ‘## Name’
-- Write 1 sentence under ‘## Name’
-- Write your name under ‘## Authors and acknowledgment’
<img width="1301" height="691" alt="image" src="https://github.com/user-attachments/assets/05d7c6cd-3e3d-4a0f-bf64-2c6b1ebe25f9" />

- Browse to ‘save’
<img width="1301" height="687" alt="image" src="https://github.com/user-attachments/assets/51f0a8ba-1a2e-4ff1-a2b4-2f92d7226a18" />

- Open the ‘source control’ window
- Write an appropriate commit message 
- Select ‘commit and push to ‘main’
<img width="1301" height="683" alt="image" src="https://github.com/user-attachments/assets/c3175707-9092-48e3-8e89-0239869fc5cd" />

- Select ‘Go to project’ to close the editor
<img width="1283" height="681" alt="image" src="https://github.com/user-attachments/assets/7c569db4-4c8f-4797-9b8a-507fdfa0da26" />

### Create SSH keys
First, we ensure that the remote host and your local desktop have a safe way to communicate, by using a private and a public SSH key. 
The private key is like a password: it should not be shared with anyone and it should not be used outside of your desktop.
It is used to decrypt messages.
The public key is like a bank account number: you can share it without problems, because it is worthless without the password (i.e., the private key).
The public key is used to encrypt messages.
As you might have guessed already, we will upload the public key to Git.
First, create a pair of keys. Open the command prompt by typing 'command prompt' in the Explorer and hitting </kbd>Enter</kbd>.
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
Still in the command prompt, type '''notepad ./.ssh/id_ed25519.pub''' to open your public key in Notepad.
Note: replace '''id_ed25519.pub''' with the correct filename, which was shown in the terminal after creating the keys.
Now, copy the content of the .pub-file by using the shortcut </kbd>Ctrl</kbd> + </kbd>A</kbd> to select all contents and </kbd>Ctrl</kbd> + </kbd>V</kbd> to copy them.
The key should start with ssh, followed by a random sequence of characters and ending with your username.
Now, open your browser and navigate back to your project homepage on the university's Gitlab.

### Add the key to Git
- On the project homepage, click on ‘Code’ and select 'Add SSH Key'.
<img width="1283" height="679" alt="image" src="https://github.com/user-attachments/assets/dd11327d-6859-4890-94fa-f524cd0139a0" />

- On the next screen, click 'Add new key'.
<img width="1309" height="519" alt="image" src="https://github.com/user-attachments/assets/0c3e0cbd-a821-430f-9281-e711f0ef8ef2" />

- Fill in the key and a title (which helps to remember which machine it belongs to).
- Leave the 'Usage type' as is and add an expiration date, which is an extra layer of security.
- Once finished, click 'Add key'.
<img width="1294" height="1135" alt="image" src="https://github.com/user-attachments/assets/6abebcc0-73bd-40ae-8902-1a0754a16cbf" />
Navigate back to your project homepage.

- Copy the link under ‘Clone with SSH’.
<img width="1428" height="869" alt="image" src="https://github.com/user-attachments/assets/6a893a9b-b191-48a4-a037-110cc14a9185" />

### Clone the repository
- Open Visual Studio Code, open the ‘source control’ window and select ‘clone repository’
<img width="1083" height="681" alt="image" src="https://github.com/user-attachments/assets/0d32f495-c975-4f4d-a21a-225c3334b84f" />

- Paste the link, which you just copied, and choose a folder.
- Select 'Yes' when Visual Studio Code shows the fingerprint.
- If you have set a passphrase, Visual Studio Code will now ask for it.
Visual Studio Code will open your repository. Browse through the Windows file explorer to ensure that your README.md-file is indeed saved on your desktop now.
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


Before committing these changes, we create a .gitignore file to make sure that our big data files
A .gitignore file is used to prevent large (binary) files from taking up all space in your Git repository.
- In the Windows file explorer, navigate to the local repository and create a file by clicking on the right mouse button and selecting 'New' and 'Test Document'.
<img width="1123" height="826" alt="image" src="https://github.com/user-attachments/assets/9ff28f89-e7db-4de3-877d-23b7b5b23e39" />

- Rename the file to '.gitignore'. The file type will change to GITIGNORE.
<img width="1082" height="212" alt="image" src="https://github.com/user-attachments/assets/09014ca3-ef4b-4597-9518-a307b374d3ff" />
In this file, you can specify which files should be ignored by Git.
Each line points to a single file, folder or to multiple files, by using a file pattern.
Blank lines and lines starting with # are ignored.
For information on file patterns, take a look at the [Official docs](https://git-scm.com/docs/gitignore).
We will specify that we do not want Git to include our data folder and the .txt-files in our output folder.
- Copy the following content to your .gitignore file and then save it.
'''
# Ignore data folder
/data/*

# Ignore .txt files in the output folder
/output/*txt
'''
 Now, your folder structure should look like this:
<img width="246" height="296" alt="image" src="https://github.com/user-attachments/assets/4eccc305-49d9-40db-b1b5-5eb81e1f0838" />

Go back to Visual Studio Code and navigate to your local repo.
Before committing, you have to tell Git your username and email address. 
This information is essential and saved with each commit, so that it is clear which person made each commit in your project.
To do this, open 'Terminal' from the top menu.

<img width="410" height="35" alt="image" src="https://github.com/user-attachments/assets/7701f084-c2a0-4b6e-ae2c-412b57ea271c" />

In the terminal, run the following lines, with your name and email address:
'''
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
'''
Now, open the 'Source Control' window. 
Note that the changes we made, are included here, except for the changes that should be ignored.
<img width="492" height="272" alt="image" src="https://github.com/user-attachments/assets/8eb26eb8-d7b8-430b-9f9d-2f11993470fc" />

Click on the </kbd>+</kbd> sign next to the listing of .gitignore to stage the change made to this file.
Then, write a commit message, such as 'Create .gitignore' and press commit.
Also do this for the other changes.
The commits will appear under 'Graph' in the 'Source Control' Menu.
Finally, select 'Push' to push the changes to your remote Git repository.
<img width="531" height="875" alt="image" src="https://github.com/user-attachments/assets/35e2febc-3b1d-4a7b-ab45-cc762c432dd5" />

Now, go back to your browser and the remote repository to confirm that:
- Your files have been succesfully uploaded.
- The data folder is not uploaded.
- The file 'big_output.txt' is not uploaded, but 'table.csv' is.








