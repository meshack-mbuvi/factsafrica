from django.shortcuts import render
from .apps.loans.models import Customer, LoanSpecifications, Loan
from django_cron import CronJobBase, Schedule
from django.contrib import admin, messages


def my_cron_job():
    customers = Customer.objects.all()

    # get all loans and calculate interest for them
    for customer in customers:
        loan = Loan.objects.filter(customer = customer).order_by('-id')
        
        if(not len(loan)):
            print("customer does not have a loan")
            return
        print('Calculating interest...')
        
        amount_requested = loan[0].amount_requested
        interest_rate = LoanSpecifications.objects.filter(
            customer=customer)[0].interest_rate
        
        interest = int(amount_requested) * interest_rate/100

        # create new record
        new_loan = Loan(customer = customer, amount_requested = amount_requested,  accrued_interest = interest)
        new_loan.save()