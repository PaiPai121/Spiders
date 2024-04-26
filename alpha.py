text = ""
with open("test.txt","r",encoding="utf8") as f:
    line = f.readline()
    text += line
    while line:
        line = f.readline()
        text  += line
with open("out.txt","w",encoding="utf8") as f:
    for i in range(0,len(text),6):
        temp = text[i:i+6] + " "
        f.write(temp)