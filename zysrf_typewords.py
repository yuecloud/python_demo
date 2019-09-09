import time
import uiautomator2 as u2
import os
import subprocess


#章鱼输入法通过uiautomator2 点击ui来模拟打字操作
def get_pic(device_id, pic_name):
    '''
    调用minicap 进行手机截图操作，保存到 sdcard/save_pic 目录中。( minicap怎么安装，具体百度就可)
    :param device_id:
    :param pic_name:
    :return:
    '''
    str1 = 'adb  -s {0} shell "LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0  ' \
           '-s  > /sdcard/save_pic/{1}.png"'.format(device_id, pic_name)
    pi = subprocess.Popen(str1, stdout=subprocess.PIPE, shell=True)
    time.sleep(1)


def get_sdcard_pic(device_id):
    """
    :param device_id:
    :return:
     将手机sdcard目录中保存的图片文件拉取到电脑目录中
    """
    if not os.path.exists("pic_{}".format(device_id)):
        os.mkdir("pic_{0}_{1}".format(device_id, time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))))
    pi = subprocess.Popen("adb  -s {} shell ls -l /sdcard/save_pic/"
                          .format(device_id), shell=True, stdout=subprocess.PIPE)

    for index, _ in enumerate(pi.stdout.readlines()):
        pic_name = (str(_).split(" ")[-1].strip().replace("\\r\\r\\n'", ""))
        subprocess.Popen("adb  -s {0} pull /sdcard/save_pic/{1}   zysrf_ocrpic/pic_{0}_1".
                         format(device_id, pic_name), shell=True, stdout=subprocess.PIPE)
        time.sleep(0.5)


def type_screen(deive_id, srf_type):
    '''

    :param deive_id: 传入设备号
    :param srf_type: 9键还是26键打字
    :return:
    调用uiautomator2 进行ui点击对应的字母操作，模拟进行打字操作，然后截图获取候选词。
    '''
    d = u2.connect(deive_id)
    sougou_26_dict = {
        "Q": (0.057, 0.684), "W": (0.125, 0.684), "E": (0.253, 0.684), "R": (0.35, 0.684), "T": (0.451, 0.682),
        "Y": (0.538, 0.682),
        "U": (0.64, 0.648), "I": (0.74, 0.684), "O": (0.84, 0.684), "P": (0.94, 0.684),
        "A": (0.105, 0.776), "S": (0.195, 0.776), "D": (0.293, 0.776), "F": (0.4, 0.776),
        "G": (0.5, 0.776), "H": (0.593, 0.776), "J": (0.691, 0.776), "K": (0.789, 0.776), "L": (0.884, 0.776),
        "Z": (0.208, 0.86), "X": (0.295, 0.86), "C": (0.393, 0.86), "V": (0.493, 0.86), "B": (0.596, 0.86),
        "N": (0.689, 0.86), "M": (0.799, 0.86), "DEL": (0.914, 0.86), "SPACE": (0.491, 0.95)
    }
    sougou_9_dict = {
        '2': (0.502, 0.675), '3': (0.702, 0.675),
        '4': (0.288, 0.765), '5': (0.495, 0.675), '6': (0.715, 0.675), 'retry': (0.905, 0.765),
        '7': (0.288, 0.865), '8': (0.495, 0.865), '9': (0.715, 0.865)

    }
    with open(deive_id, "r") as f:
        lines = f.readlines()
    if srf_type == 26:
        srf_input_dict = sougou_26_dict
    else:
        srf_input_dict = sougou_9_dict

    for _ in lines:
        str_item = (_.strip().upper())
        for item in str_item:
            zuobiao = (srf_input_dict.get(item))
            d.click(zuobiao[0], zuobiao[1])
        time.sleep(0.8)
        get_pic(deive_id, str_item.lower())

    # 26键长按de清空候选词，9键点击重输清空候选词
    if srf_type == 26:
        back_zb = sougou_26_dict.get("DEL")
        d.long_click(back_zb[0], back_zb[1], 1)
    else:
        back_zb = sougou_9_dict.get('retry')
        d.click(back_zb[0], back_zb[1])


if __name__ == '__main__':
    starttime = time.time()
    device_id_list = ["DIMZUWBYDQJ75LGE"]
    for deive_id in device_id_list:
        type_screen(deive_id, 26)
    endtime = time.time()
    print(endtime - starttime)

    for _ in device_id_list:
        get_sdcard_pic(_)
