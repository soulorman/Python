import yaml
with open('config.yaml') as f:
    y = yaml.load_all(f)
    for i in y:
        print(i)
