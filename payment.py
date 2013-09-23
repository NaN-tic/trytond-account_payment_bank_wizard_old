#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.

from trytond.pool import Pool, PoolMeta

__all__ = ['CreatePayments']

__metaclass__ = PoolMeta


class CreatePayments:
    'Create Payments'
    __name__ = 'account.payment.create'

    def get_payment_values(self, line):
        vals = super(CreatePayments, self).get_payment_values(line)
        if line.bank_account:
            vals['bank_account'] = line.bank_account
        elif vals['party'] and vals['kind']:
            party = vals['party']
            if self.kind and party:
                Party = Pool().get('party.party')
                default_bank_account = getattr(Party,
                    'get_' + self.kind + '_bank_account')
                vals['bank_account'] = default_bank_account(party).id
        return vals
