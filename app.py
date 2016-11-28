# -*- coding: utf-8 -*-
import web
from data import data
from web import form

render = web.template.render('views/', base = 'base')

urls=('/(.*)','index')
app= web.application(urls,globals())
data = data()
data.read()
myForm=form.Form(
    form.Dropdown('Periodo',data.getPeriodo()),
    form.Dropdown('Entidad',data.getEntidad())
)
class index:
    def GET(self, results):
        form=myForm
        return render.index(form, None)
        
    def POST(self, results):
        form=myForm
        if not form.validates():
            return render.index(form)
        else:
            user_data = web.input()
            periodos = user_data.Periodo
            entidad = user_data.Entidad
            results = data.getDatos(periodos,entidad)
            return render.index(form, results)

if __name__=="__main__":
    app.run()