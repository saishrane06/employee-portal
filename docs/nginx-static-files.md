# Static Files with Nginx

Nginx serves static assets directly.

## Benefits

- Faster response times
- Reduced load on Gunicorn
- Browser caching support

## Static Directory

```
static/
├── css/
├── js/
└── images/
```

## Verify

Visit:

```
http://localhost/static/css/style.css
```