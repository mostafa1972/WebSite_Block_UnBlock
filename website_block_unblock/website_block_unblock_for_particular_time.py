#import subprocess
import time
from datetime import datetime as dt

TAG = '# Blocked websites'
HOSTS_PATH = r'C:\Windows\System32\drivers\etc\hosts'
WEBSITES = "websites.txt"

if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                       10):
    with open(WEBSITES, 'r') as f:
        lines = f.read().split('\n')
        websites_to_block = [l.strip() for l in lines if len(l) > 0]
    with open(HOSTS_PATH, 'r+') as h:
        lines = h.read().split('\n')

        try:
            i = lines.index(TAG)
            already_blocked = lines[i + 1:]
            lines = lines[:i + 1]
            print('These websites were blocked for time being:')
            for w in already_blocked:
                if not w == '':
                    print('- %s' % w.split()[1])
            print('')
            print('Updating list of blocked websites')

        except ValueError:
            lines.append(TAG)
            print('No websites were blocked')
            print('')

        for w in websites_to_block:
            lines.append('127.0.0.1   %s' % w)
        h.seek(0)
        h.write('\n'.join(lines))
        h.truncate()

    # subprocess.call(['dscacheutil', '-flushcache'])

    print('These websites are now blocked for time being:')
    for w in websites_to_block:
        print('- %s' % w)

else:
    with open(HOSTS_PATH, 'r+') as h:
        lines = h.read().split('\n')

        try:
            i = lines.index(TAG)
            prev_blocked = lines[i + 1:]
            lines = lines[:i]

            h.seek(0)
            h.write('\n'.join(lines))
            h.truncate()

            print('These websites are now unblocked:')
            for w in prev_blocked:
                if not w == '':
                    print('- %s' % w.split()[1])

        except ValueError:
            print('No websites were blocked')

time.sleep(5)
