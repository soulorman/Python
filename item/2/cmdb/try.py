def test():
    print('start')
    try: 
        1/1
        print("1/0")
        return True
    except BaseException as e:
        print(e)
        return True

    print('end')

test()