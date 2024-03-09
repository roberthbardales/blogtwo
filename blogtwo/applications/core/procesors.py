from .models import About, Link,Category

def ctx_dic_link(request):
    ctx_dic_link={}
    links=Link.objects.all()
    for link in links:
        ctx_link[link.key]={'url':link.url,'icon':link_icon}
    return ctx_link
