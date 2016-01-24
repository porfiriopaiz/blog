# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453613610.9097397
_enable_loop = True
_template_filename = '/home/porfirio/virtualenvs/nikola3/lib/python3.4/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        index_file = context.get('index_file', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "filename": "/home/porfirio/virtualenvs/nikola3/lib/python3.4/site-packages/nikola/data/themes/base/templates/index.tmpl", "line_map": {"128": 36, "129": 36, "130": 37, "131": 38, "132": 39, "133": 39, "134": 41, "135": 44, "136": 45, "137": 45, "138": 46, "139": 46, "140": 47, "141": 47, "147": 6, "23": 2, "26": 3, "157": 6, "158": 7, "159": 7, "32": 0, "161": 9, "162": 9, "163": 9, "169": 14, "180": 169, "54": 2, "55": 3, "56": 4, "61": 11, "160": 8, "66": 48, "72": 13, "88": 13, "93": 14, "94": 16, "95": 17, "96": 17, "97": 17, "98": 19, "99": 19, "100": 19, "101": 19, "102": 22, "103": 23, "104": 23, "105": 23, "106": 23, "107": 23, "108": 24, "109": 25, "110": 25, "111": 25, "112": 27, "113": 28, "114": 28, "115": 28, "116": 28, "117": 28, "118": 28, "119": 28, "120": 28, "121": 29, "122": 30, "123": 30, "124": 30, "125": 32, "126": 34, "127": 35}}
__M_END_METADATA
"""
