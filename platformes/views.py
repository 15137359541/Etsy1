from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request,'platformes/index.html')
    else:
        return HttpResponse('这并非是一个get请求')
#看看文件上传上去的格式
def file_update(request):
    if request.method == "GET":
        return render(request,'platformes/file_update.html')
    else:
        print("request.path", request.path)
        print("request.POST", request.POST)
        print("request.file", request.FILES)
        title = request.POST['title']
        price_ago = request.POST['price_ago']
        price_now = request.POST['price_now']
        feedback = request.POST['feedback']
        favorited = request.POST['favorited']
        img = request.FILES['img']

        ever_good=models.Goods.goods_manage.create(title=title,price_now=price_now,price_ago=price_ago,feedback=feedback,favorited=favorited,img=img)
        print("商品为：",ever_good)
        return render(request,"platformes/index.html")

def tatalGoods(request):
    # print("request.path", request.path)
    # print("request.method", request.method)
    try:#从搜索框过来
        content=request.GET['search']
        price_low = request.GET["price_low"]
        price_high = request.GET["price_high"]

        # 获取查询的商品类型
        # 分页展示的时候，前端不会再一次传递内容参数，所以if一下，为空的话就用session获取
        if (content or price_low or price_high):
            request.session['search'] = content
            request.session['price_low'] = price_low
            request.session['price_high'] = price_high

        else:
            content=request.session['search']
            price_low=request.session['price_low']
            price_high = request.session['price_high']

        #处理价格
        try:#拥有最低高价
            # print("有高低")
            all_goods = models.Goods.goods_manage.filter(title__icontains=content,price_now__gt=price_low,price_now__lt=price_high).order_by('feedback')
            currentPage, all_goods ,paginator,page_obj= page(request, all_goods, 20)
            return render(request, 'platformes/index.html', {'all_goods': all_goods, 'currentPage': currentPage,'paginator':paginator,'page_obj':page_obj})
        except:#没有最高只有最低
            try:
                # print("有低")
                all_goods = models.Goods.goods_manage.filter(title__icontains=content,price_now__gt=price_low).order_by('-feedback')
                currentPage, all_goods ,paginator,page_obj = page(request, all_goods, 20)
                return render(request, 'platformes/index.html',
                              {'all_goods': all_goods, 'currentPage': currentPage,'paginator':paginator,'page_obj':page_obj})
            except:
                try:
                    # print("有高")
                    all_goods = models.Goods.goods_manage.filter(title__icontains=content,price_now__lt=price_high).order_by('-feedback')
                    currentPage, all_goods ,paginator ,page_obj= page(request, all_goods, 20)
                    return render(request, 'platformes/index.html',
                                  {'all_goods': all_goods, 'currentPage': currentPage,'paginator':paginator,'page_obj':page_obj})
                except:
                    # print("没有高低")
                    all_goods = models.Goods.goods_manage.filter(title__icontains=content).order_by('-feedback')
                    if all_goods:
                        print("能查询到数据")
                        currentPage, all_goods ,paginator, page_obj= page(request, all_goods, 20)
                        return render(request, 'platformes/index.html',{'all_goods': all_goods, 'currentPage': currentPage,'paginator':paginator,'page_obj':page_obj})
                    else:
                        print("没有数据")
                        return render(request, 'platformes/index.html')
    except:
        print("不是从搜索框中过来的，从url地址或者a标签")
        content = request.session['search']
        price_low = request.session['price_low']
        price_high = request.session['price_high']
        if(content or price_low or price_high):
            print(request.session['search'])
            print(request.session['price_low'])
            print('all over')
            print(request.session['price_high'])
            try:  # 拥有最低高价
                # print("有高低")
                all_goods = models.Goods.goods_manage.filter(title__icontains=content, price_now__gt=price_low,
                                                             price_now__lt=price_high).order_by('feedback')
                currentPage, all_goods, paginator,page_obj = page(request, all_goods, 20)
                return render(request, 'platformes/index.html',
                              {'all_goods': all_goods, 'currentPage': currentPage, 'paginator': paginator,'page_obj':page_obj})
            except:  # 没有最高只有最低
                try:
                    # print("有低")
                    all_goods = models.Goods.goods_manage.filter(title__icontains=content,
                                                                 price_now__gt=price_low).order_by('-feedback')
                    currentPage, all_goods, paginator,page_obj = page(request, all_goods, 20)
                    return render(request, 'platformes/index.html',
                                  {'all_goods': all_goods, 'currentPage': currentPage, 'paginator': paginator,'page_obj':page_obj})
                except:
                    try:
                        # print("有高")
                        all_goods = models.Goods.goods_manage.filter(title__icontains=content,
                                                                     price_now__lt=price_high).order_by('-feedback')
                        currentPage, all_goods, paginator,page_obj = page(request, all_goods, 20)
                        return render(request, 'platformes/index.html',
                                      {'all_goods': all_goods, 'currentPage': currentPage, 'paginator': paginator,'page_obj':page_obj})
                    except:
                        # print("没有高低")
                        all_goods = models.Goods.goods_manage.filter(title__icontains=content).order_by('-feedback')
                        if all_goods:
                            print("能查询到数据")
                            currentPage, all_goods, paginator,page_obj = page(request, all_goods, 20)
                            return render(request, 'platformes/index.html',
                                          {'all_goods': all_goods, 'currentPage': currentPage, 'paginator': paginator,'page_obj':page_obj})
                        else:
                            print("没有数据")
                            return render(request, 'platformes/index.html')
        else:
            all_goods = models.Goods.goods_manage.filter().order_by('-feedback')

            currentPage, all_goods  ,paginator,page_obj= page(request, all_goods, 20)
            return render(request, 'platformes/index.html', {'all_goods': all_goods, 'currentPage': currentPage,'paginator':paginator,'page_obj':page_obj})





#对所有的商品进行分页展示
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#传递对象值和每页显示的记录个数
def page(request,obj,item):
    # 获取Book数据表中的所有记录
    # 生成paginator对象,定义每页显示20条记录
    paginator = Paginator(obj, item)

    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)

    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    #如果页数过多时，做进一步处理
    if paginator.num_pages >10:
        if currentPage-3<1:
            pageRange = range(1,6)
        elif currentPage+3 > paginator.num_pages:
            pageRange=range(currentPage-3,paginator.num_pages+1)
        else:
            pageRange=range(currentPage -3,currentPage+3)
    else:
        pageRange = paginator.page_range
    try:
        print(page)
        book_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        book_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return currentPage,book_list,pageRange,paginator
