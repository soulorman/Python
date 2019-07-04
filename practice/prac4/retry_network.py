def retry(count=1):
    def dec(f):
        def ff(*args, **kwargs):
            ex = None
            for i in range(count):
                try:
                    ans = f(*args, **kwargs)
                    return ans
                except Exception as e:
                    ex = e
            raise ex

        return ff

    return dec


db = []


@retry(count=10)
def until_six():
    db.append("haha")
    print("until_six")
    return db[6]


print(until_six())
