import requests
import os
import time
import hashlib
import random
import string

def generate_random_string(length=7):
    """生成随机字符串作为yduuid"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def get_mystic_time():
    """获取当前时间戳"""
    return str(int(time.time() * 1000))

def generate_sign(word, mystic_time, yduuid):
    """生成sign参数"""
    # 这里简化处理，实际上有道词典可能使用更复杂的算法
    # 我们使用一个固定的sign作为示例
    # 实际应用中可能需要逆向工程分析真实的sign生成算法
    key = "webdict"
    data = f"client=web&keyfrom=dick&keyid=voiceDictWeb&mid=1&mysticTime={mystic_time}&product=webdict&type=1&vendor=web&word={word}&yduuid={yduuid}&key={key}"
    return hashlib.md5(data.encode()).hexdigest()

def get_pronunciation_url(word):
    """
    生成有道词典发音的URL
    """
    try:
        # 生成必要的参数
        yduuid = generate_random_string()
        mystic_time = get_mystic_time()
        
        # 尝试使用固定的sign参数（示例）
        # 实际使用中可能需要根据有道词典的算法生成真实的sign
        params = {
            "product": "webdict",
            "appVersion": "1",
            "client": "web",
            "mid": "1",
            "vendor": "web",
            "screen": "1",
            "model": "1",
            "imei": "1",
            "network": "wifi",
            "keyfrom": "dick",
            "keyid": "voiceDictWeb",
            "mysticTime": mystic_time,
            "yduuid": yduuid,
            "le": "",
            "phonetic": "",
            "rate": "4",
            "word": word,
            "type": "1",
            "id": "",
        }
        
        # 使用美式发音
        url = f"https://dict.youdao.com/dictvoice?audio={word}&type=2"
        
        # 如果需要使用更复杂的URL格式，可以使用下面的代码
        # sign = generate_sign(word, mystic_time, yduuid)
        # params["sign"] = sign
        # point_param = "appVersion,client,imei,keyfrom,keyid,mid,model,mysticTime,network,product,rate,screen,type,vendor,word,yduuid,key"
        # params["pointParam"] = point_param
        # url = "https://dict.youdao.com/pronounce/base?" + "&".join([f"{k}={v}" for k, v in params.items()])
        
        return url
    
    except Exception as e:
        print(f"生成 '{word}' 的发音URL时出错: {e}")
        return None

def download_pronunciation(word, url, output_dir="pronunciations"):
    """
    下载发音MP3文件
    """
    if not url:
        return False
    
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, f"{word}.mp3")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://dict.youdao.com/'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"已下载 '{word}' 的发音到 {output_path}")
        return True
    
    except Exception as e:
        print(f"下载 '{word}' 的发音时出错: {e}")
        return False

def main():
    print("欢迎使用有道词典发音下载工具")
    print("请输入要下载发音的单词，多个单词用逗号分隔")
    
    input_words = input("单词: ")
    words = [word.strip() for word in input_words.split(',') if word.strip()]
    
    if not words:
        print("未输入有效单词")
        return
    
    output_dir = input("请输入保存目录 (默认为 'pronunciations'): ").strip()
    if not output_dir:
        output_dir = "pronunciations"
    
    # 选择发音类型
    print("\n请选择发音类型:")
    print("1. 美式发音")
    print("2. 英式发音")
    pronunciation_type = input("请输入选项 (默认为美式发音): ").strip()
    
    success_count = 0
    for word in words:
        print(f"\n正在处理单词: {word}")
        url = get_pronunciation_url(word)
        
        # 根据用户选择修改URL中的type参数
        if pronunciation_type == "2" and "type=" in url:
            url = url.replace("type=2", "type=1")
        
        if url:
            if download_pronunciation(word, url, output_dir):
                success_count += 1
            # 添加延迟以避免被封IP
            time.sleep(1)
    
    print(f"\n下载完成! 成功下载 {success_count}/{len(words)} 个单词的发音")

if __name__ == "__main__":
    main()
