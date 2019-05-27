import weasyprint
pdf = weasyprint.HTML('https://mediumread.herokuapp.com/read/https://medium.com/javascript-in-plain-english/full-stack-mongodb-react-node-js-express-js-in-one-simple-app-6cc8ed6de274').write_pdf()
print(type(pdf))
f = open('file.pdf', 'wb')
f.write(pdf)
f.close()
# file('google.pdf', 'w').write(pdf)
