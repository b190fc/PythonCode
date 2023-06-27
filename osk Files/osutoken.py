
from client_info import Client_Secret, Client_ID

from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

api = Ossapi(Client_ID, Client_Secret)

user = api.user("Es_", key=UserLookupKey.USERNAME)
print(user.id)

top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
# can also use string version of enums
top50 = api.ranking("osu", "performance")

print(top50.ranking)