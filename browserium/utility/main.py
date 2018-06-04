import argparse

from ..driver import Driver

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command',help="download")
download = subparser.add_parser("download", help="download driver binary")
update = subparser.add_parser("update", help="update driver binary")
download.add_argument("--driver", help="")
update.add_argument("--driver", help="")

def main():
    args = parser.parse_args()
    driver_object = Driver.get_driver(args.driver)()
    if args.command == "download":
        driver_object.download_driver()
    elif args.command == "update":
        driver_object.update_driver()

if __name__ == '__main__':
    main()
