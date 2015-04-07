def dispatch(**verbs):
    default = verbs.get("default", "GET")

    return lambda x: verbs.get(default, verbs[default.lower()])(x)
