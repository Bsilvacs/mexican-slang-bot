#!"c:\users\benjaminsilva\documents\visual studio 2012\Projects\MexicanSlangBot\MexicanSlangBot\env\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'praw==2.1.4','console_scripts','praw-multiprocess'
__requires__ = 'praw==2.1.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('praw==2.1.4', 'console_scripts', 'praw-multiprocess')()
    )
