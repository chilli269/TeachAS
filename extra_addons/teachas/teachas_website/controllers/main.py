
from odoo import fields, http
from odoo.http import request



from odoo.addons.web.controllers import main

import logging
_logger = logging.getLogger(__name__)

class TeachasController(http.Controller):

    @http.route('/dashboard', type='http', auth="public", website=True)
    def dashboard(self):
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        sessions = request.env['teachas'].sudo().search(
            ['|', ('elev.id', '=', user_id.id), ('mentor.id', '=', user_id.id)])
        return http.request.render('teachas_website.dashboard', {
            'sessions': sessions,
        })

    @http.route('/schedule-meeting', type='http', auth='public', website=True)
    def schedule_meeting(self):
        subjects = request.env['teachas.subjects'].sudo().search([])
        days = request.env['teachas.days'].sudo().search([])
        return http.request.render('teachas_website.schedule_meeting', {
            'subjects': subjects,
            'days': days
        })

    @http.route(['/schedule-meeting/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid')).id
        mentors = request.env['res.users'].search([('materie.id', '=', post.get('subject'))])
        _logger.info('\n\n sdasdasdasdas %s\n\n', mentors[2].preferred_days)
        _logger.info('\n\n sdasdasdasdas %s\n\n', post.get('preferred_day'))
        partner = request.env['teachas'].sudo().create({
            'time_length': post.get('time_length'),
            'materie': post.get('subject'),
            'data': post.get('date'),
            'session_type': post.get('session_type'),
            'elev': user_id,
            'details': post.get('details'),
            # 'mentor': mentors[0].id
        })
        vals = {
            'partner': partner,
        }
        return request.render("teachas_website.schedule_meeting_success", vals)
    
      # @http.route('/', type='http', auth='none')
      # def index(self):
      #       int_sessions=request.env['teachas'].search([('is_session','=',True)])
      #       return int_sessions

    @http.route(['/custom_snippets/total_interactive_sessions'],type='json',auth='public', website=True)
    def interactive_sessions(self):

        data=request.env['teachas'].search([('is_session','=',True)])
        if data:
            return request.env['ir.ui.view']._render_template('teachas_website.interactive_sessions_card',{
                'data':data
            })
        else: return request.env['ir.ui.view']._render_template('teachas_website.session_empty')


