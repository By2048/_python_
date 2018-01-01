from configparser import ConfigParser

cfg = ConfigParser()

# 读取配置文件
cfg.read('config.ini')

print(cfg.sections())
# ['installation', 'debug', 'server']

print(cfg.get('installation', 'library'))
# /usr/local/lib


print(cfg.get('installation', 'library_no',fallback='no exit'))
# no exit

print(cfg.getboolean('debug', 'log_errors'))
# True

print(cfg['debug'].getboolean('log_errors'))
# True

print(cfg.getint('server', 'port'))
# 8080

print(cfg.get('server', 'signature'))
# =================================
# Brought to you by the Python Cookbook
# =================================

print('debug' in cfg)
# True

print(cfg['server']['port'])
# 8080

for key in cfg['debug']:
    print(key,end='   ')
    print(cfg['debug'][key])
# log_errors   true
# show_warnings   False





# 写入配置

config = ConfigParser()
# config.add_section('Section1')
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('config-1.ini', 'w') as configfile:
    config.write(configfile)



# print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"
# print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"

"""
; config.ini
; Sample configuration file

[installation]
library=%(prefix)s/lib
include=%(prefix)s/include
bin=%(prefix)s/bin
prefix=/usr/local

# Setting related to debug configuration
[debug]
log_errors=true
show_warnings=False

[server]
port: 8080
nworkers: 32
pid-file=/tmp/spam.pid
root=/www/root
signature:
    =================================
    Brought to you by the Python Cookbook
    =================================
"""
