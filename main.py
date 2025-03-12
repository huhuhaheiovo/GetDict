import requests
import os
import time
import hashlib
import random
import string

def generate_random_string(length=7):
    """Generate a random string for yduuid"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def get_mystic_time():
    """Get current timestamp"""
    return str(int(time.time() * 1000))

def generate_sign(word, mystic_time, yduuid):
    """Generate sign parameter
    
    This is a simplified implementation. The actual algorithm may be more complex.
    """
    key = "webdict"
    data = f"client=web&keyfrom=dick&keyid=voiceDictWeb&mid=1&mysticTime={mystic_time}&product=webdict&type=1&vendor=web&word={word}&yduuid={yduuid}&key={key}"
    return hashlib.md5(data.encode()).hexdigest()

def get_pronunciation_url(word):
    """
    Generate pronunciation URL for a word
    """
    try:
        # Generate necessary parameters
        yduuid = generate_random_string()
        mystic_time = get_mystic_time()
        
        # Parameters for the request
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
        
        # Use American pronunciation by default
        url = f"https://dict.youdao.com/dictvoice?audio={word}&type=2"
        
        # For more complex URL format, uncomment the code below
        # sign = generate_sign(word, mystic_time, yduuid)
        # params["sign"] = sign
        # point_param = "appVersion,client,imei,keyfrom,keyid,mid,model,mysticTime,network,product,rate,screen,type,vendor,word,yduuid,key"
        # params["pointParam"] = point_param
        # url = "https://dict.youdao.com/pronounce/base?" + "&".join([f"{k}={v}" for k, v in params.items()])
        
        return url
    
    except Exception as e:
        print(f"Error generating URL for '{word}': {e}")
        return None

def download_pronunciation(word, url, output_dir="pronunciations"):
    """
    Download pronunciation MP3 file
    """
    if not url:
        return False
    
    # Create output directory if it doesn't exist
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
        
        print(f"Downloaded '{word}' pronunciation to {output_path}")
        return True
    
    except Exception as e:
        print(f"Error downloading '{word}' pronunciation: {e}")
        return False

def main():
    print("Welcome to Word Pronunciation Downloader")
    print("Please enter words to download, separated by commas")
    
    input_words = input("Words: ")
    words = [word.strip() for word in input_words.split(',') if word.strip()]
    
    if not words:
        print("No valid words entered")
        return
    
    output_dir = input("Enter save directory (default is 'pronunciations'): ").strip()
    if not output_dir:
        output_dir = "pronunciations"
    
    # Select pronunciation type
    print("\nSelect pronunciation type:")
    print("1. American")
    print("2. British")
    pronunciation_type = input("Enter option (default is American): ").strip()
    
    success_count = 0
    for word in words:
        print(f"\nProcessing word: {word}")
        url = get_pronunciation_url(word)
        
        # Modify URL based on user selection
        if pronunciation_type == "2" and "type=" in url:
            url = url.replace("type=2", "type=1")
        
        if url:
            if download_pronunciation(word, url, output_dir):
                success_count += 1
            # Add delay to avoid IP blocking
            time.sleep(1)
    
    print(f"\nDownload complete! Successfully downloaded {success_count}/{len(words)} word pronunciations")

if __name__ == "__main__":
    main()
