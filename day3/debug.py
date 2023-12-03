_DEBUG = True


def debug(*args, indent=0, **kwargs):
    if not _DEBUG:
        return

    prefix = "### Debug:" + "    " * indent
    print(prefix, *args, **kwargs)
