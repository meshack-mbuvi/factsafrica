from .models import Customer, LoanSpecifications, Loan
from celery import shared_task

@shared_task())
def do(self):
    customers = Customer.objects.all()

    # get all loans and calculate interest for them
    for customer in customers:
        loan = Loan.objects.filter(customer = customer).order_by('-id')[0]
        interest_rate = LoanSpecifications.objects.filter(customer=customer)[0].interest_rate
        interest = int(loan.amount_requested) * interest_rate/100

        # create new record
        new_loan = Loan(customer = customer, amount_requested = loan.amount_requested,  accrued_interest = interest)
        new_loan.save()
