🚗 CHICAGO TICKET BOT - SETUP GUIDE

👋 HELLO!
This bot will automatically check the City of Chicago website for parking/red light tickets for your entire fleet. 
You do NOT need to know how to code to use this.

========================================================
STEP 1: INSTALL PYTHON (You only need to do this once)
========================================================
1. Go to https://www.python.org/downloads/
2. Download the latest version for your computer.
3. Run the installer.
   ⚠️ IMPORTANT (Windows Users): On the very first screen of the installer, 
   you MUST check the box that says "Add Python to PATH". 
   If you miss this, the bot will not work.

========================================================
STEP 2: ADD YOUR CARS
========================================================
1. Look for the file named "fleet.json" in this folder.
2. Open it with any text editor (Notepad, TextEdit, etc.).
3. You will see my example cars. Replace them with your real cars.
   
   It looks like this:
   {
     "plate": "FH88866",
     "state": "IL",
     "company": "Cybernex Auto LLC"
   }

   Make sure you keep the quotes "" and commas exactly as they are!

========================================================
STEP 3: RUN THE BOT
========================================================
1. Open the folder containing these files.

👉 IF YOU ARE ON MAC:
   Double-click the file named: RunBot_Mac.command

👉 IF YOU ARE ON WINDOWS:
   Double-click the file named: RunBot_Windows.bat

--- WHAT WILL HAPPEN ---
1. A black window (Terminal) will open.
2. The first time you run it, it might take 1-2 minutes to "Install Libraries" and "Check Browser Engine". This is normal.
3. A Chrome browser will open and go to the Chicago website.
4. The bot will type the license plate for you.
5. When the "I am not a robot" checkmark appears, use your mouse to click it and solve the puzzle.
6. As soon as the green checkmark appears, let go of the mouse! 
   The bot will automatically click Search, take a screenshot of the results, and move to the next car.

========================================================
TROUBLESHOOTING
========================================================

(MAC) "Permission Denied" or file won't open:
1. Open your "Terminal" app (Command + Spacebar, type 'Terminal').
2. Type: chmod +x 
   (Make sure there is a space after the x).
3. Drag the 'RunBot_Mac.command' file into the terminal window.
4. Press Enter.
5. Now try double-clicking the file again.

(WINDOWS) "Windows protected your PC":
1. Click "More Info".
2. Click "Run Anyway".

(ALL) The bot crashes immediately:
1. Make sure you didn't delete a comma or quote in the fleet.json file.
2. Make sure you installed Python.