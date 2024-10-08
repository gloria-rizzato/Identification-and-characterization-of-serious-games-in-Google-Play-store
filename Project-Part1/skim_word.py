def if_serious_word(app_id):
    from google_play_scraper import app
    import re

    result = app(app_id)
    json_result = result['description']
    regex = re.compile(r'[\r\n\r\n]')
    json_result = regex.sub(" ", json_result)
    json_result = json_result.lower()
    json_result = "".join(u for u in json_result if u not in ("?", ".", ";", ":", "!"))
    word_game = ['game','exergame','serious' , 'games']
    word_child = ['child', 'children', 'kid', 'kids', 'preschooler', 'preeschoolers', 'young', 'younger']
    word_word = ['educational','education','difficulties', 'screening', 'rehabilitation',
                'diagnosis', 'cognitive', 'skill', 'dyslexia', 'skills', 'dysgraphia']
    word_child = ' '.join(map(str, word_child))
    word_game = ' '.join(map(str, word_game))
    word_word = ' '.join(map(str, word_word))
    json_result_list = json_result.split(" ")
    word_list_child = word_child.split(" ")
    word_list_game = word_game.split(" ")
    word_list_word = word_word.split(" ")
    common_word_game = list(set(json_result_list) & set(word_list_game))
    if len(common_word_game) != 0:
        common_word_child = list(set(json_result_list) & set(word_list_child))
        if len(common_word_child) != 0:
            common_word_word = list(set(json_result_list) & set(word_list_word))
            if len(common_word_word) != 0:
                res = {key: result[key] for key in result.keys() & {'title', 'url', 'summary', 'price', 'contentRatingDescription',
                                                                    'developer', 'contentRating'}}
                return res




