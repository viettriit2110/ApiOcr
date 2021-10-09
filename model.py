import json
import easyocr
reader = easyocr.Reader(['ja','en'])

class ORC():
    def __init__(self) -> None:
        pass

    def vertices(intput):
        list_cha = []
        for i in intput:
            list_con = {}
            # print(i[0],i[1])
            list_con["x"] = int (i[0])
            list_con["y"] = int (i[1])
            list_cha.append(list_con)
        return list_cha

    def predict(self,img):
        # stri = i['input'][:-4]
        list_word = []
        # result = reader.readtext('./{}'.format(i['input']))
        result = reader.readtext(img)
        for i in result:
            word = {}
            # print(i[0])
            word["vertices"] = ORC.vertices(i[0])
            word["text"] = i[1]
            list_word.append(word)
        # with open('{}.json'.format(str(stri)),'w',encoding='utf8') as f:
            # json.dump(list_word,f,ensure_ascii=False,indent=4)
        return json.dumps(list_word,encoding='utf8')