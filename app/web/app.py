# PyWebIO组件/PyWebIO components
import os

import yaml
from pywebio import session, config as pywebio_config
from pywebio.input import *
from pywebio.output import *

from app.web.views.About import about_pop_window
from app.web.views.Document import api_document_pop_window
from app.web.views.Downloader import downloader_pop_window
from app.web.views.EasterEgg import a
from app.web.views.ParseVideo import parse_video
from app.web.views.Shortcuts import ios_pop_window
# PyWebIO的各个视图/Views of PyWebIO
from app.web.views.ViewsUtils import ViewsUtils

# 读取上级再上级目录的配置文件
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    _config = yaml.safe_load(file)

pywebio_config(theme=_config['Web']['PyWebIO_Theme'],
               title=_config['Web']['Tab_Title'],
               description=_config['Web']['Description'],
               js_file=[
                   # 整一个看板娘，二次元浓度++
                   _config['Web']['Live2D_JS'] if _config['Web']['Live2D_Enable'] else None,
               ])


class MainView:
    def __init__(self):
        self.utils = ViewsUtils()

    # 主界面/Main view
    def main_view(self):
        # 左側導航欄/Left navbar
        with use_scope('main'):
            # 設置favicon/Set favicon
            favicon_url = _config['Web']['Favicon']
            session.run_js(f"""
                            $('head').append('<link rel="icon" type="image/png" href="{favicon_url}">')
                            """)
            # 移除footer/Remove footer
            session.run_js("""$('footer').remove()""")
            # 設置不允許referrer/Set no referrer
            session.run_js("""$('head').append('<meta name=referrer content=no-referrer>');""")
            # 設置標題/Set title
            main_title = "短視頻無水印解析工具"
            subtitle = "V20B在線工具提供抖音、快手、小紅書、西瓜視頻、皮皮蝦、B站、AcFun、今日頭條、虎牙、微視、好看視頻、綠洲等多平台的無水印視頻解析與下載服務。免費無廣告，快速便捷，支持多平台解析，簡單易用。"
            put_html(f'''
                <div style="background: linear-gradient(90deg, #36d1c4 0%, #5b86e5 100%); padding: 40px 0 20px 0; color: #fff; text-align: center;">
                    <h1 style="font-size:2.5em; font-weight:bold; margin-bottom:10px;">{main_title}</h1>
                    <div style="font-size:1.1em; max-width:700px; margin:0 auto;">{subtitle}</div>
                </div>
            ''')
            put_html('<div style="height:40px;"></div>')
            # 平台分類卡片
            platforms = [
                {"name": "抖音無水印解析", "icon": "<span style='font-size:2.5em;'>🎵</span>", "desc": "支持抖音視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "快手無水印解析", "icon": "<span style='font-size:2.5em;'>📢</span>", "desc": "支持快手視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "小紅書無水印解析", "icon": "<span style='font-size:2.5em;'>📕</span>", "desc": "支持小紅書視頻圖片無水印解析與下載", "action": lambda: parse_video()},
                {"name": "西瓜視頻無水印解析", "icon": "<span style='font-size:2.5em;'>🍉</span>", "desc": "支持西瓜視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "皮皮蝦無水印解析", "icon": "<span style='font-size:2.5em;'>🦐</span>", "desc": "支持皮皮蝦視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "Bilibili（B站）無水印解析", "icon": "<span style='font-size:2.5em;'>📺</span>", "desc": "支持B站視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "AcFun（A站）無水印解析", "icon": "<span style='font-size:2.5em;'>🎬</span>", "desc": "支持AcFun視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "今日頭條無水印解析", "icon": "<span style='font-size:2.5em;'>📰</span>", "desc": "支持今日頭條視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "虎牙視頻無水印解析", "icon": "<span style='font-size:2.5em;'>🐯</span>", "desc": "支持虎牙視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "微視無水印解析", "icon": "<span style='font-size:2.5em;'>🎤</span>", "desc": "支持微視視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "好看視頻無水印解析", "icon": "<span style='font-size:2.5em;'>▶️</span>", "desc": "支持好看視頻無水印解析與下載", "action": lambda: parse_video()},
                {"name": "綠洲無水印解析", "icon": "<span style='font-size:2.5em;'>🌿</span>", "desc": "支持綠洲視頻無水印解析與下載", "action": lambda: parse_video()},
            ]
            # 三欄展示
            rows = []
            for i in range(0, len(platforms), 3):
                row = []
                for j in range(3):
                    if i + j < len(platforms):
                        p = platforms[i + j]
                        row.append(
                            put_button(f"{p['icon']}<br><b>{p['name']}</b><br><span style='font-size:0.95em;color:#888'>{p['desc']}</span>",
                                       onclick=p['action'],
                                       color='light',
                                       outline=True,
                                       shape='square',
                                       size='large',
                                       )
                        )
                rows.append(row)
            put_table(rows, header=None)
            put_html('<div style="height:40px;"></div>')
