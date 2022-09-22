from odoo import fields, http
from odoo.http import request

from odoo.addons.web.controllers import main

import logging

_logger = logging.getLogger(__name__)


class TeachasController(http.Controller):

    @http.route('/dashboard', type='http', auth="public", website=True)
    def dashboard(self):
        if request.env.user.id == request.env.ref('base.public_user').id:
            return request.redirect('/web/login')
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        if not user_id.phone_number:
            return http.request.render('teachas_website.add_your_phone_number')
        sessions = request.env['teachas'].sudo().search(['|', ('elev.id', '=', user_id.id),
                                                         ('mentor.id', '=', user_id.id)])
        return http.request.render('teachas_website.dashboard', {
            'sessions': sessions,
        })

    @http.route('/add_phone_number/submit', type="http", auth="user", website=True)
    def _teachas_add_phone_number(self, **post):
        add_phone_number = request.env['res.users'].browse(http.request.env.context.get('uid')).write({
            'phone_number': post.get('phone_number')
        })
        vals = {
            'phone_number': add_phone_number
        }
        return request.render('teachas_website.add_phone_success', vals)

    @http.route('/schedule-meeting', type='http', auth='public', website=True)
    def schedule_meeting(self):
        if request.env.user.id == request.env.ref('base.public_user').id:
            return request.redirect('/web/login')
        subjects = request.env['teachas.subjects'].sudo().search([])
        days = request.env['teachas.days'].sudo().search([])
        return http.request.render('teachas_website.schedule_meeting', {
            'subjects': subjects,
            'days': days
        })

    @http.route(['/schedule-meeting/submit'], type='http', auth="user", website=True)
    def _customer_form_submit(self, **post):
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid')).id
        mentors = request.env['res.users'].search([('materie.id', '=', post.get('subject'))])
        # _logger.info('\n\n sdasdasdasdas %s\n\n', mentors[2].preferred_days)
        # _logger.info('\n\n sdasdasdasdas %s\n\n', post.get('preferred_day'))
        mentor_id = None
        _logger.info('\n\n DATA %s\n\n', mentors)
        _logger.info('\n\n preffered %s\n\n', post.get('preferred_day'))
        _logger.info('\n\n subject %s\n\n', post.get('subject'))
        time_id = None
        if post.get('time_length') == 'half':
            time_id = 0.5
        if post.get('time_length') == 'hour':
            time_id = 1
        if post.get('time_length') == 'hourhalf':
            time_id = 1.5
        if post.get('time_length') == 'twohours':
            time_id = 2
        if mentors:
            # _logger.info('\n\n no id %s\n\n', mentors.preferred_days) returns res.users(1,)
            # _logger.info('\n\n id %s\n\n', mentors.preferred_days.id) return 1
            _logger.info('\n\n ids %s\n\n', mentors.preferred_days.ids)  # returns [1]
            aux = mentors.filtered(lambda r: post.get('preferred_day') in r.preferred_days.ids)
            _logger.info('\n\n AUX %s\n\n', aux)
            if aux:
                aux2 = aux = request.env['res.users'].search(
                    [('materie.id', '=', post.get('subject')), ('preferred_days.ids', '=', post.get('preferred_day')),
                     ('available_hours', '>=', time_id)])
                _logger.info('\n\n AUX2 %s\n\n', aux2)
                del aux
                if aux2:
                    aux2.sort()
                    _logger.info('\n\n aux2[0] %s\n\n', aux2[0])
                    mentor_id = aux2[0]
                    del aux2
                else:
                    return request.render("teachas_website.schedule_meeting_fail")
            else:
                return request.render("teachas_website.schedule_meeting_fail")
        else:
            return request.render("teachas_website.schedule_meeting_fail")

        partner = request.env['teachas'].sudo().create({
            'time_length': post.get('time_length'),
            'materie': post.get('subject'),
            'data': post.get('date'),
            'session_type': post.get('session_type'),
            'elev': user_id,
            'details': post.get('details'),
            'mentor': mentor_id
        })
        vals = {
            'partner': partner,
        }
        return request.render("teachas_website.schedule_meeting_success", vals)

    # TODO: to delete selected hours from mentor after meeting is created

    # @http.route('/', type='http', auth='none')
    # def index(self):
    #       int_sessions=request.env['teachas'].search([('is_session','=',True)])
    #       return int_sessions

    @http.route(['/custom_snippets/total_interactive_sessions'], type='json', auth='public', website=True)
    def interactive_sessions(self):

        data = request.env['teachas'].search([('is_session', '=', True)])
        if data:
            return request.env['ir.ui.view']._render_template('teachas_website.interactive_sessions_card', {
                'data': data
            })
        else:
            return request.env['ir.ui.view']._render_template('teachas_website.session_empty')
