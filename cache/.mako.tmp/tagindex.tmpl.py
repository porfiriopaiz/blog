# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476413330.953695
_enable_loop = True
_template_filename = '/home/porfirio/Documents/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/tagindex.tmpl'
_template_uri = 'tagindex.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content_header']


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
    return runtime._inherit_from(context, 'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tag = context.get('tag', UNDEFINED)
        len = context.get('len', UNDEFINED)
        description = context.get('description', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_atom:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom for the ')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer(' section (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_atom", tag, language)))
                __M_writer('">\n')
        elif generate_atom:
            __M_writer('        <link rel="alternate" type="application/atom+xml" title="Atom for the ')
            __M_writer(filters.html_escape(str(tag)))
            __M_writer(' section" href="')
            __M_writer(str(_link("tag" + "_atom", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        description = context.get('description', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        def content_header():
            return render_content_header(context)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tagindex.tmpl", "filename": "/home/porfirio/Documents/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/tagindex.tmpl", "source_encoding": "utf-8", "line_map": {"128": 16, "129": 18, "135": 129, "27": 0, "48": 2, "53": 19, "58": 30, "64": 21, "78": 21, "79": 22, "80": 22, "81": 23, "82": 24, "83": 25, "84": 25, "85": 25, "86": 25, "87": 25, "88": 25, "89": 25, "90": 27, "91": 28, "92": 28, "93": 28, "94": 28, "95": 28, "101": 4, "111": 4, "112": 6, "113": 6, "114": 7, "115": 8, "116": 8, "117": 8, "118": 10, "119": 11, "120": 11, "121": 11, "122": 13, "123": 14, "124": 14, "125": 14, "126": 14, "127": 14}}
__M_END_METADATA
"""
