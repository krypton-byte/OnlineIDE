# Author : Krypton Byte
import time
import colorama
import os
import sys
import re
import threading
from loader import loading, help
# import requests
def args(params, default):
    for i in sys.argv:
        for cordinate in re.finditer(params, i):
            print(i[cordinate.span()[1]:])
            return i[cordinate.span()[1]:]
    else:
        return default
for i in sys.argv:
    if i == "--help":
        print(help)
        sys.exit(1)
workspace = args("--workspace=","/data/data/com.termux/files/home")
port = args("--port=",7890)
path = os.path.dirname(__file__)
"""def ttyd_download():
    arch=os.popen("busybox arch").read().strip()
    newer = re.findall("\<a href\=\"/tsl0922/ttyd/releases/tag/(.*?)\"\>",requests.get("https://github.com/tsl0922/ttyd/releases/").text)
    newer.sort()
    open("bin/ttyd", "wb").write(requests.get(f"https://github.com/tsl0922/ttyd/releases/download/{newer[-1]}/ttyd.{arch}").content)
    os.system("chmod +x bin/ttyd")"""
require = ["ttyd", "php", "nginx", "busybox", "libwebsockets", "cmake", "make", "build-essential", "tmux"]
print(f"""
{colorama.Fore.LIGHTYELLOW_EX}   ___        _ _             {colorama.Fore.GREEN} ___ ____  _____ 
{colorama.Fore.LIGHTYELLOW_EX}  / _ \ _ __ | (_)_ __   ___  {colorama.Fore.GREEN}|_ _|  _ \| ____|
{colorama.Fore.LIGHTYELLOW_EX} | | | | '_ \| | | '_ \ / _ \ {colorama.Fore.GREEN} | || | | |  _|  
{colorama.Fore.LIGHTYELLOW_EX} | |_| | | | | | | | | |  __/ {colorama.Fore.GREEN} | || |_| | |___ 
{colorama.Fore.LIGHTYELLOW_EX}  \___/|_| |_|_|_|_| |_|\___| {colorama.Fore.GREEN}|___|____/|_____|
                              {colorama.Fore.LIGHTCYAN_EX}_________________{colorama.Fore.RESET}
""")
installed = lambda:[i[0] for i in [x.split("/") for x in os.popen("pkg list-installed").read().splitlines()]][1:]
while True:
    for i in require:
        if i in installed():
            pass
        else:
            spin=loading(f"{colorama.Fore.LIGHTCYAN_EX} Installing {colorama.Fore.LIGHTMAGENTA_EX}{i} {colorama.Fore.LIGHTBLUE_EX}", True)
            spin.running()
            os.system(f"apt install {i} -y > /dev/null")
            spin.run = False
        print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTYELLOW_EX}{i}{colorama.Fore.LIGHTGREEN_EX} Installed{colorama.Fore.RESET}            ")
    else:
        break
if not "BLACKICEcoder" in os.listdir("."):
    spin=loading(f"{colorama.Fore.LIGHTCYAN_EX} Cloning {colorama.Fore.LIGHTMAGENTA_EX} BLACKICEcoder {colorama.Fore.LIGHTBLUE_EX}", True)
    spin.running()
    os.system("git clone https://github.com/krypton-byte/BLACKICEcoder >/dev/null")
    spin.run = False
    time.sleep(0.4)
    print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTYELLOW_EX}Cloning Ttyd{colorama.Fore.RESET}               ")
if not "ttyd" in os.listdir("."):
    spin=loading(f"{colorama.Fore.LIGHTCYAN_EX} Cloning {colorama.Fore.LIGHTMAGENTA_EX} Ttyd           {colorama.Fore.LIGHTBLUE_EX}", True)
    spin.running()
    os.system("git clone https://github.com/tsl0922/ttyd >/dev/null")
    spin.run = False
    time.sleep(0.4)
    print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTYELLOW_EX}Cloning Ttyd{colorama.Fore.RESET}               ")
if not "build" in os.listdir("ttyd"):
    spin=loading(f"{colorama.Fore.LIGHTCYAN_EX} Compiling {colorama.Fore.LIGHTMAGENTA_EX}Ttyd {colorama.Fore.LIGHTBLUE_EX}", True)
    spin.running()
    cmd = """cd ttyd && mkdir build && cd build&&cmake .. >/dev/null&& make >/dev/null&& sudo make install>/dev/null"""
    os.system(cmd)
    print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTCYAN_EX}Compile{colorama.Fore.LIGHTMAGENTA_EX} Compile Ttyd{colorama.Fore.RESET}")
    spin.run = False

open('BLACKICEcoder/lib/config___settings.php','w').write(f'<?php\n// ICEcoder system settings\n$ICEcoderSettings = array(\n\t"versionNo"\t\t=> "1.0",\n\t"codeMirrorDir"\t\t=> "CodeMirror",\n\t"docRoot"\t\t=> "{workspace}",\t// $_SERVER[\'DOCUMENT_ROOT\'] Set absolute path of another location if needed\n\t"demoMode"\t\t=> false,\n\t"devMode"\t\t=> true,\n\t"fileDirResOutput"\t=> "none",\t\t\t// Can be none, raw, object, both (all but \'none\' output to console)\n\t"loginRequired"\t\t=> true,\n\t"multiUser"\t\t=> false,\n\t"languageBase"\t\t=> "english.php",\n\t"lineEnding"\t\t=> "\\n",\n\t"newDirPerms"\t\t=> 755,\n\t"newFilePerms"\t\t=> 644,\n\t"enableRegistration"\t=> true\n);\n?>\n')
print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTGREEN_EX}Online IDE {colorama.Fore.LIGHTCYAN_EX}Running {colorama.Fore.LIGHTRED_EX}on: {colorama.Fore.LIGHTYELLOW_EX}http://0.0.0.0:{port}")
print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTGREEN_EX}PATH {colorama.Fore.LIGHTCYAN_EX}Workspace {colorama.Fore.LIGHTRED_EX}: {colorama.Fore.LIGHTYELLOW_EX}{workspace}")
open("/data/data/com.termux/files/usr/etc/nginx/nginx.conf", "w").write("""

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       %s;
        server_name  localhost;
        #charset koi8-r;

        #access_log  logs/host.access.log  main;
        location /terminal/ws {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass http://0.0.0.0:8001/ws;
        }

        location /terminal {
            proxy_pass http://0.0.0.0:8001/;
        }

        location / {
            proxy_pass http://0.0.0.0:8000/;
        }
        
	#location /token {
	#    proxy_pass http://192.168.43.48:8000/token;
        #    proxy_set_header Host $host;
        #    proxy_set_header X-Real-IP $remote_addr;
        #    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #}
        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /data/data/com.termux/files/usr/share/nginx/html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

"""%(port))
print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTCYAN_EX}Starting{colorama.Fore.LIGHTYELLOW_EX} Editor{colorama.Fore.RESET}")
threading.Thread(target=os.system, args=(f"php -S 0.0.0.0:8000 -t {path}/BLACKICEcoder > /dev/null",)).start()
print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTCYAN_EX}Starting{colorama.Fore.LIGHTYELLOW_EX} NGINX{colorama.Fore.RESET}")
os.system("nginx")
print(f"{colorama.Fore.LIGHTRED_EX}[{colorama.Fore.GREEN}{chr(10003)}{colorama.Fore.LIGHTRED_EX}] {colorama.Fore.LIGHTCYAN_EX}Starting{colorama.Fore.LIGHTYELLOW_EX} Ttyd{colorama.Fore.RESET}")
os.system(f"cd {workspace}&& {path}/ttyd/build/ttyd -p 8001 bash>/dev/null")