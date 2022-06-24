import camelcase

c = camelcase.CamelCase()
txt = 'lorem ipsum dolor sit amet'
x = c.hump(txt) # Lorem Ipsum Dolor Sit Amet
print(x)
