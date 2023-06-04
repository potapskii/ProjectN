# -*- coding: utf-8 -*-
import functional as fn
import os
import time
import gvar as glb
def main():
    
    # direcories and files that need to be copy are placed in the list
      # TODO: make user input  
    
    if os.path.exists(glb.source[0]):
        print(glb.source[0])
    else:
        print('Something went wrong')
    # for files with spaces need  use double quotes
    # backup copyes should be kept in main backup directory
      # 
    if os.path.exists(glb.target_dir):
        print('target: ' + glb.target_dir)
    else:
        print('Something went wrong')
        exit()
    # files are placed in a zip-archive
    # using current date as a name of subdirectory in a main directory
    today = glb.target_dir + os.sep + time.strftime('%Y%m%d')
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
    print('directory success exits')

    # use zip command "zip -qvf" for placed files to a zip archive
    zip_command = "7z a -tzip -mx5 -r0 {0} {1}".format(target, ' '.join(glb.source))
    #zip_command = "echo \"zip a -tzip -mx5 -r0 {1} {2}.format(target, ' '.join(source))\""
    #zip_command = "dir"
    # run the backup
    if os.system(zip_command) == 0:
        print('backup success exists!!!')
    else:
        print('backup failt')

if __name__ == "__main__":
    main()