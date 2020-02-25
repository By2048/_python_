def _get_():
    logging.info(db.get('key1'))

    for key in db.keys('key*'):
        key = key.decode() if isinstance(key, bytes) else key
        value = db.get(key)
        logging.info(f"{key} -> {value}")


def _keys_():
    pass
