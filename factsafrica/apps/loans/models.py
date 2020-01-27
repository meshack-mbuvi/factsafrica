from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name


class LoanSpecifications(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE, related_name = 'loandetails')
    limit = models.DecimalField(max_digits = 30, default = 0.0, decimal_places = 2)
    interest_rate = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str_(self):
        return str(self.limit)


class Loan(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE, related_name = 'loans')
    amount_requested = models.DecimalField(
        default = 0, decimal_places = 2, max_digits = 30)
    accrued_interest = models.DecimalField(
        default = 0, decimal_places = 2, max_digits = 30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount_requested)


