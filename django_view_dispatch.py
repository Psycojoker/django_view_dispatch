def dispatch(get, default="get", **verbs):
    return lambda x: get(x)
