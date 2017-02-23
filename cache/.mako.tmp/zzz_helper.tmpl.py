# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487878407.0213087
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_helper.tmpl'
_template_uri = 'zzz_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_translations', 'html_headstart', 'html_feedlinks', 'html_sourcelink', 'html_stylesheets', 'html_tags', 'html_title']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
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
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\n            <script src="/assets/js/scripts.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        prevlink = context.get('prevlink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        description = context.get('description', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n            <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n            <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n')
        else:
            __M_writer('        <link href="/assets/css/font-awesome.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/style.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/flip.css" rel="stylesheet" type="text/css">\n        <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        theme_tag = context.get('theme_tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div itemprop="keywords" class="tags right">\n        <span class=tags>\n            <span class=\'muted small\'> <i class="icon-tag"></i> </span>\n')
        for tag in post.tags:
            __M_writer('        <a\n')
            if theme_tag is not UNDEFINED:
                for (theme, tag_name) in theme_tag.items():
                    if tag_name == tag:
                        __M_writer("                    class='small ")
                        __M_writer(str(theme))
                        __M_writer("'\n                    id='tag-theme' \n                    data-theme='")
                        __M_writer(str(theme))
                        __M_writer("'\n\n")
            __M_writer('        href="')
            __M_writer(str(_link('tag', tag)))
            __M_writer('" rel="tag">')
            __M_writer(str(tag))
            __M_writer('</a>\n')
        __M_writer('        </span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "zzz_helper.tmpl", "source_encoding": "utf-8", "line_map": {"258": 122, "259": 127, "260": 128, "261": 129, "262": 130, "263": 131, "264": 132, "265": 132, "266": 132, "267": 134, "268": 134, "269": 139, "270": 139, "271": 139, "16": 0, "273": 139, "274": 141, "21": 2, "22": 61, "23": 84, "24": 98, "25": 119, "26": 143, "27": 149, "28": 160, "29": 167, "286": 145, "287": 146, "288": 147, "289": 147, "290": 147, "35": 100, "296": 290, "41": 100, "42": 101, "43": 102, "44": 103, "45": 105, "46": 106, "47": 108, "48": 109, "49": 110, "50": 112, "51": 113, "57": 151, "65": 151, "66": 152, "67": 153, "68": 154, "69": 155, "70": 155, "71": 155, "72": 155, "73": 155, "74": 156, "75": 156, "81": 3, "280": 145, "272": 139, "108": 3, "109": 6, "110": 7, "111": 8, "112": 10, "113": 11, "114": 13, "115": 14, "116": 15, "117": 17, "118": 18, "119": 21, "120": 21, "121": 21, "122": 24, "123": 25, "124": 25, "125": 25, "126": 27, "127": 28, "128": 28, "129": 28, "130": 28, "131": 30, "132": 30, "133": 31, "134": 31, "135": 32, "136": 33, "137": 33, "138": 33, "139": 35, "140": 36, "141": 37, "142": 38, "143": 38, "144": 38, "145": 38, "146": 38, "147": 38, "148": 38, "149": 41, "150": 42, "151": 43, "152": 43, "153": 43, "154": 45, "155": 46, "156": 47, "157": 47, "158": 47, "159": 49, "160": 50, "161": 50, "162": 50, "163": 52, "164": 53, "165": 53, "166": 54, "167": 55, "168": 56, "169": 57, "170": 57, "171": 57, "172": 59, "173": 60, "174": 60, "180": 86, "189": 86, "190": 87, "191": 88, "192": 88, "193": 88, "194": 89, "195": 90, "196": 91, "197": 92, "198": 92, "199": 92, "200": 92, "201": 92, "202": 94, "203": 95, "204": 95, "205": 95, "211": 162, "218": 162, "219": 163, "220": 164, "221": 165, "222": 165, "223": 165, "224": 165, "230": 63, "237": 63, "238": 64, "239": 65, "240": 66, "241": 68, "242": 69, "243": 72, "244": 73, "245": 80, "246": 81, "252": 122}, "filename": "themes/lotabout/templates/zzz_helper.tmpl"}
__M_END_METADATA
"""
