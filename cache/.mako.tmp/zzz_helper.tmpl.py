# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497550425.988457
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_helper.tmpl'
_template_uri = 'zzz_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_title', 'html_sourcelink', 'html_headstart', 'html_tags', 'html_feedlinks', 'html_stylesheets', 'html_translations']


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
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
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


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "zzz_helper.tmpl", "source_encoding": "utf-8", "filename": "themes/lotabout/templates/zzz_helper.tmpl", "line_map": {"257": 63, "258": 64, "259": 65, "260": 66, "261": 68, "262": 69, "263": 72, "264": 73, "265": 80, "266": 81, "16": 0, "21": 2, "22": 61, "23": 84, "24": 98, "25": 119, "26": 143, "27": 149, "28": 160, "29": 167, "286": 155, "287": 155, "288": 155, "289": 156, "290": 156, "35": 100, "296": 290, "41": 100, "42": 101, "43": 102, "44": 103, "45": 105, "46": 106, "47": 108, "48": 109, "49": 110, "50": 112, "51": 113, "283": 154, "57": 145, "63": 145, "64": 146, "65": 147, "66": 147, "67": 147, "73": 162, "80": 162, "81": 163, "82": 164, "83": 165, "84": 165, "85": 165, "86": 165, "92": 3, "272": 151, "284": 155, "282": 153, "285": 155, "119": 3, "120": 6, "121": 7, "122": 8, "123": 10, "124": 11, "125": 13, "126": 14, "127": 15, "128": 17, "129": 18, "130": 21, "131": 21, "132": 21, "133": 24, "134": 25, "135": 25, "136": 25, "137": 27, "138": 28, "139": 28, "140": 28, "141": 28, "142": 30, "143": 30, "144": 31, "145": 31, "146": 32, "147": 33, "148": 33, "149": 33, "150": 35, "151": 36, "152": 37, "153": 38, "154": 38, "155": 38, "156": 38, "157": 38, "158": 38, "159": 38, "160": 41, "161": 42, "162": 43, "163": 43, "164": 43, "165": 45, "166": 46, "167": 47, "168": 47, "169": 47, "170": 49, "171": 50, "172": 50, "173": 50, "174": 52, "175": 53, "176": 53, "177": 54, "178": 55, "179": 56, "180": 57, "181": 57, "182": 57, "183": 59, "184": 60, "185": 60, "191": 122, "197": 122, "198": 127, "199": 128, "200": 129, "201": 130, "202": 131, "203": 132, "204": 132, "205": 132, "206": 134, "207": 134, "208": 139, "209": 139, "210": 139, "211": 139, "212": 139, "213": 141, "219": 86, "280": 151, "228": 86, "229": 87, "230": 88, "231": 88, "232": 88, "233": 89, "234": 90, "235": 91, "236": 92, "237": 92, "238": 92, "239": 92, "240": 92, "241": 94, "242": 95, "243": 95, "244": 95, "250": 63, "281": 152}}
__M_END_METADATA
"""
