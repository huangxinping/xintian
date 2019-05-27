from sanic import Blueprint
from sanic.response import json

v1_bp = Blueprint('v1_api', url_prefix='api/v1')


@v1_bp.route('/')
async def root(request):
    return json({'msg': 'haha'})
