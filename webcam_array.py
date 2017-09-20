import logging
import time

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

import openerp.addons.decimal_precision as dp
import openerp.addons.product.product
import datetime
import dateutil.relativedelta
from openerp.osv import osv
class webcam_array(osv.osv):
	_name = 'webcam.array'
	_columns = {
			'name': fields.text('Array'),
			}