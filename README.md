# csx

1. Download Python -> https://www.python.org/downloads/
  a. IMPORTANT: Check off the "Add to Path" box when installing

2. Create a Github Account -> github.com
  a. Download Git -> https://git-scm.com/downloads
  
3. Download VS Code -> https://code.visualstudio.com/download
      Once you open a VS Code window, the extensions panel can be found after clicking the extension icon on the left sie of the page
      VS Code Extensions to Download:
        Python
        Bracket Pair Colorizer
        TODO Highlight
        
4. Create a foder named 'programming' in your preferred location on your computer (i.e. Desktop)
  a. Inside 'programming' - create a folder named 'python-work'
  
5. Open a VS Code window from your newly installed app. Click "open folder". Find your programming folder. Single click the folder and press "select folder".
  a. Next, to open a terminal in VS Code:
        Use 'Shift + Ctrl + ~'
          
6. To check what your working directory is enter 'pwd' into your terminal. The output is the full pathname of your working directory. Your output should end in "programming"

7. When you want to go up a level in your directory, enter 'cd ..' into your terminal
    ex: if you are in '/Users/firstnamelastname/desktop/programming/python-work'
        Enter in the Terminal: 'cd ..'
        your working directory will then resemble ''somestuff/user/firstnamelastname/desktop/programming'

8. When you want to chamge your working directory, enter 'cd "directory name"'
        if you are in '/Users/firstnamelastname/desktop/programming'
        Enter in the Terminal: 'cd python-work' (If you begin to type the name of the desired directory,
                                                 you can hit the tab button and the directory should fill in)
        your working directory will then be ''/Users/firstnamelastname/desktop/programming/python-work'
        
9. Make sure your working directory is in python-work. Once that is completed, create a repository in Github -> https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository
Then copy the first set of commands from YOUR github window after creating the repository. The commands should resemble these below:
          echo "# INSERT REPOSITORY NAME" >> README.md
          git init
          git add README.md
          git commit -m "first commit"
          git remote add origin REPOSITORY URL
          git push -u origin master
  a. The steps to commit code to Github are:
        'git add .'
        'git commit -m "commit message"
        'git push'
  b. To pull code from the master branch of a repository:
        'git pull origin master'
        
12. Next you should read the lessons from the link below and test your knowledge by solving the assignment related to each lesson.
 a. Go to -> https://github.com/projectinnovatenewark/csx/tree/master/lesons/marking_period_1
 b. You should click on the python-work folder in the left side of your screen so that it is highlighted. Then, by the name of your root folder above python-work, there will be a small set if icons. There's an icon that, when hovered over, says "New File". Click that icon. Input a filename resembles the title of the lesson (i.e. if the lesson is "variables_and_types.py" you could call the file "var_and_types.py"). Press enter once you've written the file name.

13. Copy the todo contents in your new file. To run code in python, click the green arrow at the top right of your VS Code window. You'll need to have the python extension installed in VS Code to see the arrow, so make sure to do that part from the setup step.

14. After solving the todo, head on over to the next lesson and keep on learnin'!



