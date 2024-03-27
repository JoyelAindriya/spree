from django.urls import path,include
from SpreeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.userLogin ,name='user-login'),
    path('user-logout/', views.userLogout ,name='user-logout'),

    path('user-dashboard/', views.userDashboard ,name='user-dashboard'),
    
    path('list-entity-type/', views.listEntityType ,name='list-entity-type'),
    path('add-entity-type/', views.addNewEntityType ,name='add-entity-type'),
    path('update-entity-type/', views.updateEntityType ,name='update-entity-type'),
    path('delete-entity-type/', views.deleteEntityType ,name='delete-entity-type'),

    path('list-entity/', views.listEntity ,name='list-entity'),
    path('add-entity/', views.addNewEntity ,name='add-entity'),
    path('update-entity/', views.updateEntity ,name='update-entity'),
    path('delete-entity/', views.deleteEntity ,name='delete-entity'),

    path('list-branch/', views.listBanch ,name='list-branch'),
    path('add-branch/', views.addNewBranch ,name='add-branch'),
    path('update-branch/', views.updateBranch ,name='update-branch'),
    path('delete-branch/', views.deleteBranch ,name='delete-branch'),

    path('list-user-roles/', views.listUserRole ,name='list-user-roles'),
    path('add-user-role/', views.addNewUserRole ,name='add-user-role'),
    path('update-user-role/', views.updateUserRole ,name='update-user-role'),
    path('delete-user-role/', views.deleteUserRole ,name='delete-user-role'),

    path('list-user/', views.listUsers ,name='list-user'),
    path('add-user/', views.addNewUser ,name='add-user'),
    path('update-user/', views.updateUser ,name='update-user'),
    path('delete-user/', views.deleteUser ,name='delete-user'),

    path('list-accounting-group/', views.listAccountingGroup ,name='list-accounting-group'),
    path('add-accounting-group/', views.addNewAccountingGroup ,name='add-accounting-group'),
    path('update-accounting-group/', views.updateAccountingGroup ,name='update-accounting-group'),
    path('delete-accounting-group/', views.deleteAccountingGroup ,name='delete-accounting-group'),

    path('list-accounting-ledger/', views.listAccountingLedger ,name='list-accounting-ledger'),
    path('add-accounting-ledger/', views.addNewAccountingLedger ,name='add-accounting-ledger'),
    path('update-accounting-ledger/', views.updateAccountingLedger ,name='update-accounting-ledger'),
    path('delete-accounting-ledger/', views.deleteAccountingLedger ,name='delete-accounting-ledger'),

    path('list-financial-year/', views.listFinancialYear ,name='list-financial-year'),
    path('add-financial-year/', views.addNewFinancialYear ,name='add-financial-year'),
    path('update-financial-year/', views.updateFinancialYear ,name='update-financial-year'),
    path('delete-financial-year/', views.deleteFinancialYear ,name='delete-financial-year'),


    path('list-series/', views.listSeries ,name='list-series'),
    path('add-series/', views.addNewSeries ,name='add-series'),
    path('update-series/', views.updateSeries ,name='update-series'),
    path('delete-series/', views.deleteSeries ,name='delete-series'),


    path('list-customer-type/', views.listCustomerType ,name='list-customer-type'),
    path('add-customer-type/', views.addNewCustomerType ,name='add-customer-type'),
    path('update-customer-type/', views.updateCustomerType ,name='update-customer-type'),
    path('delete-customer-type/', views.deleteCustomerType ,name='delete-customer-type'),


    path('list-location/', views.listLocation ,name='list-location'),
    path('add-location/', views.addNewLocation ,name='add-location'),
    path('update-location/', views.updateLocation ,name='update-location'),
    path('delete-location/', views.deleteLocation ,name='delete-location'),


    path('list-customer/', views.listCustomer ,name='list-customer'),
    path('add-customer/', views.addNewCustomer ,name='add-customer'),
    path('update-customer/', views.updateCustomer ,name='update-customer'),
    path('delete-customer/', views.deleteCustomer ,name='delete-customer'),

    path('list-supplier-type/', views.listSupplierType ,name='list-supplier-type'),
    path('add-supplier-type/', views.addNewSupplierType ,name='add-supplier-type'),
    path('update-supplier-type/', views.updateSupplierType ,name='update-supplier-type'),
    path('delete-supplier-type/', views.deleteSupplierType ,name='delete-supplier-type'),


    path('list-supplier/', views.listSupplier ,name='list-supplier'),
    path('add-supplier/', views.addNewSupplier ,name='add-supplier'),
    path('update-supplier/', views.updateSupplier ,name='update-supplier'),
    path('delete-supplier/', views.deleteSupplier ,name='delete-supplier'),


    path('list-unit/', views.listUnit ,name='list-unit'),
    path('add-unit/', views.addNewUnit ,name='add-unit'),
    path('update-unit/', views.updateUnit ,name='update-unit'),
    path('delete-unit/', views.deleteUnit ,name='delete-unit'),

    path('list-size/', views.listSize ,name='list-size'),
    path('add-size/', views.addNewSize ,name='add-size'),
    path('update-size/', views.updateSize ,name='update-size'),
    path('delete-size/', views.deleteSize ,name='delete-size'),


    path('list-brand/', views.listBrand ,name='list-brand'),
    path('add-brand/', views.addNewBrand ,name='add-brand'),
    path('update-brand/', views.updateBrand ,name='update-brand'),
    path('delete-brand/', views.deleteBrand ,name='delete-brand'),


    path('list-model-number/', views.listModelNumber ,name='list-model-number'),
    path('add-model-number/', views.addNewModelNumber ,name='add-model-number'),
    path('update-model-number/', views.updateModelNumber ,name='update-model-number'),
    path('delete-model-number/', views.deleteModelNumber ,name='delete-model-number'),


    path('list-godown/', views.listGodown ,name='list-godown'),
    path('add-godown/', views.addNewGodown ,name='add-godown'),
    path('update-godown/', views.updateGodown ,name='update-godown'),
    path('delete-godown/', views.deleteGodown ,name='delete-godown'),


    path('list-rack/', views.listRack ,name='list-rack'),
    path('add-rack/', views.addNewRack ,name='add-rack'),
    path('update-rack/', views.updateRack ,name='update-rack'),
    path('delete-rack/', views.deleteRack ,name='delete-rack'),


    path('list-product-group/', views.listProductGroup ,name='list-product-group'),
    path('add-product-group/', views.addNewProductGroup ,name='add-product-group'),
    path('update-product-group/', views.updateProductGroup ,name='update-product-group'),
    path('delete-product-group/', views.deleteProductGroup ,name='delete-product-group'),


    path('list-pricing-level/', views.listPricingLevel ,name='list-pricing-level'),
    path('add-pricing-level/', views.addNewPricingLevel ,name='add-pricing-level'),
    path('update-pricing-level/', views.updatePricingLevel ,name='update-pricing-level'),
    path('delete-pricing-level/', views.deletePricingLevel ,name='delete-pricing-level'),


    path('list-tax-data/', views.listTaxData ,name='list-tax-data'),
    path('add-tax-data/', views.addNewTaxData ,name='add-tax-data'),
    path('update-tax-data/', views.updateTaxData ,name='update-tax-data'),
    path('delete-tax-data/', views.deleteTaxData ,name='delete-tax-data'),


    path('list-product/', views.listProducts ,name='list-product'),
    path('add-product/', views.addNewProduct ,name='add-product'),
    path('update-product/', views.updateProduct ,name='update-product'),
    path('delete-product/', views.deleteProduct ,name='delete-product'),


    path('list-voucher-type/', views.listVoucherType ,name='list-voucher-type'),
    path('add-voucher-type/', views.addNewVoucherType ,name='add-voucher-type'),
    path('update-voucher-type/', views.updateVoucherType ,name='update-voucher-type'),
    path('delete-voucher-type/', views.deleteVoucherType ,name='delete-voucher-type'),
    path('get-godowns/', views.get_godowns, name='get_godowns'),
    
]    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)