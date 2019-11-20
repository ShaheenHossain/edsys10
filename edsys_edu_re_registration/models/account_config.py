import time
import datetime
from dateutil.relativedelta import relativedelta

import eagle
from eagle import SUPERUSER_ID
from eagle.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from eagle.tools.translate import _
# from openerp.osv import fields, osv
from eagle import models, fields, api, _

class account_config_settings(models.TransientModel):
    _inherit = 'account.config.settings'
    
    amount_configurable = fields.Float('Amount Configurable')





    # def get_default_config_value(self, cr, uid, ids, context=None):
    #     param_obj = self.pool.get("ir.config_parameter")
    #     res = {'amount_configurable': float(param_obj.get_param(cr, uid, 'amount_configurable'))
    #          }
    #     return res


    # def set_config_value(self, cr, uid, ids, context=None):
    #     param_obj = self.pool.get("ir.config_parameter")
    #     for record in self.browse(cr, uid, ids, context=context):
    #         param_obj.set_param(cr, uid,'amount_configurable',record['amount_configurable'] or '0')






