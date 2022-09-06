from odoo import fields, http
from odoo.http import request

class TeachasController(http.Controller):

      @http.route('/dashboard', type='http',auth="public", website=True)
      def dashboard(self):

            # current_uid=http.request.env.context.get('uid')
            user_id=request.env['res.users'].browse(http.request.env.context.get('uid'))
            print(user_id)
            sessions=request.env['teachas'].sudo().search([('elev.id', '=', user_id.id)])
            print(sessions)
            return http.request.render('teachas_website.dashboard',{
               'sessions':sessions
            })
