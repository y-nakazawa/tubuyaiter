from django.shortcuts import render, get_object_or_404
from app.models import Mutter


def mutter_list(request):

    if request.method == 'POST':
        mutter = Mutter.objects.create(content=request.POST.get("content", ""))
        mutter.save()

    keyword = request.GET.get(key="keyword", default=None)

    if keyword:
        mutters = Mutter.objects.filter(content__contains=keyword).order_by("created_at").reverse()
    else:
        mutters = Mutter.objects.all().order_by("created_at").reverse()

    return render(request, 'mutter_list.html', dict(mutters=mutters))


def mutter_detail(request, mutter_id):

    # mutter_idが一致するつぶやきを取得する
    #mutter = Mutter.objects.get(id=mutter_id)
    mutter = get_object_or_404(Mutter, id=mutter_id)
    return render(request, 'mutter_detail.html', dict(mutter=mutter))
