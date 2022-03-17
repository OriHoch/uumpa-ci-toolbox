import json
from textwrap import dedent
from http.server import ThreadingHTTPServer
from http.server import BaseHTTPRequestHandler

from ruamel import yaml


class WebmonHTTPRequestHandler(BaseHTTPRequestHandler):

    def version_string(self):
        return 'uci webmon'

    def do_GET(self):
        status, data = self.server.webmon()
        if status is True:
            status_code = 200
        elif status is False:
            status_code = 500
        else:
            status_code = status
        self.send_response(status_code)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


class WebmonHTTPServer(ThreadingHTTPServer):

    def __init__(self, port, webmon):
        print("Starting webmon on port {}".format(port))
        self.webmon = webmon
        super(WebmonHTTPServer, self).__init__(('0.0.0.0', port), WebmonHTTPRequestHandler)


def start(port, python_code):
    exec(dedent(python_code))
    WebmonHTTPServer(int(port), eval('webmon')).serve_forever()


class WebmonMultiHTTPRequestHandler(BaseHTTPRequestHandler):

    def version_string(self):
        return 'uci webmon'

    def do_GET(self):
        webmon = self.server.webmon_paths.get(self.path)
        if webmon:
            status, data = webmon()
        else:
            status, data = False, {'error': 'invalid path: {}'.format(self.path)}
        if status is True:
            status_code = 200
        elif status is False:
            status_code = 500
        else:
            status_code = status
        self.send_response(status_code)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


class WebmonMultiHTTPServer(ThreadingHTTPServer):

    def __init__(self, port, webmon_paths):
        print("Starting webmon_multi on port {} paths: {}".format(port, list(webmon_paths.keys())))
        self.webmon_paths = webmon_paths
        super(WebmonMultiHTTPServer, self).__init__(('0.0.0.0', port), WebmonMultiHTTPRequestHandler)


def get_webmon_from_config(webmon_config):
    if 'python_code' in webmon_config:
        exec(dedent(webmon_config['python_code']))
        return eval('webmon')
    else:
        with open(webmon_config['python_file']) as f:
            exec(dedent(f.read()))
            return eval('webmon')


def start_multi(port, config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    webmon_paths = {}
    for webmon_config in config['webmons']:
        webmon_paths[webmon_config['path']] = get_webmon_from_config(webmon_config)
    WebmonMultiHTTPServer(int(port), webmon_paths).serve_forever()
