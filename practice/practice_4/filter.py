def make_filter(rules):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [ i for i in lines if rules in i]
        return filter_doc
    return the_filter

file = make_filter('abc')
print(file('/tmp/a'))
