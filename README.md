Usage
=====

```python
from django.conf.urls import patterns, url
from django_view_dispatch import dispatch

from . import views


urlpatterns = patterns('',
    url(r'^some_url/$', dispatch(get=views.my_view, post=views.my_view_for_post), name='events_json'),
)
```
