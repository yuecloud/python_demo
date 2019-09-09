import requests
import re
import os
import shutil



#百度搜索爬虫，输入百度图片关键字、然后把对应的图片下载下来
def get_baidu_pic(picdir_name):
    """
    :param 输入需要搜索的关键词:
    :return 将最终的图片过滤然后保存下来:
    """
    word = input("Input key word:")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word
    html = requests.get(url).text
    start_num = 1
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

    for each_url in pic_url:
        pic_end_name = str(each_url.split(".")[-1])
        if pic_end_name in ['jpg', 'jpeg', 'png', 'bmp']:

            try:
                pic = requests.get(each_url, timeout=10)
            except requests.exceptions.ConnectionError as e:
                print('【错误】：当前图片无法下载')
                continue
            else:
                pic_save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), picdir_name,
                                             str(start_num) + "." + pic_end_name)
                with  open(pic_save_path, "wb") as f:
                    f.write(pic.content)
                start_num += 1


if __name__ == "__main__":

    picdir_name = "pictures"
    if os.path.exists(picdir_name):
        shutil.rmtree(picdir_name)

    os.mkdir(picdir_name)
    get_baidu_pic(picdir_name)
