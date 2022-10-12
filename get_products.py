def get_products(file, alm=True):
    tab = ""

    if alm:
        for linea in file:
            if linea.startswith('00'):
                tab = tab + linea[13:40]+"," + linea[78:80]+"\n"
        return tab
    else:
        for linea in file:
            if linea.startswith('00'):
                tab = tab + linea[0:4]+","\
                    + linea[5:12]+","\
                    + linea[13:40]+","\
                    + linea[56:60]+"," \
                    + linea[64:76]+","\
                    + linea[78:80]+"\n"
        return tab
