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


      @http.route('/schedule-meeting', type='http', auth='public', website=True)
      def schedule_meeting(self):
            return http.request.render('teachas_website.schedule_meeting')

      @http.route(['/schedule-meeting/submit'], type='http', auth="public", website=True)
      def customer_form_submit(self, **post):
            partner = request.env['teachas'].sudo().create({
                  'time_length': post.get('time_length'),
            })
            vals = {
                  'partner': partner,
            }
            return request.render("teachas_website.schedule_meeting_success", vals)
