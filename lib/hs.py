import hashlib


def s1(args):
    args.sort()
    sha1 = hashlib.sha1()
    for i in args:
        sha1.update(i.encode("utf8"))
    return sha1.hexdigest()