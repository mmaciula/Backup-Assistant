from linux_backup import *
import argparse


def get_args():
    parser = argparse.ArgumentParser("Linux Backup")
    parser.add_argument("-s", "--service", help="drive", default="drive")
    return vars(parser.parse_args())


def main():
    linux_backup = LinuxBackup()
    linux_backup.backup()


if __name__ == '__main__':
    main()