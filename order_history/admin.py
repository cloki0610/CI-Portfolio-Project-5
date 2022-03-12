from django.contrib import admin
from .models import OrderReview, Comment


class CommentAdminInline(admin.TabularInline):
    """ Show Comment in OrderReview model page as inline attribute """
    model = Comment
    readonly_fields = ('order_review', 'user',)


@admin.register(OrderReview)
class OrderReviewAdmin(admin.ModelAdmin):
    """ Show OrderReview model in admin site with follow rules """
    inlines = (CommentAdminInline, )
    fields = ('order', 'slug', 'customer', 'order_status',
              'review', 'date', 'last_edit')
    readonly_fields = ('order', 'slug', 'customer', 'date', 'last_edit',)
    list_filter = ('customer', 'order_status',)
    search_fields = ['customer', 'review']
    ordering = ('date', 'last_edit')
