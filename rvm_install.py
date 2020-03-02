#!/usr/bin/env python3

from os import getpid
from argparse import ArgumentParser
from platform import uname as puname
from helpers import logger

parser = ArgumentParser(prog='rvm_install',
                        usage='rvm_install',
                        allow_abbrev=True,
                        prefix_chars='-+',
                        add_help=True)

# Add argument to get version
parser.add_argument('-V', '--version',
                    action='version',
                    version='a0.2',
                    help='Print the version and quit')

# Add argument to get information from program
parser.add_argument('+v', '--verbose',
                    action='store_true',
                    required=False,
                    default=False,
                    help='Tell the program to output all information that is available while processing')

# Add arguments to allow user to force an installation attempt no matter what pre-checks come back false.
#
# -f --force - Will essentially allow a user to bypass a would-be fatal exception in the install checks by
#              first delivering the exception information and then asking if they want to continue
#
# -F --force-no-confirm - Will do the same as above but will not ask for confirmation before bypassing any
#                         exceptions risen by failed pre-install checks
parser.add_argument('-f', '--force',
                    action='store_true',
                    required=False,
                    default=False,
                    help='Tell the program to attempt an install no matter what pre-install checks fail, '
                         'will confirm continued install attempt after giving more reason for a foreseen failure')


parser.add_argument('-F', '--force-no-confirm',
                    action='store_true',
                    required=False,
                    default=False,
                    dest='force_no_confirm',
                    help='Tell the program to attempt an install no matter what pre-install checks fail, '
                         'will not confirm')

# Parse command-line arguments
args = parser.parse_args()

debug = False

if args.verbose:
    debug = True

log = logger.start('RVMInstaller', debug)
log.debug('Logger started verbosely')

log.info(f'My PID is {getpid()}')

uname = puname()
log.debug(f'Uname dict: {uname}')


if 'Linux' in uname.system:
    if 'Ubuntu' in uname.version:
        print('Yep')
