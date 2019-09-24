__all__ = ['email_parser']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['add'])
@Js
def PyJsHoisted_add_(td, this, arguments, var=var):
    var = Scope({'td':td, 'this':this, 'arguments':arguments}, var)
    var.registers(['td'])
    if var.put('test', JsRegExp('/eval\\("(.*)\\);/').callprop('exec', var.get('td'))):
        while (var.get('test').get('1').callprop('indexOf', Js('\\'))!=(-Js(1.0))):
            var.get('test').put('1', var.get('test').get('1').callprop('replace', Js('\\'), Js('')))
        var.get('eval')((var.get('test').get('1')+Js(');')))
        var.put('td', var.get('d'))
    return var.get('td')
PyJsHoisted_add_.func_name = 'add'
var.put('add', PyJsHoisted_add_)
pass
pass


# Add lib to the module scope
email_parser = var.to_python()