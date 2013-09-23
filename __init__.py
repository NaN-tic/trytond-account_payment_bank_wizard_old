#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.

from trytond.pool import Pool
from .payment import *


def register():
    Pool.register(
        CreatePayments,
        module='account_payment_bank_wizard', type_='wizard')
