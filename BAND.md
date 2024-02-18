# Using BAND for the course

Here is a step guide for running the course exercises on BAND.
- Go to [https://band.embl.de](https://band.embl.de)
    - Agree to the terms of services and privacy note and log in.
    - You can then log in with your google account. If you are logging in the first time this may take a while.
- After you have logged in, start an online desktop:
    - Choose the number of CPUs (recommended: 4), memory (recommended: 24GB) and number of GPUs (1) and click launch. See 1. in the overview below.
        - You can also set a time limit (default: 2 days). After this time your desktop will be shut down (you can then start a new one).
    - After a few seconds an item should appear in `Running desktops`. Click `GO TO DESKTOP` to connect to it.
    - If you already have a desktop running you don't need to start a new one, just connect to the existing one.
- If you start BAND for the first time (or use it for this course for the first time) then you have to download the exercises via git:
    - Open a terminal by clicking the terminal symbol in the top left corner, see 2. in the overview. This will open a terminal window.
    - Then enter `git clone https://github.com/computational-cell-analytics/dl-for-micro` in it and press enter.
    - This will download all materials for the course.
- Now you can start jupyter, which we use to work on the exercises:
    - Click on the `Applications` button in the top left corner and then select `Programming->JupyterLab`.
    - This will open a new window (it may take up to a minute) with the jupyter environment.
    - You can now open any of the exercises with it. They are in the folder `dl-for-micro` (that you have downloaded earlier). See 3. in the overview.
    - We recommend that you start with the notebook `data-visualization-napari`.
    - To run it (and the other notebooks), you need to select the kernel `micro_sam`. See 4. in the overview.

## Tips & Tricks

Because BAND is running in the browser, the shortcuts you know for copying and pasting text are not working quite as usual. It is however very convenient to copy and paste text between your laptop and BAND, and to copy and paste inside of jupyter, so it's good to learn how this works in BAND:

**Copy and paste between your laptop and BAND:**
- Press `Ctrl + Shift + Alt` in your browser window with BAND. This will open a text field that you can use to copy and paste into from your laptop and from BAND. (See screenshot below).
- To copy from your laptop to BAND, first copy the text on your laptop (e.g. via `Ctrl + C`), then paste it into the window opened via `Ctrl + Shift + Alt`, then select the text again there and copy it (`Ctrl + C`). Now you can close the window (by pressing `Ctrl + Shift + Alt` again), and then paste the text within BAND.

**Copy and paste in jupyter:**
- It is often very convenient to copy and paste text or code when working in jupyter. You can do this via the following shortcuts:
    - Copy text via `Ctrl + C` (as usual)
    - Paste text via `Ctrl + Shift + V` (different from the usual shortcut!)

You can find more infos on how to use BAND:
- In the [user guide](https://docs.google.com/document/d/1TZBUsNIciGMH_g4aFj2Lu_upISxh5TV9FBMrvNDWmc8/edit?usp=sharing)
- In the [video tutorial](https://drive.google.com/file/d/11pbF70auGyWF-1ir2XUGM8fgiY7ETxP8/view?usp=sharing)
