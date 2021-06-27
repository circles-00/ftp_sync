# ftp_sync
Synchronize local files with remote files via FTP Protocol using python

This script automatically synchronizes local with remote folder, checking for already synced files along the way(If the file is already there, it will not re-upload it again) and also generates & uploads a summary report of which songs were last synced.

Usage: `python3 ftp_sync.py`

All you need to do is change line 10, 11, 12, 13 (you need to fill these variables with your own ftp information) and lines 21 and 22(to set local and remote folder for synchronization).

I hope this will be some sort of help to you.
Enjoy.
