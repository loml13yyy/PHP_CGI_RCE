# PHP_CGI_RCE
批量检测PHPCGI平台远程代码执行漏洞工具
![图片](https://github.com/user-attachments/assets/4b8c9bc5-c199-4cd5-b813-e8cd5ee255a5)

```shell
漏洞描述：
该漏洞可在受影响的环境下执行任意PHP代码，从而获取操作系统权限。最严重的情况下，这可能导致服务器的完全接管，敏感数据泄露，甚至将服务器转化为发起其他攻击的跳板。

影响版本：
PHP 8.3 < 8.3.8
PHP 8.2 < 8.2.20
PHP 8.1 < 8.1.29

fofa搜索语句：
header="Xampps_info" || body="/xampps.jpg" || (header="location http" && header="xampp") || body="content="Kai Oswald Seidler" || title="XAMPP for" || title="XAMPP Version" || body="font-size: 1.2em; color: red;">New XAMPP"

工具使用：
  -h, --help                        获取帮助信息
  -f FILENAME, --filename FILENAME  批量检验URL，输入URL文件名
  -u URL, --url URL                 检测单个URL
```
