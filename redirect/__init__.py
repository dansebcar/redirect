from aiohttp import web

routes = web.RouteTableDef()
default = """\
<!DOCTYPE html>
<meta http-equiv="refresh" content="3">
<h1>Location not set, retrying...</h1>
"""


@routes.get("/")
async def get_location(request: web.Request):
    app = request.app
    try:
        loc = app["location"]
    except KeyError:
        return web.Response(text=default, content_type="text/html")
    else:
        raise web.HTTPTemporaryRedirect(loc)



@routes.post("/")
async def set_location(request: web.Request):
    app = request.app
    app["location"] = await request.text()
    raise web.HTTPNoContent


def run_app():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
