from wtforms.widgets import HTMLString, html_params
from wtforms import Field
class ButtonWidget(object):  # 自定义一个input组件
    def __call__(self, field, **kwargs):
        if field.name is not None:
            kwargs.setdefault("name", field.name)
        kwargs.setdefault("type", field.btype)
        kwargs.setdefault('id', field.id)
        kwargs.setdefault("value", field.value)
        return HTMLString("<input %s>" % (html_params(**kwargs)))
class InputButtonField(Field):
    widget = ButtonWidget()
    """
    @params value 按钮的标签
    @params text  按钮的文本
    """
    def __init__(self,value="按钮",text="btn",btype="button",**kwargs):
    	super(InputButtonField, self).__init__(**kwargs)
    	self.type = "SubmitField"
    	self.btype = btype
    	self.value = value
    	self.text = text