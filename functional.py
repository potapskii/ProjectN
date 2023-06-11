# -*- coding: utf-8 -*-
import gvar as g
import os, time

def global_backup():
    for p in g.source:
        if os.path.exists(p):
            print(p)
        else:
            print('Error: Invalid global Path, --> ', p)
            exit(1)  
    # for files with spaces need  use double quotes
    # backup copyes should be kept in main backup directory
      #
    if os.path.exists(g.target_dir):
        print('target: ' + g.target_dir)
    else:
        print('Something went wrong')
        exit(1)
    # files are placed in a zip-archive
    # using current date as a name of subdirectory in a main directory
    today = g.target_dir + os.sep + time.strftime('%Y%m%d')
    # using current time  as a name of a zip archive
    now = time.strftime('%Y%m%d')
    # we request user comment for file name
    comment = input('Enter comment -->')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' +\
            comment.replace(' ', '_') + '.zip'
    print(target)
    # creating directory if it not exists
    if not os.path.exists(today):
        os.mkdir(today)
        print('The new directory success exits ', today)
    # run the backup
    zip_command = "7z a -tzip -mx5 -r0 {0} {1}".format(
        target, ' '.join(g.source))
    if os.system(zip_command) == 0:
        print('backup success exists!!!')
    else:
        print('backup failt')

def path_from_file():
    # open and read file
    with open("C://Users//PC//PYTHON//ProjectN//backup.txt", "r") as f:
        for line in f.readlines():
            p = line[:-1]
            if os.path.exists(p):
                print('The path', p, ' has been added successefuly')  # for debug
                g.path_lst.append(p)
            else:
                if p != 'END':
                    print('doesn\'t exists dir --> ', p)
                    exit(11)
                else:
                    print(p)

    # for files with spaces need  use double quotes
    # backup copyes should be kept in main backup directory

    if os.path.exists(g.target_dir):
        print('target: ' + g.target_dir)
    else:
        print('Something went wrong')
        exit(1)
    # files are
    # files are placed in a zip-archive
    # using current date as a name of subdirectory in a main directory
    today = g.target_dir + os.sep + time.strftime('%Y%m%d')
    # using current time  as a name of a zip archive
    now = time.strftime('%Y%m%d')
    # we request user comment for file name
    comment = input('Enter comment --> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' +\
            comment.replace(' ', '_') + '.zip'
    print(target)
    # creating directory if it not exists
    if not os.path.exists(today):
        os.mkdir(today)
        print('directory success exits ', today)

    # use zip command "zip -qvf" for placed files to a zip archive
    zip_command = "7z a -tzip -mx5 -r0 {0} {1}".format(target, ' '.join(g.path_lst)) # run backup ...
    if os.system(zip_command) == 0:
        print('backup success exists!!!')
    else:
        print('backup failt')
