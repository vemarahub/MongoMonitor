def oplogstats(connection):
    c = connection
    localdb = c["local"]

    if "oplog.rs" in localdb.collection_names():
        collstats = dict()
        collstats.clear()
        collstats = localdb.command("collstats", "oplog.rs")

        return collstats
    else:
        return None


def logsizemb(connection):
    c = connection
    localdb = c["local"]

    if "oplog.rs" in localdb.collection_names():
        collstats = dict()
        collstats.clear()
        collstats = localdb.command("collstats", "oplog.rs")

        logsizemb = round((collstats["maxSize"] / (1024 * 1024)), 2)

        return logsizemb
    else:
        return None


def usedmb(connection):
    c = connection
    localdb = c["local"]

    if "oplog.rs" in localdb.collection_names():
        collstats = dict()
        collstats.clear()
        collstats = localdb.command("collstats", "oplog.rs")

        usedmb = round(((collstats["size"] / (1024 * 1024)) * 100) / 100, 2)

        return usedmb
    else:
        return None


def tfirst(connection):
    c = connection
    localdb = c["local"]

    if "oplog.rs" in localdb.collection_names():
        oplogcol = localdb["oplog.rs"]
        firstdoc = oplogcol.find_one(sort=[("$natural", 1)])

        return firstdoc["ts"].as_datetime()
    else:
        return None


def tlast(connection):
    c = connection
    localdb = c["local"]
    if "oplog.rs" in localdb.collection_names():
        oplogcol = localdb["oplog.rs"]
        lastdoc = oplogcol.find_one(sort=[("$natural", -1)])

        return lastdoc["ts"].as_datetime()
    else:
        return None


def timediff(connection):
    oplogcol = connection.local.oplog.rs
    tsfirst = oplogcol.find_one(sort=[("$natural", 1)])["ts"]
    tslast = oplogcol.find_one(sort=[("$natural", -1)])["ts"]
    timediff = tslast.time - tsfirst.time

    if isinstance(timediff, int):
        return timediff
    else:
        return None


def timediffhours(connection):
    timediffhours = round(((timediff(connection) / 36) / 100), 2)

    if isinstance(timediffhours, float):
        return timediffhours
    else:
        return None