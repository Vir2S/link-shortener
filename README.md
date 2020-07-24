# link-shortener
Python Django Link Shortener REST API

Easy to create short link from any url.

# Endpoints:
    - url shortener:
        /api/shortener/(?P<origin_uri>.+)$
        method POST
        payload_to_create={'url': url, 'short_url': short_url}
        response serialized data

    - export urls list to csv-file:
        /api/export/
        method GET

    - url hash:
        /api/(?P<hash>.+)$
        method GET
        response hash redirect
        
    - urls list:
        /api/
        method GET
        response serialized data
