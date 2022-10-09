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
        if not user_id.phone_number or not user_id.grade_id:
            return http.request.render('teachas_website.finish_profile', {
                'user': user_id,
            })
        sessions = request.env['teachas'].sudo().search(['|', ('elev.id', '=', user_id.id),
                                                         ('mentor.id', '=', user_id.id)])
        return http.request.render('teachas_website.dashboard', {
            'sessions': sessions,
        })

    @http.route('/finish_profile/submit', type="http", auth="user", website=True)
    def _teachas_add_phone_number(self, **post):
        finish_profile = request.env['res.users'].browse(http.request.env.context.get('uid')).write({
            'phone_number': post.get('phone_number'),
            'grade_id': str(post.get('grade_id'))
        })
        vals = {
            'phone_number': finish_profile
        }
        return request.render('teachas_website.profile_finished', vals)

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

    @http.route(['/schedule-meeting/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        mentors = request.env['res.users'].search(
            [('materie.id', '=', post.get('subject')), ('grade_id', '>=', user_id.grade_id)])
        _logger.info('\n\n Comp1 %s \n\n', '8' < '9')
        _logger.info('\n\n Comp1 %s \n\n', '10' < '11')
        # _logger.info('\n\n sdasdasdasdas %s\n\n', mentors[2].preferred_days)
        # _logger.info('\n\n sdasdasdasdas %s\n\n', post.get('preferred_day'))
        # _logger.info('\n\n DATA %s\n\n', mentors)
        # _logger.info('\n\n preffered %s\n\n', post.get('preferred_day'))
        # _logger.info('\n\n subject %s\n\n', post.get('subject'))
        time_id = None
        if (post.get('time_length') == 'half'):
            time_id = 0.5
        if (post.get('time_length') == 'hour'):
            time_id = 1
        if (post.get('time_length') == 'hourhalf'):
            time_id = 1.5
        if (post.get('time_length') == 'twohours'):
            time_id = 2

        if mentors:
            _logger.info('\n\n Mentors %s \n\n', mentors)
            aux = []
            for rec in mentors:
                if int(post.get('preferred_day')) not in rec.preferred_days.ids:
                    _logger.info('\n\n post %s \n\n', post.get('preferred_day'))
                    _logger.info('\n\n prefg %s \n\n', rec.preferred_days.ids)
                    _logger.info('\n\n okay sooo %s \n\n', type(rec.preferred_days.ids))
                    _logger.info('\n\n sofro za king %s \n\n', type(rec.id))
                    aux.append(rec.id)
            # mentors2=mentors.filtered(lambda r: r.id not in aux)
            mentors = mentors.filtered(lambda r: r.id not in aux)
            # _logger.info('\n\n Mentors2 %s \n\n',mentors)
            # _logger.info('\n\n aux %s \n\n',aux)
            # _logger.info('\n\n aux %s \n\n',type(aux))
            # _logger.info('\n\n auxxxx %s \n\n',type(post.get('preferred_day'))) # returns string
            # del mentors

            if mentors:
                aux = []
                for rec in mentors:
                    if rec.available_hours - time_id < 0:
                        aux.append(rec.id)
                mentors = mentors.filtered_domain([('id', 'not in', aux)])
                _logger.info('\n\n Mentors3 %s \n\n', mentors)
                # del mentors2
            if mentors:
                mentors = mentors.sorted(key=lambda r: r.exp_points)
                _logger.info('\n\n Mentors4 %s \n\n', mentors)
            else:
                return request.render("teachas_website.schedule_meeting_fail")

        else:
            return request.render("teachas_website.schedule_meeting_fail")

        partner = request.env['teachas'].sudo().create({
            'time_length': post.get('time_length'),
            'materie': post.get('subject'),
            'data': post.get('preferred_day'),
            'session_type': post.get('session_type'),
            'elev': user_id.id,
            'details': post.get('details'),
            'mentor': mentors[0].id
        })
        mentors[0].available_hours -= time_id  # remove hours from available time
        mentors[0].exp_points += 8 * time_id
        vals = {
            'partner': partner,
        }
        return request.render("teachas_website.schedule_meeting_success", vals)

    # @http.route('/', type='http', auth='none')
    # def index(self):
    #       int_sessions=request.env['teachas'].search([('is_session','=',True)])
    #       return int_sessions

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
