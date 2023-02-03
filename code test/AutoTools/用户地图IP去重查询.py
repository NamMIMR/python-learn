import pandas as pd
from pathlib import WindowsPath
import logging
from playwright.sync_api import sync_playwright, jPlaywright


def get_filelist(filepath: str) -> list[WindowsPath]:
    '''
    获取给定目录下所有xlsx文件路径
    '''

    filelist = list(WindowsPath(filepath).glob('*.xlsx'))
    logging.info('给定目录xlsx文件: %s', filelist)
    return filelist

def get_ipaddress(filepath: WindowsPath) -> tuple[list[str], int]:
    '''
    获取去重后IP地址数据
    '''

    df = pd.read_excel(filepath, sheet_name=1)
    origin_count = df.shape[0]
    logging.info('原始数据样本量: %s', origin_count)
    df.drop_duplicates(subset=['ip_address'], keep='first', inplace=True)
    after_count = df.shape[0]
    logging.info('IP去重后样本量: %s', after_count)
    logging.info('去除IP重复样本: %d', origin_count - after_count)
    ip_list = df['ip_address'].tolist()
    return ip_list, after_count

def get_ipinfo(ip_list: list[str]) -> dict[str, list]:


    pass

def main():
    logging.basicConfig(level=logging.DEBUG)
    filepath = r'E:\Desktop\temp\230201'
    filelist = get_filelist(filepath)

    ip_list, ip_count = get_ipaddress(filelist[0])
    logging.debug('IP列表长度: %d', len(ip_list))
    logging.debug('IP列表前10项: %s', ip_list[:10])
    # for file in filelist:
    #     ip_list = get_ipaddress(file)


if __name__ == '__main__':
    main()
