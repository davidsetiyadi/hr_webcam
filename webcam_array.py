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
	def _get_image(self, cr, uid, ids, name, args, context=None):
		attachment_field = 'image_id'
		result = dict.fromkeys(ids, False)
		for obj in self.browse(cr, uid, ids, context=context):
			# print obj.employee_id.image,'image',obj.employee_id
			result[obj.id] = {
				'image': obj.employee_id.image,
			}
		return result
	_columns = {
			'name' : fields.char('Name'),
			'employee_id':fields.many2one('hr.employee','Employee'),
			'array': fields.text('Array'),
			'image': fields.function(_get_image,type="binary",string="Image",multi="_get_image")
			}
			#dibuat image onchange ke employee_id