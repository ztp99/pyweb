
CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/path/to/my/app',
    'python': '/usr/bin/python',
    'args': (
        '--bind=127.0.0.1:8080',
        '--workers=16',
        '--timeout=60',
        'app.module',
    ),
}

def application(env, start_response):
    url = []
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = (env['QUERY_STRING'])
    url += "&z=0" #z=0 just for test when no url query
    url = url.split('&')
    print 'app:', url
    datastr=str(url)
    print 'app:', datastr
    datastr=' '.join(map(str, url))
    print 'app:', datastr
    datastr='\n'.join(map(str, url)).replace("'", '').replace("[",'').replace("]",'')
    #url = '\r\n'.join([url]) 
    #url = '\r\n'.join([(env['QUERY_STRING'].split("&"))])
    return datastr
