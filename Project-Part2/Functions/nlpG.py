def nlp(text):
    import nltk
    from nltk.stem import WordNetLemmatizer

    text_lemm = []
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    text_token = tokenizer.tokenize(text)
    for w, t in nltk.pos_tag(text_token):
        if t.startswith("NN"): #noun
            l = lemmatizer.lemmatize(w, pos='n')
            text_lemm.append(l)
        elif t.startswith("VB"): #verb
            l = lemmatizer.lemmatize(w, pos='v')
            text_lemm.append(l)
        elif t.startswith("JJ"): #adjective
            l = lemmatizer.lemmatize(w, pos='a')
            text_lemm.append(l)

    return list(dict.fromkeys(text_lemm)) # this is done to remove duplicates