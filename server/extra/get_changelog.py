import sys
import py
from devpi_server.keyfs import KeyFS
import pprint

if __name__ == "__main__":
    basedir = py.path.local(sys.argv[1], expanduser=True)
    serial = int(sys.argv[2])
    assert basedir.check(), basedir
    keyfs = KeyFS(basedir)
    pprint.pprint (keyfs._fs.get_changelog_entry(serial))
