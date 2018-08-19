import argparse
from ..driver import Driver
from .utility import Utility

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command',help="download")

download = subparser.add_parser("download", help="download driver binary")
update = subparser.add_parser("update", help="update driver binary")
delete = subparser.add_parser("delete", help="delete specific driver binary")
elk = subparser.add_parser("elk", help="install elk stack")

download.add_argument("--driver", help="download the respective driver")
update.add_argument("--driver", help="update the respective driver")
delete.add_argument("--driver", help="delete all drivers")
elk.add_argument("--configure", help="install elk stack")

def main():
    args = parser.parse_args()
    args1 = parser.parse_args()
    driver_object = Driver.get_driver(args.driver)()
    configure_object = Driver.get_driver(args1.configure)
    if args.command == "download":
        driver_object.download_driver()
    elif args.command == "update":
        driver_object.update_driver()
    elif args.command == "delete":
        driver_object.delete_driver_history()
    elif args.command == "elk":
        configure_object.Elkmain()

if __name__ == '__main__':
    main()