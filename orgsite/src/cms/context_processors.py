from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cms.models import NavBlock, HomeBlock, ServicesBlock, PortfolioBlock, AboutBlock

def template_tag(request):
    nav       = NavBlock.objects.all()
    if nav:
        nav = nav[0]
    else:
        nav = NavBlock()
        nav.shopname = 'Org08'
        nav.services = '服務'
        nav.portfolio = '產品'
        nav.aboutus = '關於我們'

    home      = HomeBlock.objects.all()
    if home:
        home = home[0]
    else:
        home = HomeBlock()
        home.title = '歡迎光臨'
        home.subtitle = '我們能提供最好的服務以及最棒的產品'

    services  = ServicesBlock.objects.all()
    if services:
        services = services[0]

    ser_list  = ServicesBlock.objects.all()
    paginator = Paginator(ser_list, 8) # Show 8 post per page
    page = request.GET.get('page')
    try:
        post_contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_contacts = paginator.page(paginator.num_pages)

    #portfolio = PortfolioBlock.objects.all()[0]
    #about     = AboutBlock.objects.all()[0]

    return {'navblock'      : nav,
            'homeblock'     : home,
            'ser_list'      : ser_list,
            'servicesblock' : services,
         # 'portfolioblock': portfolio,
         # 'aboutblock'    : about        
    }
    