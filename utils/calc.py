import datetime


def my_sum(lst):
    """
    returns the sum of lst
    """
    s = 0
    for i in lst:
        s = s + i
    return s


def my_avg(lst):
    if not lst:
        raise ValueError("Empty List")

    return my_sum(lst) / len(lst)


class Person(object):
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    @classmethod
    def from_full_name(cls, full_name, dob):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name, dob)

    @property
    def age(self):
        return datetime.date.today() - self.dob

    def __repr__(self):
        return 'Person({!r}, {!r}, {!r})'.format(
            self.first_name, self.last_name, self.dob
        )

    def __str__(self):
        return '{} {} born on {}'.format(
            self.first_name,
            self.last_name,
            self.dob
        )
