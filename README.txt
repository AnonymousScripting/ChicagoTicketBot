🚗 CHICAGO TICKET BOT - SETUP GUIDE

👋 HELLO!
This bot will automatically check the City of Chicago website for parking/red light tickets for your entire fleet. 
You do NOT need to know how to code to use this.

========================================================
STEP 1: INSTALL GOOGLE CHROME (Required)
========================================================
1. If you don't have it, download and install Google Chrome:
   https://www.google.com/chrome/
   (The bot uses your real Chrome browser to look like a human).

========================================================
STEP 2: INSTALL PYTHON
========================================================
1. Go to https://www.python.org/downloads/
2. Download the latest version for your computer.
3. Run the installer.
   ⚠️ IMPORTANT (Windows Users): On the very first screen of the installer, 
   you MUST check the box that says "Add Python to PATH". 
   If you miss this, the bot will not work.

========================================================
STEP 3: ADD YOUR CARS
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
STEP 4: RUN THE BOT
========================================================
1. Open the folder containing these files.

👉 IF YOU ARE ON MAC:
   Double-click the file named: RunBot_Mac.command

👉 IF YOU ARE ON WINDOWS:
   Double-click the file named: RunBot_Windows.bat

--- WHAT WILL HAPPEN ---
1. A black window (Terminal) will open.
2. The first time you run it, it might take 1-2 minutes to set up.
3. A Chrome browser will open automatically.
4. The bot will type the license plate for you.
5. When the "I am not a robot" checkmark appears, use your mouse to click it and solve the puzzle.
6. As soon as the green checkmark appears, let go of the mouse! 
   The bot will automatically click Search, take a screenshot of the results, and move to the next car.

========================================================
TROUBLESHOOTING (READ IF IT DOESN'T OPEN)
========================================================

(MAC) "File is damaged" or "Permission Denied":
Apple security blocks downloaded scripts by default. Follow these steps to unlock it:

1. Move this entire folder to your **Desktop**.
2. Open the "Terminal" app on your Mac (Command+Space, type "Terminal").
3. Type the following command and press Enter:
   cd Desktop

4. Type "cd " followed by the name of this folder. 
   (Tip: Type "cd Chicago" and hit TAB to auto-complete the folder name).
   Press Enter.

5. Now type this EXACT command manually to unlock the file:
   xattr -cr RunBot_Mac.command
   (Press Enter)

6. Type this EXACT command manually to make it runnable:
   chmod +x RunBot_M
   
   IMPORTANT: Type the "_M" and THEN hit the TAB key. 
   (If you don't type "M", the computer won't know if you mean Mac or Windows).
   
   It should auto-complete to: chmod +x RunBot_Mac.command
   Press Enter.

7. Close Terminal and double-click the file again. It will work now!

(WINDOWS) "Windows protected your PC":
1. Click "More Info".
2. Click "Run Anyway".

(ALL) The bot crashes immediately:
1. Make sure you have Google Chrome installed.
2. Make sure you didn't delete a comma or quote in the fleet.json file.