from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Customer. See timeline below for details'),
		'fieldname': 'installed_at',
		'transactions': [
			{
				'items': ['Equipment']
			}
		]
	}