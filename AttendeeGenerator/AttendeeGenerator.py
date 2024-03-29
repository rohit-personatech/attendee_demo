import string
import random
import json


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random():
    print "generate_random"
    data = []
    for x in range(10000):
        data.append({
            'index': x,
            'id': random_generator(size=10),
            'profileImage': random_generator(size=30),
            'name': random_generator(size=15),
            'profileFieldsHidden': False if x % 3 == 0 else True,
            'company': random_generator(size=10),
            'jobLevel': random_generator(size=10),
            'jobTitle': random_generator(size=15),
            'email': random_generator(size=20),
            'isDeleted': True if x % 7 == 0 else False
        })

    with open('attendee.json', 'w') as outfile:
        json.dump(data, outfile)

    print "done"
    return 0


if __name__ == '__main__':
    generate_random()
