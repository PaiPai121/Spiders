from mangadownload import MangaCreeper
MC = MangaCreeper()

def download(begin,end):
    try:
        MC.mainDownload(2,begin,end)
        return True
    except:
        return True

for i in range(5,10):
    begin = i*100 + 1
    end = begin + 100
    while not download(begin,end):
        pass



