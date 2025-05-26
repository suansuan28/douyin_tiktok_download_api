#!/bin/bash

# Set script to exit on any errors.
set -e

echo 'Updating package lists... | 正在更新软件包列表...'
sudo apt-get update

echo 'Installing Git... | 正在安装Git...'
sudo apt-get install -y git

echo 'Installing Python3... | 正在安装Python3...'
sudo apt install -y python3

echo 'Installing PIP3... | 正在安装PIP3...'
sudo apt install -y python3-pip

echo 'Installing python3-venv... | 正在安装python3-venv...'
sudo apt install -y python3-venv

echo 'Creating path: /www/wwwroot | 正在创建路径: /www/wwwroot'
sudo mkdir -p /www/wwwroot

cd /www/wwwroot || { echo "Failed to change directory to /www/wwwroot | 无法切换到目录 /www/wwwroot"; exit 1; }

echo 'Cloning douyin_tiktok_download_api from Github! | 正在从Github克隆你的项目!'
sudo git clone https://github.com/suansuan28/douyin_tiktok_download_api.git

cd douyin_tiktok_download_api/ || { echo "Failed to change directory | 无法切换到项目目录"; exit 1; }

echo 'Creating a virtual environment | 正在创建虚拟环境'
python3 -m venv venv

echo 'Activating the virtual environment | 正在激活虚拟环境'
source venv/bin/activate

echo 'Setting pip to use the default PyPI index | 设置pip使用默认PyPI索引'
pip config set global.index-url https://pypi.org/simple/

echo 'Installing pip setuptools | 安装pip setuptools'
pip install setuptools

echo 'Installing dependencies from requirements.txt | 从requirements.txt安装依赖'
pip install -r requirements.txt

echo 'Deactivating the virtual environment | 正在停用虚拟环境'
deactivate

echo 'Adding project to system service | 添加项目为系统服务'
sudo cp daemon/* /etc/systemd/system/

echo 'Enabling project service | 启用项目服务'
sudo systemctl enable Douyin_TikTok_Download_API.service

echo 'Starting project service | 启动项目服务'
sudo systemctl start Douyin_TikTok_Download_API.service

echo '✅ 部署完成！你现在可以通过 http://localhost 访问你的服务了！'
echo '📍 修改配置看 /www/wwwroot/douyin_tiktok_download_api/config.yaml'
