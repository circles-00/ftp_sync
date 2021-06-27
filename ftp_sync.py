import os
from ftplib import FTP
from datetime import datetime as date
import time

# Start Elapsed timer
start = time.time()

# FTP Information
server = 'host'
port = 21 # Set custom port
username = 'username'
password = 'password'

# Connect to Remote FTP Server
ftp = FTP()
ftp.connect(server, port)
ftp.login(username, password)

# Set local and remote path
local_path = r'Absolute path of local directory'
remote_path = r'Absolute path of remote directory'
ftp.cwd(remote_path)

# Open summary file
summary = open(local_path + "\summary.txt", "w")
summary.close()
summary = open(local_path + "\summary.txt", "a")
summary.write("-----------------------------")
summary.write(" Last sync: " + date.now().strftime("%H:%M:%S - %B %d, %Y") + " ")
summary.write("-----------------------------\n")


# Recursive function that handles file uploading to remote server
def upload_song(path):
    os.chdir(path)
    files = os.listdir(path)

    for f in files:
        if os.path.isfile(path + r'\{}'.format(f)):
            if f not in ftp.nlst():
                fh = open(f, 'rb')
                print("----> Now uploading: " + f.title())
                ftp.storbinary('STOR ' + f, fh, 262144)
                summary.write("----> " + f.title() + "\n")
                fh.close()
            else:
                print("----> Song " + f.title() + " already synced")
                summary.write("----> " + f.title() + "\n")

        elif os.path.isdir(path + r'\{}'.format(f)):
            if f not in ftp.nlst():
                ftp.mkd(f)
            ftp.cwd(f)
            print("\n->Now uploading folder: " + f.title())
            summary.write("-> " + f.title() + "\n")
            upload_song(path + r'\{}'.format(f))
    ftp.cwd('..')
    os.chdir('..')


upload_song(local_path)  # call the recursive function
print("Successfully synced all local files with remote directory")

# End the Elapsed Timer
end = time.time()
elapsed = end - start
print(
    "Total Time Elapsed: %02d hours, %02d minutes & %02d seconds" % (elapsed // 3600, elapsed // 60 % 60, elapsed % 60))

summary.write("\nTotal Time Elapsed: %02d hours, %02d minutes & %02d seconds" % (
    elapsed // 3600, elapsed // 60 % 60, elapsed % 60))
summary.close()

# Upload the summary file
print("Uploading summary file")
fh = open(local_path + '\summary.txt', 'rb')
ftp.cwd(remote_path)
ftp.storbinary('STOR ' + 'summary.txt', fh, 262144)
fh.close()
ftp.close()
