# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497550426.1848514
_enable_loop = True
_template_filename = '/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_items = context.get('cat_items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_items = context.get('cat_items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n')
        if cat_items:
            __M_writer('        <h2>')
            __M_writer(str(messages("Categories")))
            __M_writer('</h2>\n        <ul class="postlist">\n')
            for text, link in cat_items:
                if text:
                    __M_writer('                <li><a class="reference" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <ul class="postlist">\n')
            for text, link in items:
                __M_writer('            <li><a class="reference listtitle" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tags.tmpl", "source_encoding": "utf-8", "filename": "/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/tags.tmpl", "line_map": {"64": 10, "65": 10, "66": 12, "67": 13, "68": 14, "69": 14, "70": 14, "71": 14, "72": 14, "73": 17, "74": 18, "75": 19, "76": 19, "77": 19, "78": 22, "79": 23, "80": 24, "81": 25, "82": 25, "83": 25, "84": 25, "85": 25, "86": 27, "87": 29, "27": 0, "93": 87, "38": 2, "43": 30, "49": 4, "59": 4, "60": 7, "61": 7, "62": 9, "63": 10}}
__M_END_METADATA
"""
