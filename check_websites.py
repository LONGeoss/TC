import requests
import time
import os
from datetime import datetime

# 目标网站列表
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.hanime1.me"
]

# 创建日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 生成日志文件
log_file = os.path.join(log_dir, "website_check.log")

# 记录日志
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(log_entry + "\n")

# 访问网站并记录状态
def check_websites():
    log_message("开始检查网站可用性...\n")

    for website in websites:
        try:
            start_time = time.time()
            response = requests.get(website, timeout=10)
            end_time = time.time()
            latency = round((end_time - start_time) * 1000, 2)

            if response.status_code == 200:
                log_message(f"[✔] {website} - 正常 (状态码: 200, 延迟: {latency} ms)")
            else:
                log_message(f"[✘] {website} - 访问异常 (状态码: {response.status_code})")

        except requests.exceptions.RequestException as e:
            log_message(f"[✘] {website} - 访问失败 ({e})")

    log_message("\n检查完成。\n" + "="*50 + "\n")

if __name__ == "__main__":
    check_websites()
