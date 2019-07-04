import logging


def deprecated(info):
    def decorator(f):
        def ff(*args, **kwargs):
            logging.warning("%s is deprected. %s" % (f.__name__, info))
            res = f(*args, **kwargs)
            return res

        return ff

    return decorator
