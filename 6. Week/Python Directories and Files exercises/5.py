brands=['nike','adidas','puma','asics']
def k(brands):
    with open('brands.txt','w') as fb:
        for br in brands:
            fb.write(f'{br}\n')
    f = open("brands.txt", "r")
    print(f.read())
k(brands)