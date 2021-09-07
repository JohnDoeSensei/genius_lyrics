import wikipediaapi

WORD_DELETE = ['(rappeur français)','(artiste)','(rappeur)','(chanteur)','vidéaste','rap','musicien']





def print_categorymembers(categorymembers, word_delete, level=0, max_level=1):
    list_title_page = []
    for c in categorymembers.values():
        c_str = c.title
        for w in word_delete :
            c_str = c_str.replace(w, '')
        list_title_page.append(c_str)

    return list_title_page


def get_rapper_fr(word_delete=WORD_DELETE) :
    wiki_wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page_rapper_fr = wiki_wiki.page("Catégorie:Rappeur_français")
    list_rapper_fr = print_categorymembers(page_rapper_fr.categorymembers, word_delete)
    #print(list_rapper_fr)
    return list_rapper_fr

get_rapper_fr(WORD_DELETE)