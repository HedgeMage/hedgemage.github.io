# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497550426.0111964
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_header.tmpl'
_template_uri = 'zzz_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu" role="navigation">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li> ')
                __M_writer(str(text))
                __M_writer('\n            <ul>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <header id="header" class="header transparent">\n        <div class="container">\n            <div class="scroll top">\n                <a href=\'#\'><i class="icon-chevron-up icon-large"></i></a>\n            </div>\n\n            ')
        __M_writer(str(html_site_title()))
        __M_writer('\n            ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        __M_writer("        </div>\n        <div class='separator clearfix'></div>\n    </header>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div class="brand">\n        <div class="flip_container">\n            <div class="flipper">\n                <div class="front">\n                    <p><a href="')
        __M_writer(str(abs_link('/')))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('                        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                        <span id="blog-title">')
            __M_writer(str(blog_title))
            __M_writer('</span>\n')
        __M_writer('                    </a></p>\n                </div>\n\n')
        if show_blog_title and blog_description:
            __M_writer('                <div class="back">\n                    <p><a href="')
            __M_writer(str(abs_link('/')))
            __M_writer('" title="')
            __M_writer(str(blog_description))
            __M_writer('" rel="home">\n                        <span id="blog-description">')
            __M_writer(str(blog_description))
            __M_writer('</span>\n                    </a></p>\n                </div>\t\t\t\n')
        __M_writer('            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "zzz_header.tmpl", "source_encoding": "utf-8", "filename": "themes/lotabout/templates/zzz_header.tmpl", "line_map": {"130": 25, "131": 30, "132": 30, "133": 30, "134": 30, "135": 31, "136": 32, "137": 32, "138": 32, "139": 32, "140": 32, "141": 34, "142": 35, "143": 36, "144": 36, "145": 36, "146": 38, "147": 41, "148": 42, "149": 43, "150": 43, "23": 2, "152": 43, "153": 44, "26": 0, "155": 48, "154": 44, "33": 2, "34": 22, "35": 51, "36": 81, "42": 54, "151": 43, "55": 54, "56": 57, "57": 58, "58": 59, "59": 59, "60": 59, "61": 61, "62": 62, "63": 63, "64": 63, "65": 63, "66": 63, "67": 63, "68": 64, "69": 65, "70": 65, "71": 65, "72": 65, "73": 65, "74": 68, "75": 69, "76": 70, "77": 71, "78": 71, "79": 71, "80": 71, "81": 71, "82": 72, "83": 73, "84": 73, "85": 73, "86": 73, "87": 73, "88": 77, "89": 77, "90": 77, "91": 78, "92": 78, "98": 4, "161": 155, "108": 4, "109": 12, "110": 12, "111": 13, "112": 13, "113": 19, "119": 25}}
__M_END_METADATA
"""
