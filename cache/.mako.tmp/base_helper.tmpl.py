# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497550426.0281117
_enable_loop = True
_template_filename = '/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_feedlinks', 'html_stylesheets', 'html_headstart', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        prevlink = context.get('prevlink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        nextlink = context.get('nextlink', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(_link("index", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/lib64/python3.4/site-packages/nikola/data/themes/base/templates/base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 61, "23": 65, "24": 82, "25": 96, "26": 106, "32": 63, "37": 63, "38": 64, "39": 64, "45": 84, "54": 84, "55": 85, "56": 86, "57": 86, "58": 86, "59": 87, "60": 88, "61": 89, "62": 90, "63": 90, "64": 90, "65": 90, "66": 90, "67": 92, "68": 93, "69": 93, "70": 93, "76": 67, "83": 67, "84": 68, "85": 69, "86": 70, "87": 71, "88": 72, "89": 74, "90": 75, "91": 78, "92": 79, "98": 3, "125": 3, "126": 6, "127": 7, "128": 8, "129": 10, "130": 11, "131": 13, "132": 14, "133": 15, "134": 17, "135": 18, "136": 21, "137": 21, "138": 21, "139": 24, "140": 25, "141": 25, "142": 25, "143": 27, "144": 28, "145": 28, "146": 28, "147": 28, "148": 30, "149": 30, "150": 31, "151": 31, "152": 32, "153": 33, "154": 33, "155": 33, "156": 35, "157": 36, "158": 37, "159": 38, "160": 38, "161": 38, "162": 38, "163": 38, "164": 38, "165": 38, "166": 41, "167": 42, "168": 43, "169": 43, "170": 43, "171": 45, "172": 46, "173": 47, "174": 47, "175": 47, "176": 49, "177": 50, "178": 50, "179": 50, "180": 52, "181": 53, "182": 53, "183": 54, "184": 55, "185": 56, "186": 57, "187": 57, "188": 57, "189": 59, "190": 60, "191": 60, "197": 98, "205": 98, "206": 100, "207": 101, "208": 102, "209": 102, "210": 102, "211": 102, "212": 102, "213": 102, "214": 102, "215": 105, "221": 215}}
__M_END_METADATA
"""
