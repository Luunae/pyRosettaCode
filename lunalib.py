def intcheck(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def getint(say: str, range_start=None, range_end=None, set=None):
    while True:
        user_data = input(say)
        if intcheck(user_data):
            user_data = int(user_data)
            if range_start is not None and range_end is not None:
                if range_start <= user_data <= range_end:
                    return user_data
            elif range_start is not None:
                if range_start <= user_data:
                    return user_data
            elif range_end is not None:
                if user_data <= range_end:
                    return user_data
            elif set is not None:
                if user_data in set:
                    return user_data
            else:
                raise Exception("intcheck fucked up")


def getstr(say: str, min_length=None, max_length=None, compare=None):
    while True:
        user_data = input(say)
        if min_length is not None and max_length is not None:
            if min_length <= len(user_data) <= max_length:
                return user_data
        if min_length is not None:
            if min_length <= len(user_data):
                return user_data
        if max_length is not None:
            if len(user_data) <= max_length:
                return user_data
        if compare is not None:
            if user_data == compare:
                return user_data
    pass
