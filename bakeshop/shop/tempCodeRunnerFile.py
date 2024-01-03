  categ_paginated = Paginator(Category.objects.all(), 3)
    page_number = request.GET.get('page')
    page = category_paginated.get_page(page_number)
    nums = "a" * page.paginator.num_pages