# Sayobot

目的：学习机器人开发以及提高python编写能力
实现：基于gocqhttp的后端，以及python编写的功能实现的聊天机器人


### 文件结构  

```
sayobot/
└── Sayo/
    ├── bot.py         # bot.py 实例化bot
    ├── bot_config.py  # bot_config.py bot配置
    ├── services/      # services为插件提供支持和服务
    ├── sources/       # sources暂时存放数据
    └── bot_plugins/   # bot_plugins存放插件
        ├── ping.py  
        ├── jrrp.py  
        └── weather.py
```  


bot_plugins存放插件  

services为插件提供支持和服务  

sources暂时存放数据  

bot.py 实例化bot  

bot_config.py bot配置，包括监听端口等设置
