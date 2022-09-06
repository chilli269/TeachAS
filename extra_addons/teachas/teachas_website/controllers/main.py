from odoo import fields, http
from odoo.http import request

class TeachasController(http.Controller):

      @http.route('/dashboard', type='http',auth="public", website=True)
      def dashboard(self):

            current_uid=http.request.env.context.get('uid')
            contact=request.env['res.user'].browse(current_uid)
            
            return http.request.render('teachas_website.dashboard',{
               'type':contact.contact_type   
            })
