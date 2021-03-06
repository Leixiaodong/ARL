from flask_restplus import Resource, Api, reqparse, fields, Namespace
from app.utils import get_logger, auth
from . import base_query_fields, ARLResource, get_arl_parser

ns = Namespace('domain')

logger = get_logger()

base_search_fields = {
    'domain': fields.String(required=False, description="域名"),
    'record': fields.String(description="解析值"),
    'type': fields.String(description="解析类型"),
    'ips': fields.String(description="IP"),
    'source': fields.String(description="是否开启"),
    "task_id": fields.String(description="任务ID")
}

base_search_fields.update(base_query_fields)


@ns.route('/')
class ARLDomain(ARLResource):
    parser = get_arl_parser(base_search_fields, location='args')

    @auth
    @ns.expect(parser)
    def get(self):
        """
        域名信息查询
        """
        args = self.parser.parse_args()
        data = self.build_data(args=args, collection='domain')

        return data
