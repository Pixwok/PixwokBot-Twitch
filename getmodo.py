from requests import *
#API TWITCH
modo_list = ['cappixwok']
def getmodo():
    response_api = get('https://api.twitch.tv/helix/users?login=cappixwok',
                       headers={
                            'Client-ID': '0scad0g5d8j5qsqerly8hlo5b1ikpr'
                       })
    id_channel = response_api.json()['data'][0]['id']

    response_api = get('https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=%s' % id_channel,
                       headers={
                           'Client-ID': '0scad0g5d8j5qsqerly8hlo5b1ikpr',
                           'Authorization': 'Bearer dr34htq2srh26oq836obaqqm19x1fn'
                       })
    a = len(response_api.json()['data'])
    for i in range(a):
        modo_list.append(response_api.json()['data'][i]['user_name'])