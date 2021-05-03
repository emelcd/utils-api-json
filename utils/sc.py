import wikipedia

def searchingW(sterm):
    pages_obj = []
    pag = wikipedia.search(sterm)
    # print(pag)
    for i in pag:
        # summ=wikipedia.summary(i, sentences=1)
        try:
            me = {
                "title":i,
                "summary":wikipedia.summary(i,sentences=2),
                "link":wikipedia.page(i).url,
                
            }
            pages_obj.append(me)
        except:
            pass


    return pages_obj
