# -*- coding: utf-8 -*-
import functional as fn
import os, sys
import time
import gvar as glb
import functional as fn
    # derectories and files are grabbed from file backup.txt
    # direcories and files that need to be copy are placed in the list
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('usage ', sys.argv[0], ' -[f] -[l]')
        exit (123)
    else: 
        if sys.argv[1] == '-l':
            fn.global_backup()
        elif sys.argv[1] == '-f':
            fn.path_from_file()
        elif sys.argv[1] == '-h':
            fn.help_message_show()
        else:
            print('TODO# make default')