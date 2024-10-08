def get_apps(path):
    import pandas as pd
    import play_scraper

    df = pd.read_csv(path)
    categories = df['Category']
    # selected_cat = ['Books & Reference', 'Medical', 'Educational', 'Education','Trivia', 'Word', 'Music'] 
    selected_cat = ['Music']
    selected_apps = df[df['Category'].isin(selected_cat)]
    
    return selected_apps
