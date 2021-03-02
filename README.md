# An Extremely Simple DayOne Exporter

## Goal
* Export all the entries in the DayOne database to markdown files in a folder.  
* Maintain the created time and modified time to the files. 
* No tags (could be added by macos_tags library if needed) and photos. 
* No journal/book support (I only have one journal)

## Why? 
My DayOne app just got stuck every time it launches suddenly since Feb 22, 2021. Reached to the Support team, and they recommended to delete and reinstall the app if you were premium user, in which all data would be restored from the cloud. Unfortunately I was not a premium user that time, and no more response from the Support team. 

## Requirement 

Python 3.6 or higher in MacOS.

## Usage
```
mkdir ~/DayOneEntries
cd ~/DayOneEntries
cp ~/Library/Group Containers/5U8NS4GX82.dayoneapp2/DayOne.sqlite ~/DayOne_exporter
python3 DayOne_exporter.py
```

## Note
Use it as you want and risk it as you use, for this script and DayOne.
