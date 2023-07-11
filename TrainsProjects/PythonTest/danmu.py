import requests,time 

import threading
had_danmu = []
had_sent = []
import random
import requests  # 发送请求
import pandas as pd  # 保存csv文件
import os  # 判断文件是否存在
import time
from time import sleep  # 设置等待，防止反爬
import random  # 生成随机数
import jieba
from PIL import Image as Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

import pyttsx3



list_text = ['666', '主播真厉害',
        '爱了，爱了',
        '关注走一走，活到99',
        '牛逼！！！',
        '秀儿，是你吗？']


def get_infos():
    url = 'https://api.live.bilibili.com/ajax/msg'

    form = {
        'roomid':30079271,
        'csrf_token':''
    }

    count =0 
    engin = pyttsx3.init()
    while True:
        time.sleep(5)
        try:
            res = requests.post(url=url,data=form)
            # print(res.content)
            # print("=====>")
            # print(res.json()['data'])

            text = list(map(lambda li:res.json()['data']['room'][li]['text'],range(10)))
            # print(text)
            for x in text:
                if x not in had_danmu:
                    had_danmu.append(x)
            print("当前弹幕:",had_danmu)

            for danmu in had_danmu:
                time.sleep(2)
                engin.say(danmu)
                engin.runAndWait()


        except Exception as e :
            print(e)
        # break 
        count += 1 
        if count > 10:
            print('退出')
            break



    # time.sleep(10)


def send_msg():
    count = 0 
    while 1:
        count+=1 
        msg = random.choice(list_text)
        try:
            url = 'https://api.live.bilibili.com/msg/send'
            headrs = {
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'cookie':"buvid3=B8D86799-02D1-B6E9-3E9E-1C5819723F0A62324infoc; b_nut=1680136662; _uuid=77EA5A88-F5C5-5352-32AB-F99A7C2103A8861387infoc; buvid4=0235FCEA-AC6E-FE21-FC93-2C0198D601C763015-023033008-CqihqonbP5rCUxMefhAOTA%3D%3D; buvid_fp=f865ebe264ae1af39fdac29f8f41ec37; DedeUserID=296837957; DedeUserID__ckMd5=b5cbfdb24e88ceb1; CURRENT_PID=28d75b30-ce93-11ed-a606-b52a4d44ed2c; rpdid=|(JYYJkJkY|k0J'uY)|uJYYm~; nostalgia_conf=-1; bp_video_offset_296837957=801356905317400600; CURRENT_FNVAL=16; CURRENT_QUALITY=112; SESSDATA=0cd6cd1c%2C1703293599%2Cb9e32%2A62j1a7F0dnojTtLzog7qZOfNSpQ8Goax1vB6odNPAAn_yVmgCljzB_VJz-K6xLKacq-oZy0QAAOQA; bili_jct=91adb2ce303f80b39af31e80eaf7cb68; sid=562esmgx; LIVE_BUVID=AUTO4816877427849578; share_source_origin=COPY; bsource=share_source_copy_link; b_lsid=C97D4349_188F63527BC; innersign=0; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=1080-1752; _dfcaptcha=b43e4277f5ecf2f024bf792c179e7c3b; PVID=3",
                'referer':"https://live.bilibili.com/30079271?spm_id_from=333.1007.0.0",
                "origin":"https://live.bilibili.com"
            }

            data = {
                'buble': '0',
                'msg': msg,
                'color': 16777215,
                'mode': 1,
                'room_type': 0,
                'jumpfrom': 0,
                'fontsize': 25,
                'rnd': 1687758297,
                'roomid': 30079271,
                'csrf': '691adb2ce303f80b39af31e80eaf7cb6876',
                'csrf_token': '691adb2ce303f80b39af31e80eaf7cb6876',
            }

            result = requests.post(url=url,data=data,headers=headrs)
            print(result.content)

           
        except Exception as e:
            print(e)

        time.sleep(5)
        time.sleep(random.randint(0,100))
        if count >10:
            print("退出发送")
            break
        
def trans_date(v_timestamp):
    """10位时间戳转换为时间字符串"""
    timeArray = time.localtime(v_timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def wordcloud(data, name, pic=None, font=None):
    # 使用jieba进行中文分词
    comment = jieba.cut(str(data), cut_all=False)
    words = ' '.join(comment)
    
    # 加载图片并转换为数组
    if pic:
        img = Image.open(pic)
        img_array = np.array(img)
    else:
        img_array = None
    
    # 创建WordCloud对象并生成词云
    wc = WordCloud(width=2000, height=1800, background_color='white', font_path=font, mask=img_array,
                   stopwords=STOPWORDS, contour_width=3, contour_color='steelblue')
    wc.generate(words)
    
    # 将词云保存为图片文件
    wc.to_file(name + '.png')

# wordcloud(df_new["评论内容"], "冰冰", '1.PNG')


def get_data(data):
    data_list = []
    comment_data_list = data["data"]["replies"]
    for i in comment_data_list:
        data_list.append([i['rpid'], i['like'], i['member']['uname'], i['member']['level_info']['current_level'], i['content']['message']])
    return data_list


def save_data(data_type, data):
    if not os.path.exists(data_type + r'_data.csv'):
        with open(data_type + r"_data.csv", "a+", encoding='utf-8') as f:
            f.write("rpid,点赞数量,用户,等级,评论内容\n")
            for i in data:
                rpid = i[0]
                like_count = i[1]
                user = i[2].replace(',', '，')
                level = i[3]
                content = i[4].replace(',', '，')
                row = '{},{},{},{},{}'.format(rpid,like_count,user,level,content)
                f.write(row)
                f.write('\n')
    else:
        with open(data_type + r"_data.csv", "a+", encoding='utf-8') as f:
            for i in data:
                rpid = i[0]
                like_count = i[1]
                user = i[2].replace(',', '，')
                level = i[3]
                content = i[4].replace(',', '，')
                row = '{},{},{},{},{}'.format(rpid,like_count,user,level,content)
                f.write(row)
                f.write('\n')


def test():

    id_list = [996547186,997673466]
    for id in id_list:
        for i in range(2):
            url = "https://api.bilibili.com/x/v2/reply/main?jsnotallow=jsonp&next={}&type=1&oid={}&mode=3&plat=1&_=1632192192097".format(str(i),id)
            print(url)
            d = requests.get(url)
            data = d.json()
            if not data['data']['replies']:
                break
            m_data = get_data(data)
            save_data("main", m_data)
            for j in m_data:
                reply_url = "https://api.bilibili.com/x/v2/reply/reply?jsnotallow=jsonp&pn=1&type=1&oid={}&ps=10&root={}&_=1632192668665".format(id,str(j[0]))
                print(reply_url)
                r = requests.get(reply_url)
                r_data = r.json()
                if not r_data['data']['replies']:
                    break
                reply_data = get_data(r_data)
                save_data("reply", reply_data)
                time.sleep(5)
            time.sleep(5)

def test_csv():
    df = pd.read_csv(r"main_data.csv")
    # print(df,df.head())
    df_new = df.dropna(axis=0,subset=['用户'])
    print("df_new:",df_new)
    wordcloud(df_new["评论内容"], "冰冰2", '111.png',font=r"D:\alphandbeltWorkspace\font\simhei.ttf")


if __name__ == "__main__":

    t = threading.Thread(target=get_infos,args=())
    t.start()
    # send_msg()
    # test()
    # test_csv()
    # data = "支持中文  This is a sample text for generating a word cloud. asdfj;adsmfalsfnakdsjf asdfasiuweoqr asdfasdfd"
    # wordcloud(data, "my_wordcloud", pic=None, font=r"D:\alphandbeltWorkspace\font\simhei.ttf")
    # get_infos()


