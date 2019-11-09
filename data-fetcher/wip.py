from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

from library.constants import LOG_ROOT, NUM_MESSAGES, PROJECT_ID, DATA_SUBSCRIPTION_NAME, ITEM_SIZE, HERO_SIZE, DATABASE_URL

client = FaunaClient(secret="secret", domain=DATABASE_URL, scheme="http", port="8443")

def getIntValue(key):
    sum = 0 
    for char in key:
        sum += ord(char)
    return sum

print(getIntValue('match_count'))

# min_match_duration = 1909
# max_match_duration = 1911
# max_first_blood_time = 2122
# mean_match_duration = 2002
# avg_first_blood_time = 2114
# match_count = 1173

def getAllPairs():
    for i in range(1, HERO_SIZE):
        for j in range(max(i+1, 129), HERO_SIZE):
            hero_pair = {}
            key = format(i, '03d') + format(j, '03d')
            hero_pair['games'] = 0
            hero_pair['wins'] = 0
            try:
                print(client.query(
                    q.create(
                        q.ref(
                            q.collection('hero_pairs'), key
                        ),
                        {'data': hero_pair}
                    )
                ))
            except Exception as e:
                print('Exception for ' + str(key) + ': ' + str(e))

getAllPairs()