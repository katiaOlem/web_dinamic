import web

urls = (
    '/', 'index',
    '/webpy', 'webpy',
    '/javascript', 'javascript'
)
app = web.application(urls, globals())
render= web.template.render("templates/", base="layout")

class index:
    def GET(self):
        return render.index()

class webpy:
    def GET(self):
        resultado = 0
        return render.webpy(resultado)

    def POST(self):
        form        =   web.input()
        num1        =   int(form.num1)
        num2        =   int(form.num2)
        resultado   =   num1 + num2
        return render.webpy(resultado)


class javascript:
    def GET(self):
        return render.javascript()     
        
           
if __name__ == "__main__":
    app.run()