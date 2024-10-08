def if_serious_trivia(app_id):
    from google_play_scraper import app
    import re

    result = app(app_id)
    json_result = result['description']
    regex = re.compile(r'[\r\n\r\n]')
    json_result = regex.sub(" ", json_result)
    json_result = json_result.lower()
    json_result = "".join(u for u in json_result if u not in ("?", ".", ";", ":", "!"))
    word_game = ['game', 'exergame', 'serious', 'games']
    word_child = ['child', 'children', 'kid', 'kids', 'preschoolers', 'preschooler','young','younger']
    word_trivia = ['learn', 'learning', 'train', 'training', 'skill', 'medical', 'education', 'dyslexia','autism', 'rehabilitation',
                  'brain', 'damage','screening', 'adhd', 'skills']
    word_child = ' '.join(map(str, word_child))
    word_game = ' '.join(map(str, word_game))
    word_trivia = ' '.join(map(str, word_trivia))
    json_result_list = json_result.split(" ")
    words_list_child = word_child.split(" ")
    word_list_game = word_game.split(" ")
    words_list_trivia = word_trivia.split(" ")
    common_word_game = list(set(json_result_list) & set(word_list_game))
    if len(common_word_game) != 0:
        common_word_child = list(set(json_result_list) & set(words_list_child))
        if len(common_word_child) != 0:
            common_word_sport = list(set(json_result_list) & set(words_list_trivia))
            if len(common_word_sport) != 0:
                res = {key: result[key] for key in result.keys() & {'title', 'url', 'summary', 'price', 'contentRatingDescription',
                                                                    'developer', 'contentRating'}}
                return res





