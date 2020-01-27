from django.contrib import admin, messages
from .models import Customer, Loan, LoanSpecifications


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Loan)
class LoansAdmin(admin.ModelAdmin):
    list_display = ('created_at','customer', 'amount_requested', 'accrued_interest')
    readonly_fields = ('created_at', )

    def message_user(self, *args):
        pass

    def save_model(self, request, obj, form, change):
        # check whether amount requested is within the limit
        limit = LoanSpecifications.objects.filter(
            customer=obj.customer)
        if(len(limit) == 0):
            messages.error(request, "Please set customer loan limit and interest rate in Loan Specifications.")
            return 


        # check whether customer has pending loan and increment it
        pending_loan = Loan.objects.filter(
            customer = obj.customer).order_by('-id')

        if(len(pending_loan) > 0):
            amount_requested = pending_loan[0].amount_requested + obj.amount_requested
        else:
            amount_requested = obj.amount_requested

        if(limit[0].limit < amount_requested):
            # Show error on the admin panel
            messages.error(request, "Requested amount is greater than allowed limit")
            return

        obj.amount_requested = amount_requested
        obj.save()
        
        


@admin.register(LoanSpecifications)
class LoanSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'limit', 'interest_rate')