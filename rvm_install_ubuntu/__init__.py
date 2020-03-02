#!/usr/bin/env python3

"""

A script to install RVM and Ruby for you, so you don't have to deal with it.

Note: This script will make changes to your PATH, specifically regarding Ruby

"""

from os import getuid, chdir, getcwd, path, makedirs, system
from termcolor import colored

import getpass

temp_dir_present = False
dest = None


def _cleanup_tmp():
    global dest
    import shutil
    from pathlib import Path

    print('Done with .tmp, cleaning up')

    tmp_path = Path(dest)
    print(path.exists(Path(dest)))
    Path(dest).rmdir()
    print(path.exists(Path(dest)))


if getuid() == 0:
    print('Please do not run this script as root.')
else:
    current = getcwd()
    dest = path.expanduser('~/.tmp')
    if path.exists(dest):
        temp_dir_present = True
        chdir(dest)
    else:
        print(f'Did not find {dest}, making a new one')
        makedirs(dest)
        chdir(dest)

    print('Installing GPG keys for RVM...')
    print('\n')
    system(
        'gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 '
        '7D2BAF1CF37B13E2069D6956105BD0E739499BDB')
    print('\n')
    print(colored('GPG keys installed!', 'green'))
    print('\n')
    print('Downloading and installing RVM and Ruby')

    system('\curl -L https://get.rvm.io | bash -s -- --autolibs=read-fail')
    print(colored('Ruby installed, via RVM. Putting RVM in your PATH...', 'green'))
    print('\n')

    system('echo "source $HOME/.rvm/scripts/rvm" >> ~/.bash_profile')

    print(colored('All done, in order for your Ruby and RVM installations to work properly you will have to either '
                  'restart your computer or close all terminal windows and open a brand-new one.',
                  color="green"))
    print('\n')
    print(colored('If (after you follow the above instructions) you are able to see a value in "rvm:" when you run "'
                  'whereis rvm" in a terminal window then your environment is ready to run Ruby locally. No sudo access'
                  'needed!',
                  color='yellow'))

    if temp_dir_present:
        print(system('\ls'))
        _cleanup_tmp()
