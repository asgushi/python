import json
from collections import Counter

pythonValue = r'''{"created_at":"Fri Jul 22 13:46:18 +0000 2016","id":756485524894851073,"id_str":"756485524894851073","text":"Rentabilidade do Tesouro Direto sobe nesta sexta-feira; veja taxas: O Tesouro IPCA+ com juros semestrais e ve... https:\/\/t.co\/26jna7Pc8M","source":"\u003ca href=\"http:\/\/twitterfeed.com\" rel=\"nofollow\"\u003etwitterfeed\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":58054653,"id_str":"58054653","name":"ECONOMIA NA WEB","screen_name":"economianaweb","location":null,"url":null,"description":null,"protected":false,"verified":false,"followers_count":1156,"friends_count":6,"listed_count":99,"favourites_count":0,"statuses_count":194031,"created_at":"Sat Jul 18 22:55:19 +0000 2009","utc_offset":-10800,"time_zone":"Brasilia","geo_enabled":false,"lang":"es","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/24345236\/C_pia_de_MeuBackgroundDoTwitter2.JPG","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/24345236\/C_pia_de_MeuBackgroundDoTwitter2.JPG","profile_background_tile":false,"profile_link_color":"0084B4","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"000000","profile_text_color":"F51331","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/322175441\/foto-do-Pol_ticaEnLaWeb_normal.png","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/322175441\/foto-do-Pol_ticaEnLaWeb_normal.png","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/26jna7Pc8M","expanded_url":"http:\/\/bit.ly\/2aie0Rs","display_url":"bit.ly\/2aie0Rs","indices":[113,136]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"pt","timestamp_ms":"1469195178613"}'''

##pythonValue = {"created_at":"Wed Jul 20 02:59:21 +0000 2016",
##               "id":755597938890539008,"id_str":"755597938890539008",
##               "text":"RT @diegoescosteguy: Dilma cada vez mais distante de Bras\u00edlia. https:\/\/t.co\/UWxGt3T3JF",
##               "source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e"}

jsonDataAsPythonValue = json.loads(pythonValue)

#print(jsonDataAsPythonValue)

#filtra string que possui a key:'text'
#conteudo={}
conteudo = str(jsonDataAsPythonValue.get('text',0))
print(conteudo)

#cria lista com as palavras separadas
palavras = conteudo.split()

#word stop - data cleansing
lista_stop_words = ['a', 'as', 'antes', 'até', 'após', 'cada', 'com', 'como', 'contra', 'de', 'da', 'do', 'desde', 'desta', 'deste',
                    'e', 'em', 'entre', 'esta', 'este', 'nesta', 'neste', 'na', 'no', 'o', 'os', 'para', 'por', 'perante',
                    'qual', 'quais', 'quando', 'que', 'quem', 'RT', 'sem', 'sob', 'sobre', 'vez']

for tirar in lista_stop_words:
    if tirar in palavras:
        palavras.remove(tirar)

print(palavras)
print("-------------------------------------------")

contador = Counter(palavras)
print(contador)
