from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        title = 'Главная'
        content = {
            'title': title,
            # 'products': product_list,
            # 'occupied_dates': visits(str(datetime.date.today())),
            # 'service_names': services(),
            # 'product_compilation_list': product_compilation_list,
            # # Формат следующего поля: [[compilation.id, product.id], ... ]
            # 'product_compilation_list_product_list': product_compilation_list_product_list,
        }
        return render(request, 'index.html', content)
    else:
        return redirect('auth:login')
    # if LOW_CACHE:
    #     key = 'products'
    #     product_list = cache.get(key)
    #     if product_list is None:
    #         product_list = Product.objects.filter(is_active=True)
    #         cache.set(key, product_list)
    #     key = "compilations"
    #     product_compilation_list = cache.get(key)
    #     if product_compilation_list is None:
    #         product_compilation_list = ProductCompilation.objects.filter(is_active=True)
    #         cache.set(key, product_compilation_list)
    #
    #     product_compilation_list_product_list = []
    #     for c in product_compilation_list:
    #         for product in c.product_list.prefetch_related():
    #             product_compilation_list_product_list.append([c.id, product.id])
    #

