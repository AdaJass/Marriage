import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
import staticfile as static
from aiomysql.sa import create_engine
from model import *
import mainpage

# async def middleware_factory(app, handler):
#     async def middleware_handler(request):        
#         return await handler(request)
#     return sss

# async def logout(request): 
#     data={}
#     data['title']='登录'
#     data['main']=static.assets
#     res = aiohttp_jinja2.render_template('login.jinja2',
#                                               request,
#                                               data)
#     res.set_cookie('Authentication','logout')
#     return res
    
@asyncio.coroutine
def Database(future):
    '''
    data is from the http response in main module.
    '''
    global engine
    engine = yield from create_engine(user='root',db='hot',port=3306,\
                                        host='127.0.0.1', password='11111',\
                                        echo=True, charset='utf8')
    future.set_result(engine)


@asyncio.coroutine
def CloseDB():
    engine.close()
    yield from engine.wait_closed()    
    pass
# web.run_app(app,port=9999)
async def init(loop):
    app = web.Application(middlewares=[mainpage.middleware_factory])
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader('./view'))

    app.router.add_route('GET', '/', mainpage.showMainPage)

    app.router.add_route('GET', '/productbuyer', mainpage.showBuyerPage)
    app.router.add_route('GET', '/productseller', mainpage.showSellerPage)
    app.router.add_route('GET', '/productmatchlist', mainpage.showMatchList)
    app.router.add_static('/static/', './bower_components')
    # app.router.add_static('/statics/', './node_modules')
    app.router.add_static('/','./public')
    srv = await loop.create_server(
        app.make_handler(), '0.0.0.0', 80)
    print('Sever starts at port: 80')
    return srv

if __name__ == '__main__':    
    loop = asyncio.get_event_loop()
    # future = asyncio.Future()
    # asyncio.ensure_future(Database(future))
    # loop.run_until_complete(future)
    # engine = future.result() 

    # hot.initialDatabase(engine)      
    
    loop.run_until_complete(init(loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass