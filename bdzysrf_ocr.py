from aip import AipOcr
import os

#通过百度ocr来识别图片中的文字
class ocr_zysrf():
    """
    调用百度ocr来识别截取图片的文字
    """
    def  __init__(self):
        """
        self.APP_ID='16855381'
        self.API_KEY = 'Pm2Ea6rsjXwjHPmcyEvCLYy8'
        self.SECRET_KEY = 'pkc9H0v60xWSrKGDnHpWhaLiU8bstlEj
        """
        #换成自己百度ocr账号对应的参数,具体值查看 https://ai.baidu.com/docs#/OCR-Python-SDK/925a3d63 如何获取
        self.APP_ID='16855381'
        self.API_KEY = 'Pm2Ea6rsjXwjHPmcyEvCLYy8'
        self.SECRET_KEY = 'pkc9H0v60xWSrKGDnHpWhaLiU8bstlEj'


    """ 读取图片 """
    def get_pic_ocrtext(self,filePath):
        dirname_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(dirname_path,'python_demo','zysrf_ocrpic',filePath), 'rb') as fp:
            image= fp.read()

        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        return  client.general(image).get("words_result")[0].get('words',None)




if  __name__=="__main__":
    print (ocr_zysrf().get_pic_ocrtext("huangjin.png"))

