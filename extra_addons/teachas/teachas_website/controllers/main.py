from odoo import fields, http
from odoo.http import request

class TeachasController(http.Controller):

      @http.route('/dashboard', type='http',auth="public", website=True)
      def dashboard(self):
            user_id=request.env['res.users'].browse(http.request.env.context.get('uid'))
            sessions=request.env['teachas'].sudo().search(['|', ('elev.id', '=', user_id.id), ('mentor.id', '=', user_id.id)])
            return http.request.render('teachas_website.dashboard',{
               'sessions':sessions
            })
