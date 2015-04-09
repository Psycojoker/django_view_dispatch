Usage
=====

```python
from django.conf.urls import patterns, url
from django_view_dispatch import dispatch, dispatch_strict

from . import views


urlpatterns = patterns('',
    url(r'^some_url/$', dispatch(get=views.my_view, post=views.my_view_for_post), name='events_json'),

    # you can get any keyword argument you want to specify any http verb
    url(r'^some_url/$', dispatch(get=views.my_view, put=views.create, foo=views.another_view, bar=views.baz), name='events_json'),

    # by default, if a request has an HTTP verb that hasn't been specified in
    # the dispatch() function, it will be redirected to the GET view if present
    url(r'^some_url/$', dispatch(get=views.will_get_everything_thats_not_put, put=views.stuff), name='events_json'),

    # you can change this behavior this way
    url(r'^some_url/$', dispatch(get=views.stuff, put=views.will_get_everything_thats_not_get, default="put"), name='events_json'),

    # if "default" is set to None, this behavior is disabled and and
    # HttpResponseNotAllowed will be returned
    url(r'^input/$', dispatch(post=views.my_view_for_post, default=None), name='events_json'),  # behave like @require_POST

    # a more explicit way to do that is provided with "dispatch_strict" which behave exactly like dispatch with default set to None
    url(r'^input/$', dispatch_strict(post=views.my_view_for_post), name='events_json'),
)
```
