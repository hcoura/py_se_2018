from http.server import SimpleHTTPRequestHandler, test

m = SimpleHTTPRequestHandler.extensions_map
m[''] = 'text/plain'
m.update({k: v + ';charset=UTF-8' for k, v in m.items()})

test(SimpleHTTPRequestHandler, port=8000)
