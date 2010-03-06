from django.contrib.sites.models import Site

from cms.templatetags.cms_tags import ancestors_from_page
from cms.utils.moderator import get_page_queryset, get_title_queryset
from cms.utils import get_language_from_request,\
    get_extended_navigation_nodes, find_selected

def top_ancestor(context, template="cms/breadcrumb.html"):
    request = context['request']
    page_queryset = get_page_queryset(request)
    title_queryset = get_title_queryset(request) 
    
    page = request.current_page
    if page == "dummy":
        context.update({
            'ancestor': [],
            'template': template,
        })
        return context
    lang = get_language_from_request(request)
    if page and not page.navigation_extenders:
        ancestors = ancestors_from_page(page, page_queryset, title_queryset, lang)
    else:
        site = Site.objects.get_current()
        ancestors = []
        extenders = page_queryset.published().filter(site=site)
        extenders = extenders.exclude(navigation_extenders__isnull=True).exclude(navigation_extenders__exact="")
        for ext in extenders:
            ext.childrens = []
            ext.ancestors_ascending = []
            nodes = get_extended_navigation_nodes(request, 100, [ext], ext.level, 100, 0, False, ext.navigation_extenders)
            if hasattr(ext, "ancestor"):
                selected = find_selected(nodes)
                if selected:
                    ancestors = list(ext.get_ancestors()) + [ext]
                    home = page_queryset.get_home()
                    if ancestors and ancestors[0].pk != home.pk: 
                        ancestors = [home] + ancestors
                    ids = []
                    for anc in ancestors:
                        ids.append(anc.pk)
                    titles = title_queryset.filter(page__in=ids, language=lang)
                    ancs = []
                    for anc in ancestors:
                        anc.home_pk_cache = home.pk
                        anc.ancestors_ascending = ancs[:]
                        ancs += [anc]
                        for title in titles:
                            if title.page_id == anc.pk:
                                if not hasattr(anc, "title_cache"):
                                    anc.title_cache = {}
                                anc.title_cache[title.language] = title
                    ancestors = ancestors + selected.ancestors_ascending[1:] + [selected]
        if not ancestors and page:
            ancestors = ancestors_from_page(page, page_queryset, title_queryset, lang)
    
    if ancestors and home and ancestors[0].pk != home.pk: 
        ancestors = [home] + ancestors
    
    context.update({'ancestors':ancestors,
                    'template': template})
    return context
top_ancestor = register.inclusion_tag('cms/dummy.html',
                                         takes_context=True)(top_ancestor)