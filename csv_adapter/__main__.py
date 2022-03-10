import sys
import csv_adapter


def main():
    print("Passing arg" + sys.argv[1])
    csv_adapter.run(sys.argv[1])


if __name__ == "__main__":
    main()
