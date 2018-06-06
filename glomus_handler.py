# coding=utf-8
import re

class GlomusHanderException(Exception):
    pass

'''
バーチャルスライドファイルを取り扱うクラスの上位クラス。
各種の染色方式ごとのファイル名のパターンを一元管理する。
'''
class GlomusHandler(object):
    '''データカテゴリに応じて対象ファイル識別パターンを設定する'''
    def set_type(self, data_category):

        if data_category == 'OPT_PAM':
            self.TYPE = 'OPT_PAM'
            self.pattern = r'.*PAM.*\.ndpi'
        elif data_category == 'OPT_MT':
            self.TYPE = 'OPT_MT'
            self.pattern = r'.*MT.*\.ndpi'
        elif data_category == 'OPT_PAS':
            self.TYPE = 'OPT_PAS'
            self.pattern = r'.*PAS.*\.ndpi'
        elif data_category == 'OPT_HE':
            self.TYPE = 'OPT_HE'
            self.pattern = r'.*HE.*\.ndpi|.*\d+ - \d+.*\.ndpi|.*\d+-\d*\.ndpi'
        elif data_category == 'OPT_Azan':
            self.TYPE = 'OPT_Azan'
            self.pattern = r'.*Azan.*\.ndpi'
        else:
            raise GlomusHanderException('Unknown Augument is given.:' + data_category)

        self.repattern = re.compile(self.pattern, re.IGNORECASE)

def get_staining_type(staining_type):
    if staining_type == 'OPT_PAS':
        return '02_PAS'
    elif staining_type == 'OPT_PAM':
        return '03_PAM'
    elif staining_type == 'OPT_MT':
        return '05_MT'
    elif staining_type == 'OPT_Azan':
        return '06_Azan'
    else:
        return ''
