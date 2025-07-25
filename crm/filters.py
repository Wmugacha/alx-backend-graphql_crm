import django_filters
from .models import Customer, Product, Order
from django.db.models import Q
from django_filters import OrderingFilter


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    created_at__gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')
    phone_pattern = django_filters.CharFilter(method='filter_phone_pattern')
    order_by = OrderingFilter(
        fields=(
            ('email', 'email'),
            ('first_name', 'name'),
            ('created_at', 'created_at'),
        )
    )

    class Meta:
        model = Customer
        fields = ['first_name', 'email', 'created_at', 'phone']

    def filter_phone_pattern(self, queryset, name, value):
        return queryset.filter(phone__startswith=value)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    stock__gte = django_filters.NumberFilter(field_name="stock", lookup_expr='gte')
    stock__lte = django_filters.NumberFilter(field_name="stock", lookup_expr='lte')
    order_by = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('price', 'price'),
            ('stock', 'stock'),
        )
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']


class OrderFilter(django_filters.FilterSet):
    total_amount__gte = django_filters.NumberFilter(field_name='total_amount', lookup_expr='gte')
    total_amount__lte = django_filters.NumberFilter(field_name='total_amount', lookup_expr='lte')
    order_date__gte = django_filters.DateFilter(field_name='order_date', lookup_expr='gte')
    order_date__lte = django_filters.DateFilter(field_name='order_date', lookup_expr='lte')
    customer_name = django_filters.CharFilter(method='filter_customer_name')
    product_name = django_filters.CharFilter(method='filter_product_name')
    product_id = django_filters.UUIDFilter(method='filter_product_id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    order_by = OrderingFilter(
        fields=(
            ('created_at', 'order_date'),
            ('total_amount', 'total_amount'),
        )
    )

    class Meta:
        model = Order
        fields = ['total_amount', 'order_date', 'customer', 'products']

    def filter_customer_name(self, queryset, name, value):
        return queryset.filter(customer__first_name__icontains=value)

    def filter_product_name(self, queryset, name, value):
        return queryset.filter(products__name__icontains=value).distinct()

    def filter_product_id(self, queryset, name, value):
        return queryset.filter(products__id=value).distinct()
