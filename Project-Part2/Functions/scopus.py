def scopus(url):

    from urllib.parse import urlparse
    from urllib.parse import parse_qs
    from pybliometrics.scopus import AbstractRetrieval

    # we have to extract eid = scopus identifier
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['eid'][0]
    captured_value = str(captured_value)
    ab = AbstractRetrieval(identifier=captured_value, view='FULL')
    return(ab.abstract)
