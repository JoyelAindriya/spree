from django.db import models

# Create your models here.

class entity_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class entity_data(models.Model):
    name            = models.CharField(max_length=100,default='')
    entity_type_id  = models.ForeignKey(entity_type,on_delete=models.CASCADE,default='',null=True)
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class branch_data(models.Model):
    entity_id       = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    name            = models.CharField(max_length=100,default='',null=True)
    branch_code     = models.CharField(max_length=100,default='',null=True)
    address         = models.CharField(max_length=100,default='',null=True)
    city            = models.CharField(max_length=100,default='',null=True)
    state           = models.CharField(max_length=100,default='',null=True)
    country         = models.CharField(max_length=100,default='',null=True)
    pincode         = models.CharField(max_length=100,default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class user_roles(models.Model):
    role            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class user_data(models.Model):
    branch_id       = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    user_role_id    = models.ForeignKey(user_roles,on_delete=models.CASCADE,default='',null=True)
    entity_id       = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    name            = models.CharField(max_length=100,default='',null=True)
    email           = models.CharField(max_length=100,default='',null=True)
    password        = models.CharField(max_length=100,default='',null=True)
    profile_image   = models.ImageField(upload_to='image',null=True)
    active          = models.BooleanField(max_length=100,default=0)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class accounting_group_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    under_group         = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='accound_group')
    nature              = models.CharField(max_length=100,default='',null=True)
    affect_gross_profit = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class accounting_ledger_data(models.Model):
    name                = models.CharField(max_length=100,default='',null=True)
    accounting_group_id = models.ForeignKey(accounting_group_data,on_delete=models.CASCADE,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class financial_year_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    from_date           = models.CharField(max_length=100,default='',null=True)
    to_date             = models.TextField(default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class series_data(models.Model):
    type                = models.CharField(max_length=100,default='',null=True)
    pre_text            = models.CharField(max_length=100,default='',null=True)
    post_text           = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class customer_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class location_data(models.Model):
    location        = models.CharField(max_length=100,default='')
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class customer_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    customer_type_id    = models.ForeignKey(customer_type,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    phone               = models.CharField(max_length=100,default='',null=True)
    email               = models.CharField(max_length=100,default='',null=True)
    customer_code       = models.CharField(max_length=100,default='',null=True)
    location_id         = models.ForeignKey(location_data,on_delete=models.CASCADE,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    credit_period       = models.CharField(max_length=100,default='',null=True)
    credit_limit        = models.CharField(max_length=100,default='',null=True)
    address             = models.CharField(max_length=100,default='',null=True)
    city                = models.CharField(max_length=100,default='',null=True)
    state               = models.CharField(max_length=100,default='',null=True)
    country             = models.CharField(max_length=100,default='',null=True)
    pincode             = models.CharField(max_length=100,default='',null=True)
    account_number      = models.CharField(max_length=100,default='',null=True)
    branch_name         = models.CharField(max_length=100,default='',null=True)
    branch_code         = models.CharField(max_length=100,default='',null=True)
    tin                 = models.CharField(max_length=100,default='',null=True)
    pan                 = models.CharField(max_length=100,default='',null=True)
    cst                 = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class supplier_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class supplier_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    supplier_type_id    = models.ForeignKey(supplier_type,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    phone               = models.CharField(max_length=100,default='',null=True)
    email               = models.CharField(max_length=100,default='',null=True)
    supplier_code       = models.CharField(max_length=100,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    credit_period       = models.CharField(max_length=100,default='',null=True)
    credit_limit        = models.CharField(max_length=100,default='',null=True)
    address             = models.CharField(max_length=100,default='',null=True)
    city                = models.CharField(max_length=100,default='',null=True)
    state               = models.CharField(max_length=100,default='',null=True)
    country             = models.CharField(max_length=100,default='',null=True)
    pincode             = models.CharField(max_length=100,default='',null=True)
    account_number      = models.CharField(max_length=100,default='',null=True)
    branch_name         = models.CharField(max_length=100,default='',null=True)
    branch_code         = models.CharField(max_length=100,default='',null=True)
    tin                 = models.CharField(max_length=100,default='',null=True)
    pan                 = models.CharField(max_length=100,default='',null=True)
    cst                 = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class unit_data(models.Model):
    unit                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    formal_name         = models.CharField(max_length=100,default='',null=True)
    no_of_decimal_place = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class size_data(models.Model):
    size                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class brand_data(models.Model):
    name                = models.CharField(max_length=100,default='',null=True)
    manufacture         = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class model_number_data(models.Model):
    model_number        = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class godown_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class rack_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    godown_id           = models.ForeignKey(godown_data,on_delete=models.CASCADE,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class product_group_data(models.Model):
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    under_group         = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='product_group')
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class pricing_level_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class tax_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    tax                 = models.CharField(max_length=100,default='',null=True)
    rate_perc           = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class product_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    product_code        = models.CharField(max_length=100,default='',null=True)
    product_group_id    = models.ForeignKey(product_group_data,on_delete=models.CASCADE,default='',null=True)
    brand_id            = models.ForeignKey(brand_data,on_delete=models.CASCADE,default='',null=True)
    unit_id             = models.ForeignKey(unit_data,on_delete=models.CASCADE,default='',null=True)
    size_id             = models.ForeignKey(size_data,on_delete=models.CASCADE,default='',null=True)
    model_number_id     = models.ForeignKey(model_number_data,on_delete=models.CASCADE,default='',null=True)
    godown_id           = models.ForeignKey(godown_data,on_delete=models.CASCADE,default='',null=True)
    rack_id             = models.ForeignKey(rack_data,on_delete=models.CASCADE,default='',null=True)
    purchase_rate       = models.CharField(max_length=100,default='',null=True)
    mrp                 = models.CharField(max_length=100,default='',null=True)
    sales_rate          = models.CharField(max_length=100,default='',null=True)
    reorder_level       = models.CharField(max_length=100,default='',null=True)
    minimum_stock       = models.CharField(max_length=100,default='',null=True)
    maximum_stock       = models.CharField(max_length=100,default='',null=True)
    tax                 = models.CharField(max_length=100,default='',null=True)
    bom                 = models.CharField(max_length=100,default='',null=True)
    bar_code            = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class voucher_type_data(models.Model):
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    type_of_voucher     = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='voucher_type')
    start_index         = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')