# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 自定义显示什么内容 exclude:不显示那些内容
    # fields = ('title', 'desc', 'content',)
    # fields和fieldsets中的内容不能重复
    # 隐藏要填写的其他东西,可以展开,选填
    # admin中菜单上显示的内容 list_display_links可以点击内容
    # list_display = ('title', 'desc', 'content',)
    # list_display_links = ('title', 'desc', 'content',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'desc', 'content',)
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse',),
    #         'fields': ('click_count', 'is_recommend',)
    #     })
    # )

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Ad)
admin.site.register(Links)
