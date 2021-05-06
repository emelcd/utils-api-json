import wikipedia

def searchingW(sterm):
    pages_obj = []
    pag = wikipedia.search(sterm)
    for i in pag:
        try:
            me = {
                "title":i,
                "summary":wikipedia.summary(i),
                "link":wikipedia.page(i).url,
            }
            pages_obj.append(me)
        except:
            pass
    return pages_obj

    
