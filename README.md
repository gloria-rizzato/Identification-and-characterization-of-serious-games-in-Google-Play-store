# Identification-and-characterization-of-serious-games-in-Google-Play-store

![projectssummary](https://github.com/user-attachments/assets/b930ff75-2ce0-4e67-87c2-a67ea13c748a)

- **DATABASE CREATION**: an automatic algorithm in Python identifies serious games among all PlayStore apps based on the "category" and the "description" of the app. Using google search library to query for the app name followed by the words
“google play”, the app ID is retrieved and details about the app are extracted.

![projectpart2](https://github.com/user-attachments/assets/3a59662e-8a83-474c-9de1-28ea3c7e6e6c)

- **SERIOUS GAMES CHARACTERIZATION**:
1. **Gooogle Scholar scraping**: implementation of automated generation of the url to research app references on Google Scholar. The url is used by the Python Request module to fetch the data;
BeautifulSoup is used to extract information and to use CSS (Cascading Style Sheets) selectors to query the page for meaningful data; 
2. **Abstract extraction**: to obtain the needed information for the characterization of the serious games;  
3. **Natural Language Processing (NLP)**: tokenization, POS-tagging, lemmatization. All the steps were done by the usage of nltk library;
4. **Study type classification**: assessment of the level of clinical evidence produced on selected serious games, based on the type of study carried on in associated papers.This was done by analyzing abstracts using a predefined list of keywords specific to each study type, counting the occurrences of common words after natural language processing (NLP) with four established dictionaries.

---
Contributors:Gloria Rizzato, Giulia Peteani, Francesca Ronchetti, Maria Marchesi, Martina Minotti
