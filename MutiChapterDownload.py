from mangadownload import MangaCreeper
MC = MangaCreeper()



for i in range(0,2):
    begin = i*100 + 1
    end = begin + 100
    MC.mainDownload(39,begin,end)



