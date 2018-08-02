# -*- coding:utf-8 -*-
#  Author:aling

import select
from selectors_ftp_server.conf import settings


class Interactive_Service(object):

    def __init__(self,user_info):
        self.user_info = user_info
        print(user_info)
        self.star_main(user_info)

    def star_main(self,user_info):
        print(self)
        print(user_info)
        ftp_server_menu = {
            'get_file': self.get_file,
            'show_files': self.show_files,
            'put_file': self.put_files,
            'cd_files': self.cd_files,
            'editor_info':self.editor_info,
            'exits': self.exits
        }
        return settings.FTP_MAIN_MENU_INFO
        # inputs = ''
        # outputs = ''
        #
        # readable, writeable, exceptional = select.select(inputs, outputs, inputs)

    def get_file(self):
        pass

    def show_files(self):
        pass

    def put_files(self):
        pass

    def cd_files(self):
        pass

    def exits(self):
        exit('欢迎再次使用select版ftp,下次再见')

    def editor_info(self):
        pass