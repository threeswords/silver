from django_filters import (FilterSet, CharFilter, BooleanFilter, DateFilter,
                            NumberFilter)
from silver.models import (MeteredFeature, Subscription, Customer, Provider,
                           Plan, Invoice, BillingDocument, Proforma)


class MeteredFeaturesFilter(FilterSet):
    name = CharFilter(name='name', lookup_type='icontains')

    class Meta:
        model = MeteredFeature
        fields = ('name', )


class SubscriptionFilter(FilterSet):
    plan = CharFilter(name='plan__name', lookup_type='icontains')
    reference = CharFilter(name='reference', lookup_type='icontains')

    class Meta:
        model = Subscription
        fields = ['plan', 'reference', 'state']


class CustomerFilter(FilterSet):
    active = BooleanFilter(name='is_active', lookup_type='iexact')
    email = CharFilter(name='email', lookup_type='icontains')
    company = CharFilter(name='company', lookup_type='icontains')
    name = CharFilter(name='name', lookup_type='icontains')
    country = CharFilter(name='country', lookup_type='icontains')
    sales_tax_name = CharFilter(name='sales_tax_name', lookup_type='icontains')
    sales_tax_number = CharFilter(name='sales_tax_number',
                                  lookup_type='icontains')
    consolidated_billing = CharFilter(name='consolidated_billing',
                                      lookup_type='icontains')
    reference = CharFilter(name='customer_reference', lookup_type='icontains')

    class Meta:
        model = Customer
        fields = ['email', 'name', 'company', 'active', 'country', 'reference',
                  'sales_tax_name', 'consolidated_billing', 'sales_tax_number']


class ProviderFilter(FilterSet):
    email = CharFilter(name='email', lookup_type='icontains')
    company = CharFilter(name='company', lookup_type='icontains')

    class Meta:
        model = Provider
        fields = ['email', 'company']


class PlanFilter(FilterSet):
    name = CharFilter(name='name', lookup_type='icontains')
    currency = CharFilter(name='currency', lookup_type='icontains')
    enabled = BooleanFilter(name='enabled', lookup_type='iexact')
    private = BooleanFilter(name='private', lookup_type='iexact')
    interval = CharFilter(name='interval', lookup_type='icontains')
    product_code = CharFilter(name='product_code', lookup_type='icontains')
    provider = CharFilter(name='provider__company', lookup_type='icontains')

    class Meta:
        model = Plan
        fields = ['name', 'currency', 'enabled', 'private', 'product_code',
                  'provider', 'interval']


class BillingDocumentFilter(FilterSet):
    state = CharFilter(name='state', lookup_type='iexact')
    number = NumberFilter(name='number', lookup_type='iexact')
    customer_name = CharFilter(name='customer__name', lookup_type='icontains')
    customer_company = CharFilter(name='customer__company',
                                  lookup_type='icontains')
    provider_name = CharFilter(name='provider__name', lookup_type='icontains')
    provider_company = CharFilter(name='provider__company',
                                  lookup_type='icontains')
    issue_date = DateFilter(name='issue_date', lookup_type='iexact')
    due_date = DateFilter(name='due_date', lookup_type='iexact')
    paid_date = DateFilter(name='due_date', lookup_type='iexact')
    cancel_date = DateFilter(name='cancel_date', lookup_type='iexact')
    currency = CharFilter(name='currency', lookup_type='icontains')
    sales_tax_name = CharFilter(name='sales_tax_name', lookup_type='icontains')

    class Meta:
        fields = ['state', 'number', 'customer_name', 'customer_company',
                  'issue_date', 'due_date', 'paid_date', 'cancel_date',
                  'currency', 'sales_tax_name']


class InvoiceFilter(BillingDocumentFilter):
    series = CharFilter(name='provider__invoice_series',
                        lookup_type='icontains')

    class Meta(BillingDocumentFilter.Meta):
        model = Invoice
        fields = BillingDocumentFilter.Meta.fields + ['series', ]


class ProformaFilter(BillingDocumentFilter):
    series = CharFilter(name='provider__proforma_series',
                        lookup_type='icontains')

    class Meta(BillingDocumentFilter.Meta):
        model = Proforma
        fields = BillingDocumentFilter.Meta.fields + ['series', ]