def app_field(app_doc):
    import re
    app_name = app_doc['title'].lower()
    app_summary = app_doc['summary'].lower()
    # content contains regex related to LSD and ADHD
    content = [r'\bdysgrap[a-z]*', r'\bdyslex[a-z]*', 'adhd', r'\bdyscalcul[a-z]*', r'\banorthog[a-z]*', r'\bdysprax[a-z]*']
    for field in content:
        if field == 'adhd':
            is_name = re.findall(field, app_name)
            is_summary = re.findall(field, app_summary)
            if len(is_name) != 0 or len(is_summary) != 0:
                field = 'ADHD'
                return field
        elif (field == '\\bdysgrap[a-z]*') or (field == '\\bdyslex[a-z]*') or (field == '\\bdyscalcul[a-z]*') or (field == '\\bdysortog[a-z]*') or (field == '\\bdysprax[a-z]*'):
            is_name = re.findall(field, app_name)
            is_summary = re.findall(field, app_summary)
            if len(is_name) != 0 or len(is_summary) != 0:
                # specific learning disability
                field = 'LSD'
                return field
    return 'other'