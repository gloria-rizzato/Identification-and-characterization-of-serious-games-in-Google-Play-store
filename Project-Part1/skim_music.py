def if_serious_music(app_id):
    from google_play_scraper import app
    import re

    result = app(app_id)
    json_result = result['description']
    regex = re.compile(r'[\r\n\r\n]')
    json_result = regex.sub(" ", json_result)
    json_result = json_result.lower()
    json_result = "".join(u for u in json_result if u not in ("?", ".", ";", ":", "!"))
    word_game = ['game', 'exergame', 'serious', 'games']
    word_child = ['child', 'children', 'kid', 'kids', 'preschoolers', 'preschooler', 'young', 'younger']
    word_music = ['coordination', 'fine', 'motor', 'skills', 'hand-eye', 'cognitive', 'skill', 'rehabilitation',
                  'diagnosis', 'autism', 'screening']
    word_child = ' '.join(map(str, word_child))
    word_game = ' '.join(map(str, word_game))
    word_music = ' '.join(map(str, word_music))
    json_result_list = json_result.split(" ")
    word_list_child = word_child.split(" ")
    word_list_game = word_game.split(" ")
    word_list_music = word_music.split(" ")
    common_word_game = list(set(json_result_list) & set(word_list_game))
    if len(common_word_game) != 0:
        common_word_child = list(set(json_result_list) & set(word_list_child))
        if len(common_word_child) != 0:
            common_word_music = list(set(json_result_list) & set(word_list_music))
            if len(common_word_music) != 0:
                res = {key: result[key] for key in result.keys() & {'title', 'url', 'summary', 'price', 'contentRatingDescription',
                                                                    'developer', 'contentRating'}}
                return res




