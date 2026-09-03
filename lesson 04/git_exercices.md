<img width="489" height="114" alt="image" src="https://github.com/user-attachments/assets/aabe1f56-c48f-461f-b49f-a5f121464ac3" /># Git - Exercises
In this exercise, ...

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
- Select ‘commit and push to ‘main’’
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







