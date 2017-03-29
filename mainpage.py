import asyncio
from aiohttp import web
import staticfile as static
import aiohttp_jinja2

@aiohttp_jinja2.template('index.jinja2')
async def showMainPage(request):
    data={}
    data['title']='信息中心'
    data['main']=static.assets
    return data
    pass

@aiohttp_jinja2.template('productBuyer.jinja2')
async def showBuyerPage(request):
    data={}
    data['title']='买方信息'
    data['main']=static.assets
    return data
    pass

@aiohttp_jinja2.template('productBuyer.jinja2')
async def showSellerPage(request):
    data={}
    data['title']='卖方信息'
    data['main']=static.assets
    return data
    pass

@aiohttp_jinja2.template('productBuyer.jinja2')
async def showMatchList(request):
    data={}
    data['title']='匹配列表'
    data['main']=static.assets
    return data
    pass

async def middleware_factory(app, handler):
    async def middleware_handler(req):
        # if req.path == '/' or req.path.startswith('/static/')\
        #         or req.cookies.get('uid') == users['psw']:
        # if req.path.startswith('/private/') and \
        # req.cookies.get('Authentication') != cookies['Authentication']:
        #     #print(req.cookies.get('uid'))
        #     return web.HTTPFound('/')

        # else:
        #     # print(req.path)
        #     return await handler(req)
        #     pass
        return await handler(req)
        pass

    return middleware_handler
