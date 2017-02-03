#!/usr/bin/python
#
# The two things you need to change are the files to monitor and the IP address of te SYSLOG server
#It will continue to alert on the same changes until you manually delete the old SHA512 hashes. This is to ensure you do not miss a file change alert.
import os
import re
import hashlib
import time
import subprocess
# needed for backwards compatibility of python2 vs 3 - need to convert to threading eventually
try: import thread
except ImportError: import _thread as thread
import datetime
import shutil
import logging
import logging.handlers
import signal
import socket

if not os.path.exists("C:\\artillery\\db\\"):
    os.makedirs("C:\\artillery\\db\\")

def monitor_system(time_wait):
    # total_compare is a tally of all sha512 hashes
    total_compare = ""
    #CHANGE THIS
    # what files we need to monitor
    check_folders = "C:\\Users,C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup,C:\\inetpub"
    # split lines
    check_folders = check_folders.replace('"', "")
    check_folders = check_folders.replace("MONITOR_FOLDERS=", "")
    check_folders = check_folders.rstrip()
    check_folders = check_folders.split(",")
    # cycle through tuple
    print("Monitoring ", check_folders)
    for directory in check_folders:
        time.sleep(0.1)
        # we need to check to see if the directory is there first, you never
        # know
        if os.path.isdir(directory):
            # check to see if theres an include
            exclude_check = ""
            match = re.search(exclude_check, directory)
            # if we hit a match then we need to exclude
            if not directory in exclude_check:
                # this will pull a list of files and associated folders
                for path, subdirs, files in os.walk(directory):
                    for name in files:
                        filename = os.path.join(path, name)
                        # check for sub directory exclude paths
                        if not filename in exclude_check:
                            # some system protected files may not show up, so
                            # we check here
                            if os.path.isfile(filename):
                                try:
                                    fileopen = open(filename, "rb")
                                    data = fileopen.read()

                                except:
                                    pass
                                hash = hashlib.sha512()
                                try:
                                    hash.update(data)
                                except:
                                    pass
                                # here we split into : with filename :
                                # hexdigest
                                compare = filename + ":" + hash.hexdigest() + "\n"
                                # this will be all of our hashes
                                total_compare = total_compare + compare

    # write out temp database
    print("Writing Out Temp DB")
    temp_database_file = open("C:\\artillery\\db\\temp.database", "w")
    temp_database_file.write(total_compare)
    temp_database_file.close()
    print("Finished Writing Out Temp DB")

    # once we are done write out the database, if this is the first time,
    # create a database then compare
    print("Creating New Integrity DB")
    if not os.path.isfile("C:\\artillery\\db\\integrity.database"):
        # prep the integrity database to be written for first time
        database_file = open("C:\\artillery\\db\\integrity.database", "w")
        database_file.write(total_compare)
        database_file.close()
        print("Done Writing New DB")

    # hash the original database

    print("Hashing And Comparing DB's")
    if os.path.isfile("C:\\artillery\\db\\integrity.database"):
        database_file = open("C:\\artillery\\db\\integrity.database", "r")
        try: database_content = database_file.read().encode('utf-8')
        except: database_content = database_file.read()
        if os.path.isfile("C:\\artillery\\db\\temp.database"):
            temp_database_file = open(
                "C:\\artillery\\db\\temp.database", "r")
            try: temp_hash = temp_database_file.read().encode('utf-8')
            except: temp_hash = temp_database_file.read()

            # hash the databases then compare
            database_hash = hashlib.sha512()
            database_hash.update(database_content)
            database_hash = database_hash.hexdigest()

            # this is the temp integrity database
            temp_database_hash = hashlib.sha512()
            temp_database_hash.update(temp_hash)
            temp_database_hash = temp_database_hash.hexdigest()
            # if we don't match then there was something that was changed
            if database_hash != temp_database_hash:
                # using diff for now, this will be rewritten properly at a
                # later time
                output_file = " "
                for line in open('C:\\artillery\\db\\integrity.database', "r"):
                    if line in open('C:\\artillery\\db\\temp.database', "r"):
                        pass
                    else:
                        output_file += " " + line + "\n"
                for line in open('C:\\artillery\\db\\temp.database', "r"):
                    if line in open('C:\\artillery\\db\\integrity.database', "r"):
                        pass
                    else:
                        output_file += " " + line + "\n"
                #file1 = open('C:\\artillery\\db\\integrity.database', "r" )
                #file2 = open('C:\\artillery\\db\\temp.database', "r" )
                #lines1 = file1.readlines()
                #output_file = " "
                #for i,lines2 in enumerate(file1):
                #    if lines2 != lines1[i]:
                #        output_file += "\n" + lines1 + " Has Changed\n"
                #compare_files = subprocess.Popen(
                #    "FC C:\\artillery\\db\\integrity.database C:\\artillery\\db\\temp.database", shell=True, stdout=subprocess.PIPE)
                #output_file = compare_files.communicate()[0]
                if output_file == "":
                    # no changes
                    pass

                else:
                    subject = "[!] Artillery has detected a change. [!]"
                    output_file = "********************************** The following changes were detected at %s **********************************\n" % (
                        str(datetime.datetime.now())) + str(output_file) + "\n********************************** End of changes. **********************************\n\n"
                    syslog(output_file)

    # put the new database as old
    #if os.path.isfile("C:\\artillery\\db\\temp.database"):
    #    shutil.move("C:\\artillery\\db\\temp.database",
    #                "C:\\artillery\\db\\integrity.database")


def start_monitor():
    time_wait = 360
    while 1:
        thread.start_new_thread(monitor_system, (time_wait,))
        time_wait = int(time_wait)
        time.sleep(time_wait)
        
def syslog(message):
    FACILITY = {
            'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
            'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
            'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
            'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
            'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
        }

    LEVEL = {
            'emerg': 0, 'alert': 1, 'crit': 2, 'err': 3,
            'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
        }
    level=LEVEL['emerg']
    facility=FACILITY['daemon']
    port = 514
    #CHANGE THIS
    host = "172.20.241.3"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '<%d>%s' % (level + facility * 8, message + "\n")
    sock.sendto(data, (host, port))
    sock.close()
start_monitor()

