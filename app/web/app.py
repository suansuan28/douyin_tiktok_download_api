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
        # 左侧导航栏/Left navbar
        with use_scope('main'):
            # 设置favicon/Set favicon
            favicon_url = _config['Web']['Favicon']
            session.run_js(f"""
                            $('head').append('<link rel="icon" type="image/png" href="{favicon_url}">')
                            """)
            # 修改footer/Remove footer
            session.run_js("""$('footer').remove()""")
            # 设置不允许referrer/Set no referrer
            session.run_js("""$('head').append('<meta name=referrer content=no-referrer>');""")
            # 设置标题/Set title
            title = self.utils.t("TikTok/抖音无水印在线解析下载",
                                 "Douyin/TikTok online parsing and download without watermark")
            put_html(f"""
                    <div align="center">
                    <a href="/" alt="logo" ><img src="{favicon_url}" width="100"/></a>
                    <h1 align="center">{title}</h1>
                    </div>
                    """)
            # 直接显示批量解析视频的输入区域
            parse_video()
