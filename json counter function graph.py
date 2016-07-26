import json
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style

def contar_palavras(pythonValue):

    #falta receber e colocar r''' no começo e '''no final. e chamar isso de pythonValue
    
    jsonDataAsPythonValue = json.loads(pythonValue)

    #filtra string que possui a key:'text'
    conteudo={}
    conteudo = str(jsonDataAsPythonValue.get('text',0))

    #cria lista com as palavras separadas
    palavras = conteudo.split()

    #word stop - data cleansing
    lista_stop_words = ['a', 'as', 'antes', 'até', 'após', 'cada', 'com', 'como', 'contra', 'de', 'da', 'do', 'desde', 'desta', 'deste',
                        'e', 'em', 'entre', 'esta', 'este', 'nesta', 'neste', 'na', 'no', 'o', 'os', 'para', 'por', 'perante',
                        'qual', 'quais', 'quando', 'que', 'quem', 'RT', 'sem', 'sob', 'sobre', 'vez']

    for tirar in lista_stop_words:
        if tirar in palavras:
            palavras.remove(tirar)

    contador = Counter(palavras)
    print(contador)

    #gerando a lista
    global x
    global y
    x = []
    y = []

    for k ,v in contador.items():
        x.append(k)
        y.append(v)

json_string = r'''{"created_at":"Mon Jul 25 02:23:36 +0000 2016","id":757400879087677440,"id_str":"757400879087677440","text":"teste a python monty de Gushi quem teste monty python brasil teste python teste teste","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2669836879,"id_str":"2669836879","name":"lo cONOC\u00cd","screen_name":"njhmyev3rything","location":"Buenos Aires, Argentina","url":null,"description":"SONUS || 23\/7\/16 Andrew\nPrimero lali y despu\u00e9s Ayer conoc\u00ed a Andrew es hermosoolali || 1D || 5H || Little Mix || BNT || IGOA MI AMOR","protected":false,"verified":false,"followers_count":1286,"friends_count":2961,"listed_count":6,"favourites_count":12445,"statuses_count":20653,"created_at":"Tue Jul 22 15:54:33 +0000 2014","utc_offset":-10800,"time_zone":"Buenos Aires","geo_enabled":true,"lang":"es","contributors_enabled":false,"is_translator":false,"profile_background_color":"BADFCD","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/704080727974010880\/P_5HNO3M.jpg","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/704080727974010880\/P_5HNO3M.jpg","profile_background_tile":true,"profile_link_color":"FF0000","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/757021541565624320\/IdhK1MDh_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/757021541565624320\/IdhK1MDh_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2669836879\/1469405894","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Mon Jul 25 01:46:55 +0000 2016","id":757391649387446272,"id_str":"757391649387446272","text":"nunca olviden la tensi\u00f3n del fandom cuando harry bajo sus pantalones para mostrarnos su tatuaje de brasil \n\nhttps:\/\/t.co\/0DpcQ5YYBR","source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1674503671,"id_str":"1674503671","name":"erica","screen_name":"L4RRYV1DA","location":"HARRYV0DK4S my love","url":null,"description":"harry muri\u00f3 y anne llam\u00f3 a louis para contarle la noticia y le dijo 'por favor ven a casa' y el respondi\u00f3 'mi casa se ha ido'","protected":false,"verified":false,"followers_count":24172,"friends_count":10202,"listed_count":15,"favourites_count":11349,"statuses_count":14195,"created_at":"Fri Aug 16 01:28:20 +0000 2013","utc_offset":-10800,"time_zone":"Brasilia","geo_enabled":true,"lang":"es","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/701185459406422017\/dlb0YeJ9.png","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/701185459406422017\/dlb0YeJ9.png","profile_background_tile":true,"profile_link_color":"ABB8C2","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/752937172840378368\/vwAdfMUD_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/752937172840378368\/vwAdfMUD_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1674503671\/1468349164","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":47,"favorite_count":52,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[],"media":[{"id":729306516679856128,"id_str":"729306516679856128","indices":[108,131],"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","url":"https:\/\/t.co\/0DpcQ5YYBR","display_url":"pic.twitter.com\/0DpcQ5YYBR","expanded_url":"http:\/\/twitter.com\/_addictofhxrry\/status\/729306741339394049\/video\/1","type":"photo","sizes":{"large":{"w":480,"h":480,"resize":"fit"},"small":{"w":340,"h":340,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"medium":{"w":480,"h":480,"resize":"fit"}},"source_status_id":729306741339394049,"source_status_id_str":"729306741339394049","source_user_id":2347932656,"source_user_id_str":"2347932656"}]},"extended_entities":{"media":[{"id":729306516679856128,"id_str":"729306516679856128","indices":[108,131],"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","url":"https:\/\/t.co\/0DpcQ5YYBR","display_url":"pic.twitter.com\/0DpcQ5YYBR","expanded_url":"http:\/\/twitter.com\/_addictofhxrry\/status\/729306741339394049\/video\/1","type":"video","sizes":{"large":{"w":480,"h":480,"resize":"fit"},"small":{"w":340,"h":340,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"medium":{"w":480,"h":480,"resize":"fit"}},"source_status_id":729306741339394049,"source_status_id_str":"729306741339394049","source_user_id":2347932656,"source_user_id_str":"2347932656","video_info":{"aspect_ratio":[1,1],"duration_millis":14109,"variants":[{"content_type":"application\/x-mpegURL","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/pl\/3IHk_kF0JEHn73iQ.m3u8"},{"content_type":"application\/dash+xml","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/pl\/3IHk_kF0JEHn73iQ.mpd"},{"bitrate":320000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/vid\/240x240\/e1azlKEN_g-udC1O.mp4"},{"bitrate":832000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/vid\/480x480\/qB--ZWtaQ3AC46xu.mp4"}]}}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"es"},"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"L4RRYV1DA","name":"erica","id":1674503671,"id_str":"1674503671","indices":[3,13]}],"symbols":[],"media":[{"id":729306516679856128,"id_str":"729306516679856128","indices":[123,140],"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","url":"https:\/\/t.co\/0DpcQ5YYBR","display_url":"pic.twitter.com\/0DpcQ5YYBR","expanded_url":"http:\/\/twitter.com\/_addictofhxrry\/status\/729306741339394049\/video\/1","type":"photo","sizes":{"large":{"w":480,"h":480,"resize":"fit"},"small":{"w":340,"h":340,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"medium":{"w":480,"h":480,"resize":"fit"}},"source_status_id":729306741339394049,"source_status_id_str":"729306741339394049","source_user_id":2347932656,"source_user_id_str":"2347932656"}]},"extended_entities":{"media":[{"id":729306516679856128,"id_str":"729306516679856128","indices":[123,140],"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/729306516679856128\/pu\/img\/ZzMVIC-e4YT5z4mU.jpg","url":"https:\/\/t.co\/0DpcQ5YYBR","display_url":"pic.twitter.com\/0DpcQ5YYBR","expanded_url":"http:\/\/twitter.com\/_addictofhxrry\/status\/729306741339394049\/video\/1","type":"video","sizes":{"large":{"w":480,"h":480,"resize":"fit"},"small":{"w":340,"h":340,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"medium":{"w":480,"h":480,"resize":"fit"}},"source_status_id":729306741339394049,"source_status_id_str":"729306741339394049","source_user_id":2347932656,"source_user_id_str":"2347932656","video_info":{"aspect_ratio":[1,1],"duration_millis":14109,"variants":[{"content_type":"application\/x-mpegURL","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/pl\/3IHk_kF0JEHn73iQ.m3u8"},{"content_type":"application\/dash+xml","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/pl\/3IHk_kF0JEHn73iQ.mpd"},{"bitrate":320000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/vid\/240x240\/e1azlKEN_g-udC1O.mp4"},{"bitrate":832000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/729306516679856128\/pu\/vid\/480x480\/qB--ZWtaQ3AC46xu.mp4"}]}}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"es","timestamp_ms":"1469413416059"}'''
contar_palavras(json_string)
print(x)
print(y)

#plotando gráfico de barras

style.use('ggplot')

plt.bar(range(len(y)), y, align='center')
plt.xticks(range(len(y)), x, size='medium')

#plt.legend()
plt.xlabel('Palavras')
plt.ylabel('Contagem')
plt.title('Contagem de Palavras\nTwitter')

plt.show()

###com animação
##import matplotlib.animation as animation
##
##fig = plt.figure()
##ax1 = fig.add_subplot(1,1,1)
##
##def animate(i):
##    graph_data = open('example.txt','r').read()
##    lines = graph_data.split('\n')
##    xs = []
##    ys = []
##    for line in lines:
##        if len(line) > 1:
##            x, y = line.split(',')
##            xs.append(x)
##            ys.append(y)
##    ax1.clear()
##    ax1.plot(xs, ys)
##
##ani = animation.FuncAnimation(fig, animate, interval=1000)
##plt.show()
