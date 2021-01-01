from mangadownload import MangaCreeper
MC = MangaCreeper()

for i in range(5,10):
    begin = i*100 + 1
    end = begin + 100
    MC.mainDownload(2,begin,end)
