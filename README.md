This program converts Ignition hand histories to PokerStars format.  

It will not convert hand histories as you play.

*All hole cards are shown (optional) in HM2's latest version*

<hr>

#### *Short Version*
1. Install <a href="https://www.python.org/downloads/" target="_blank">Python</a>  2.7.x (install the latest 2.7.x which is probably 2.7.11)
  * **DO NOT INSTALL PYTHON 3.5.x, the converter will not work with this version**
  * enable/install ```"Add python.exe to Path"``` and ```"pip"```, no other optional features need to be installed
2. Install <a href="https://www.riverbankcomputing.com/software/pyqt/download" target="_blank">PyQt4</a> (direct download links - <a href="http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x32.exe" target="_blank">32-bit</a>, <a href="http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe" target="_blank">64-bit</a>)
  * only the Qt runtime needs to be installed (minimal install)
3. Install <a href="https://pypi.python.org/pypi/pytz" target="_blank">pytz</a>
  * install via <a href="http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/" target="_blank">Command Prompt</a> with the following command:
    * ```easy_install --upgrade pytz```
4. Download and run the converter
  * scroll to the top of this webpage and download the converter (click on ```"Clone or download"``` then click ```"Download ZIP"```)
  * extract the folder within the zip you downloaded to a new folder on your computer
  * open a Command Prompt window to that folder and run the following command:
    * ```python app.py```
  * the program might load slowly the first time but each time after that it should load quickly
  * **you probably will want to make a shortcut to run the converter (see details below)**

#### *Detailed Version*
1. Install <a href="https://www.python.org/downloads/" target="_blank">Python</a>  2.7.x (install the latest 2.7.x which is probably 2.7.11)
  * **DO NOT INSTALL PYTHON 3.5.x, the converter will not work with this version**
  * on the ```"Customize Python 2.7.x"``` screen (installer's 3rd screen) enable ```"Add python.exe to Path"``` by clicking on it's icon and selecting ```"Will be installed on local hard drive"```
  * on the same screen enable/install ```"pip"``` also (required for step 3)
  * you can choose to not install optional features from the same screen (except ```"Add python.exe to Path"``` and ```"pip"```)
    * click on each item's icon ```"Register Extensions"```, etc. and select ```"Entire feature will be unavailable"``` or ```"Feature will be installed when required"```
  * Test if Python is installed by doing the following:
    * <a href="http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/" target="_blank">open a Command Prompt</a> window
    * type ```python --version```
    * press Enter key
    * if a version is shown then Python is installed
    * **if this is not working you might need to sign out of your Windows user account and sign back in or restart the computer and if it's still not working after that see [Troubleshooting](#Troubleshooting) step 3**
2. Install <a href="https://www.riverbankcomputing.com/software/pyqt/download" target="_blank">PyQt4</a> (direct download links - <a href="http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x32.exe" target="_blank">32-bit</a>, <a href="http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe" target="_blank">64-bit</a>)
  * only the Qt runtime needs to be installed
  * on the ```"Choose Components"``` screen (installer's 3rd screen) uncheck all checkboxes except Qt runtime (or choose ```"Minimal"``` from the drop-down menu)
3. Install <a href="https://pypi.python.org/pypi/pytz" target="_blank">pytz</a>
  * open a Command Prompt window
  * type ```easy_install --upgrade pytz```
  * press Enter key
  * wait for installation to complete
  * if this is not working see [Troubleshooting](#Troubleshooting) step 3
4. Download and run the converter
  * scroll to the top of this webpage
  * click on ```"Clone or download"``` then click ```"Download ZIP"```
  * extract the folder (this folder can be renamed) within the zip you downloaded to a new folder on your computer
  * open a Command Prompt window to that folder (hold shift and right click in/on that folder and then click on ```"Open command window here"```)
  * type ```python app.py```
  * press Enter key and the converter should start running and the GUI should appear (you can minimize the Command Prompt window while it's running), the program might load slowly the first time but each time after that it should load quickly
  * **you probably will want to make a shortcut to run the converter by doing the following:**
    * within the folder you extracted from the zip file make a new text document (right click --> ```"New"``` --> ```"Text Document"```
    * open the text document and type ```python app.py```
    * save the document
    * rename the text document from New Text Document.txt to anyname.cmd (or anyname.bat), you might have to set Windows to show file name extensions to be able rename the file's extension (you can change the setting back to hide file extensions after completing this step)
    * you can double click on this cmd (or bat) file to run the converter, you can also make a shortcut by right clicking on the cmd (or bat) file and then clicking ```"Send to"``` --> ```"Desktop (create shortcut)"``` (the shortcut can be renamed)

## Mac

* Python might already be installed on your system, check by doing the following:
  * open a Terminal window
  * type ```python --version```
  * press Enter key
  * if a version is shown then Python is installed

<a id="Troubleshooting"></a>
## Troubleshooting
1. Try using 32-bit version of PyQt4 instead of 64-bit version.
2. Try installing Python and PyQt4 with default settings (do not do minimal installs)
3. If you did not ```"Add python.exe to Path"``` from step 1 in the [Windows](#Windows) section you can do it manually by editing the ```"PATH"``` or ```"Path"``` user or system environment variable to include both of the following paths:

  C:\Python27\

  C:\Python27\Scripts

  Test if its working by doing the following:
   * open a Command Prompt window
   * type ```python --version```
   * press Enter key
   * if a version is shown then it worked
   * **You might need to sign out of your Windows user account and sign back in or restart the computer after doing this for it to work**
