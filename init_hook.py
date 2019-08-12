# -*- coding: utf-8 -*-
# © 2019 yasmany Castillo <yasmany003@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    """
    The objective of this hook is to speed up the installation
    of the module on an existing Odoo instance.
    Without this script, if a database has a few hundred thousand
    invoices, which is not unlikely, the update will take
    at least a few hours.
    The pre init script only writes 0 in the each field
    so that it is not computed by the install.
    The post init script sets the value of maturity_residual.
    """
    # delete_field_advance_itbis(cr)
    # delete_field_selective_tax(cr)
    # delete_field_cost_itbis(cr)
    # delete_field_good_total_amount(cr)
    # delete_field_income_withholding(cr)
    # delete_field_invoiced_itbis(cr)
    # delete_field_isr_withholding_type(cr)
    # delete_field_legal_tip(cr)
    # delete_field_payment_date(cr)
    # delete_field_withholded_itbis(cr)
    # delete_field_third_withheld_itbis(cr)
    # delete_field_is_exterior(cr)
    # delete_field_third_income_withholding(cr)
    # delete_field_service_total_amount(cr)
    # delete_field_other_taxes(cr)
    # delete_field_withholded_itbis(cr)
    set_computed_fields(cr)
    return True


def delete_field_payment_date(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='payment_date';""")
    payment_date = cr.fetchall()
    if payment_date:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='payment_date';""")
        cr.commit()
    logger.info('Delete field payment_date')


def delete_field_service_total_amount(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='service_total_amount';""")
    service_total_amount = cr.fetchall()
    if service_total_amount:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='service_total_amount';""")
        cr.commit()
        logger.info('Delete field service_total_amount')


def delete_field_good_total_amount(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='good_total_amount';""")
    good_total_amount = cr.fetchall()
    if good_total_amount:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='good_total_amount';""")
        cr.commit()
        logger.info('Delete field good_total_amount')


def delete_field_invoiced_itbis(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='invoiced_itbis';""")
    invoiced_itbis = cr.fetchall()
    if invoiced_itbis:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='invoiced_itbis';""")
        cr.commit()
        logger.info('Delete field invoiced_itbis')


def delete_field_withholded_itbis(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='withholded_itbis';""")
    withholded_itbis = cr.fetchall()
    if withholded_itbis:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='withholded_itbis';""")
        cr.commit()
        logger.info('Delete field withholded_itbis')


def delete_field_proportionality_tax(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='proportionality_tax';""")
    proportionality_tax = cr.fetchall()
    if proportionality_tax:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='proportionality_tax';""")
        cr.commit()
        logger.info('Delete field proportionality_tax')


def delete_field_cost_itbis(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='cost_itbis';""")
    cost_itbis = cr.fetchall()
    if cost_itbis:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='cost_itbis';""")
        cr.commit()
        logger.info('Delete field cost_itbis')


def delete_field_advance_itbis(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='advance_itbis';""")
    advance_itbis = cr.fetchall()
    if advance_itbis:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='advance_itbis';""")
        cr.commit()
        logger.info('Delete field advance_itbis')


def delete_field_isr_withholding_type(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='isr_withholding_type';""")
    isr_withholding_type = cr.fetchall()
    if isr_withholding_type:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='isr_withholding_type';""")
        cr.commit()
        logger.info('Delete field isr_withholding_type')


def delete_field_income_withholding(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='income_withholding';""")
    income_withholding = cr.fetchall()
    if income_withholding:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='income_withholding';""")
        cr.commit()
        logger.info('Delete field income_withholding')


def delete_field_selective_tax(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='selective_tax';""")
    selective_tax = cr.fetchall()
    if selective_tax:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='selective_tax';""")
        cr.commit()
        logger.info('Delete field selective_tax')


def delete_field_other_taxes(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='other_taxes';""")
    other_taxes = cr.fetchall()
    if other_taxes:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='other_taxes';""")
        cr.commit()
        logger.info('Delete field other_taxes')


def delete_field_legal_tip(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='legal_tip';""")
    legal_tip = cr.fetchall()
    if legal_tip:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='legal_tip';""")
        cr.commit()
        logger.info('Delete field legal_tip')


def delete_field_third_withheld_itbis(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='third_withheld_itbis';""")
    third_withheld_itbis = cr.fetchall()
    if third_withheld_itbis:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='third_withheld_itbis';""")
        cr.commit()
        logger.info('Delete field third_withheld_itbis')


def delete_field_third_income_withholding(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='third_income_withholding';""")
    third_income_withholding = cr.fetchall()
    if third_income_withholding:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='third_income_withholding';""")
        cr.commit()
        logger.info('Delete field third_income_withholding')


def delete_field_is_exterior(cr):
    # Delete payment_date field
    cr.execute("""SELECT 1 FROM ir_model_fields 
    WHERE model = 'account.invoice' and name='is_exterior';""")
    is_exterior = cr.fetchall()
    if is_exterior:
        cr.execute("""DELETE FROM ir_model_fields 
        WHERE model='account.invoice' and name='is_exterior';""")
        cr.commit()
        logger.info('Delete field is_exterior')


def set_computed_fields(cr):
    store_field_payment_date(cr)
    store_field_service_total_amount(cr)
    store_field_good_total_amount(cr)
    store_field_invoiced_itbis(cr)
    store_field_withholded_itbis(cr)
    store_field_proportionality_tax(cr)
    store_field_cost_itbis(cr)
    store_field_advance_itbis(cr)
    store_field_isr_withholding_type(cr)
    store_field_income_withholding(cr)
    store_field_selective_tax(cr)
    store_field_legal_tip(cr)
    store_field_third_withheld_itbis(cr)
    store_field_third_income_withholding(cr)
    store_field_is_exterior(cr)

    return True


def store_field_payment_date(cr):
    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='payment_date'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN payment_date date;
            COMMENT ON COLUMN account_invoice.payment_date IS 'Payment date';
            """)

    logger.info('Computing field payment_date on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET payment_date = NULL;
        """
    )
    cr.commit()


def store_field_service_total_amount(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='service_total_amount'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN service_total_amount float;
            COMMENT ON COLUMN account_invoice.service_total_amount IS 'Service Total Amount';
            """)

    logger.info('Computing field service_total_amount on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET service_total_amount = 0.0;
        """
    )
    cr.commit()


def store_field_good_total_amount(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='good_total_amount'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN good_total_amount float;
            COMMENT ON COLUMN account_invoice.good_total_amount IS 'Good Total Amount';
            """)

    logger.info('Computing field good_total_amount on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET good_total_amount = 0.0;
        """
    )
    cr.commit()


def store_field_invoiced_itbis(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='invoiced_itbis'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN invoiced_itbis float;
            COMMENT ON COLUMN account_invoice.invoiced_itbis IS 'Invoiced ITBIS';
            """)

    logger.info('Computing field invoiced_itbis on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET invoiced_itbis = 0.0;
        """
    )
    cr.commit()


def store_field_withholded_itbis(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='withholded_itbis'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN withholded_itbis float;
            COMMENT ON COLUMN account_invoice.withholded_itbis IS 'Withheld ITBIS';
            """)

    logger.info('Computing field withholded_itbis on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET withholded_itbis = 0.0;
        """
    )
    cr.commit()


def store_field_proportionality_tax(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='proportionality_tax'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN proportionality_tax float;
            COMMENT ON COLUMN account_invoice.proportionality_tax IS 'Proportionality Tax';
            """)

    logger.info('Computing field proportionality_tax on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET proportionality_tax = 0.0;
        """
    )
    cr.commit()


def store_field_cost_itbis(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='cost_itbis'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN cost_itbis float;
            COMMENT ON COLUMN account_invoice.cost_itbis IS 'Cost Itbis';
            """)

    logger.info('Computing field cost_itbis on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET cost_itbis = 0.0;
        """
    )
    cr.commit()


def store_field_advance_itbis(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='advance_itbis'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN advance_itbis float;
            COMMENT ON COLUMN account_invoice.advance_itbis IS 'Advanced ITBIS';
            """)

    logger.info('Computing field advance_itbis on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET advance_itbis = 0.0;
        """
    )
    cr.commit()


def store_field_isr_withholding_type(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='isr_withholding_type'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN isr_withholding_type float;
            COMMENT ON COLUMN account_invoice.isr_withholding_type IS 'ISR Withholding Type';
            """)

    logger.info('Computing field isr_withholding_type on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET isr_withholding_type = 0.0;
        """
    )
    cr.commit()


def store_field_income_withholding(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='income_withholding'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN income_withholding float;
            COMMENT ON COLUMN account_invoice.income_withholding IS 'Income Withholding';
            """)

    logger.info('Computing field income_withholding on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET income_withholding = 0.0;
        """
    )
    cr.commit()


def store_field_selective_tax(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='selective_tax'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN selective_tax float;
            COMMENT ON COLUMN account_invoice.selective_tax IS 'Selective Tax';
            """)

    logger.info('Computing field selective_tax on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET selective_tax = 0.0;
        """
    )
    cr.commit()


def store_field_legal_tip(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='legal_tip'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN legal_tip float;
            COMMENT ON COLUMN account_invoice.legal_tip IS 'Legal tip amount';
            """)

    logger.info('Computing field legal_tip on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET legal_tip = 0.0;
        """
    )
    cr.commit()


def store_field_third_withheld_itbis(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='third_withheld_itbis'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN third_withheld_itbis float;
            COMMENT ON COLUMN account_invoice.third_withheld_itbis IS 'Withheld ITBIS by a third';
            """)

    logger.info('Computing field third_withheld_itbis on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET third_withheld_itbis = 0.0;
        """
    )
    cr.commit()


def store_field_third_income_withholding(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='third_income_withholding'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN third_income_withholding float;
            COMMENT ON COLUMN account_invoice.third_income_withholding IS 'Income Withholding by a third';
            """)

    logger.info('Computing field third_income_withholding on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET third_income_withholding = 0.0;
        """
    )
    cr.commit()


def store_field_is_exterior(cr):

    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_invoice' AND
    column_name='is_exterior'""")
    if not cr.fetchone():
        cr.execute(
            """
            ALTER TABLE account_invoice ADD COLUMN is_exterior float;
            COMMENT ON COLUMN account_invoice.is_exterior IS 'Is exterior';
            """)

    logger.info('Computing field is_exterior on account.invoice')

    cr.execute(
        """
        UPDATE account_invoice SET is_exterior = False;
        """
    )
    cr.commit()







