import argparse
from ..driver import Driver
from browserium.utility.utility import Utility

class Main(object):
    # parser = argparse.ArgumentParser()
    # subparser = parser.add_subparsers(dest='command',help="download")

    # download = subparser.add_parser("download", help="download driver binary")
    # update = subparser.add_parser("update", help="update driver binary")
    # delete = subparser.add_parser("delete", help="delete specific driver binary")

    # download.add_argument("--driver", help="download the respective driver")
    # update.add_argument("--driver", help="update the respective driver")
    # delete.add_argument("--driver", help="delete all drivers")

    # def main():
    def __init__(self):
        self.ut = Utility()

    def configure_parser(self):
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest='command',help="download")

        download = subparser.add_parser("download", help="download driver binary")
        update = subparser.add_parser("update", help="update driver binary")
        delete = subparser.add_parser("delete", help="delete specific driver binary")

        download.add_argument("--driver", help="download the respective driver")
        update.add_argument("--driver", help="update the respective driver")
        delete.add_argument("--driver", help="delete all drivers")
        args = parser.parse_args()

        driver_object = Driver.get_driver(args.driver)()
        if args.command == "download":
            driver_object.download_driver()
        if args.command == "update":
            driver_object.update_driver()
        if args.command == "delete":
            self.ut.delete_driver_history()

m = Main()
m.configure_parser()

# if __name__ == '__main__':
#     main()