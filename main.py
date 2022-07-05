import sys

from utils.calc import my_avg


def main():
    numbers = []
    errors = []
    for i in sys.argv[1:]:
        try:
            numbers.append(float(i))
        except ValueError:
            errors.append(
                  "{!r} couldn't be converted to an integer".format(i),
            )

    if errors:
        print(errors, file=sys.stderr)
        sys.exit(1)

    print(my_avg(numbers))


if __name__ == '__main__':
    main()
