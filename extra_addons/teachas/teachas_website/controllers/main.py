from odoo import fields, http
from odoo.http import request

# from odoo.addons.web.controllers import main

from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class TeachasController(http.Controller):

    @http.route('/dashboard', type='http', auth="public", website=True)
    def dashboard(self):
        if request.env.user.id == request.env.ref('base.public_user').id:
            return request.redirect('/web/login')
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        _logger.info("\n\n user_type %s", user_id)
        _logger.info("\n\n user_type %s", user_id.contact_type)
        if not user_id.phone_number or not user_id.grade_id:
            return http.request.render('teachas_website.finish_profile', {
                'user': user_id,
            })
        sessions = request.env['teachas'].sudo().search(['|', ('elev.id', '=', user_id.id),
                                                         ('mentor.id', '=', user_id.id),('stage_id','=','ongoing')])
                                    
        archived_sessions = request.env['teachas'].sudo().search(['|', ('elev.id', '=', user_id.id),
                                                         ('mentor.id', '=', user_id.id),('stage_id','=','done')])
        if user_id.contact_type == 'mentor':
            mentor = 1
        else:
            mentor = 0
        if user_id.contact_type == 'elev':
            elev = 1
        else:
            elev = 0
        return http.request.render('teachas_website.dashboard', {
            'sessions': sessions,
            'archived_sessions':archived_sessions,
            'mentor': mentor,
            'elev': elev
        })

    @http.route(['/custom_snippets/interactive_sessions'], type='json', auth='public', website=True)
    def interactive_sessions_(self):

        data = request.env['teachas'].search([('is_session', '=', True)])
        if data:
            return request.env['ir.ui.view']._render_template('teachas_website.interactive_sessions_card', {
                'data': data
            })
        else:
            return request.env['ir.ui.view']._render_template('teachas_website.session_empty')

    @http.route('/finish_profile/submit', type="http", auth="user", website=True)
    def _teachas_add_phone_number(self, **post):
        if post.get("phone_number") and post.get("grade_id"):
            finish_profile = request.env['res.users'].browse(http.request.env.context.get('uid')).sudo().write({
                'phone_number': post.get('phone_number'),
                'grade_id': str(post.get('grade_id'))
            })
        elif post.get("phone_number"):
            finish_profile = request.env['res.users'].browse(http.request.env.context.get('uid')).sudo().write({
                'phone_number': post.get('phone_number'),
            })
        elif post.get("grade_id"):
            finish_profile = request.env['res.users'].browse(http.request.env.context.get('uid')).sudo().write({
                'grade_id': str(post.get('grade_id')),
            })
        vals = {
            'phone_number': finish_profile
        }
        return request.render('teachas_website.profile_finished', vals)

#     @http.route('/finish_profile/submit', type="http", auth="user", website=True)
#     def _teachas_add_checkbox(self, **post):
#         user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
#         if (post.get('session_done')):
#             if user_id.contact_type == 'elev':

#         return request.redirect('/dashboard')

    @http.route('/schedule-meeting', type='http', auth='public', website=True)
    def schedule_meeting(self):
        if request.env.user.id == request.env.ref('base.public_user').id:
            return request.redirect('/web/login')
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        if not user_id.phone_number or not user_id.grade_id:
            return http.request.render('teachas_website.finish_profile', {
                'user': user_id,
            })
        subjects = request.env['teachas.subjects'].sudo().search([])
        days = request.env['teachas.days'].sudo().search([])
        return http.request.render('teachas_website.schedule_meeting', {
            'subjects': subjects,
            'days': days
        })

    @http.route(['/schedule-meeting/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        user_id = request.env['res.users'].sudo().browse(http.request.env.context.get('uid'))
        mentors2 = request.env['res.users'].sudo().search(
            [('materie.id', '=', post.get('subject')), ('grade_id', '>=', user_id.grade_id)])
        _logger.info('\n\n nu mai pot %s \n\n',type(user_id.grade_id))
        # _logger.info('\n\n sdasdasdasdas %s\n\n', mentors[2].preferred_days)
        # _logger.info('\n\n sdasdasdasdas %s\n\n', post.get('preferred_day'))
        _logger.info('\n\n DATA %s\n\n', mentors2)
        _logger.info('\n\n DATA2 %s\n\n', user_id)
        mentors2 = mentors2.filtered(lambda m: m.id != user_id.id)
        _logger.info('\n\n DATA3 %s\n\n', mentors2)
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
        _logger.info('\n\n time %s \n\n',time_id)

        if post.get('preferred_day')=='ASAP' and mentors2:

            _logger.info('\n\n HAlelUjAHhHh \n\n')
            days=request.env['teachas.days'].search([])
            index=datetime.today().weekday()+1
            if index>6:
                index=0

            ok=True
            index_aux=index-1
            if index_aux<0:
                index_aux=6
            while ok:
                mentors=mentors2
                _logger.info('\n\n passed \n\n',)
                if index==index_aux:
                    ok=False
                if index>6:
                    index=0
                
                aux=[]
                for rec in mentors:
                    _logger.info('\n\n ISaD %s \n\n',index)
                    _logger.info('\n\n INDeX %s \n\n',days[index].name)
                    # _logger.info('\n\n type INDeX %s \n\n',type(days[index].id))
                    # # _logger.info('\n\n grade  %s \n\n',rec.grade_id)
                    # _logger.info('\n\n rec.preferred_days.ids %s \n\n',rec.preferred_days.ids)
                    # _logger.info('\n\n type rec.preferred_days.ids %s \n\n',type(rec.preferred_days.ids[0]))
                    if days[index].id in rec.preferred_days.ids:
                        aux.append(rec.id)
                _logger.info('\n\n AUX %s \n\n',aux)
                if aux:
                    mentors = mentors.filtered(lambda r: r.id in aux)
                    _logger.info('\n\n 1 %s \n\n',mentors)

                    if mentors:
                        aux = []
                        for rec in mentors:
                            if rec.available_hours - time_id >= 0:
                                aux.append(rec.id)
                        if aux:
                            mentors = mentors.filtered(lambda r: r.id in aux)
                            _logger.info('\n\n 2 %s \n\n',mentors)
                            
                            if mentors:
                                mentors = mentors.sorted(key=lambda r: r.exp_points)
                                partner = request.env['teachas'].sudo().create({
                                    'time_length': post.get('time_length'),
                                    'materie': int(post.get('subject')),
                                    'data': days[index].id,
                                    'session_type': post.get('session_type'),
                                    'elev': user_id.id,
                                    'details': post.get('details'),
                                    'mentor': mentors[0].id
                                })

                                _logger.info('\n\n 3 %s \n\n',mentors)
                                _logger.info('\n\n 3 %s \n\n',partner.mentor.name)

                                mentors[0].available_hours -= time_id # remove hours from available time
                                mentors[0].auxiliary_hours += time_id  
                                mentors[0].exp_points += 8 * time_id
                                vals = {
                                    'partner': partner,
                                }
                                return request.render("teachas_website.schedule_meeting_success", vals)
                            else:
                                index+=1
                        else:
                            index+=1
                    else:
                        index+=1
                else:
                    index+=1
            return request.render("teachas_website.schedule_meeting_fail")
        else:
            if mentors2:
                _logger.info('\n\n Mentors %s \n\n', mentors2)
                aux = []
                mentors=mentors2
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

                    partner = request.env['teachas'].sudo().create({
                        'time_length': post.get('time_length'),
                        'materie': int(post.get('subject')),
                        'data': int(post.get('preferred_day')),
                        'session_type': post.get('session_type'),
                        'elev': user_id.id,
                        'details': post.get('details'),
                        'mentor': mentors[0].id
                    })
                    mentors[0].available_hours -= time_id # remove hours from available time
                    mentors[0].auxiliary_hours += time_id  
                    mentors[0].exp_points += 8 * time_id
                    vals = {
                        'partner': partner,
                    }
                    return request.render("teachas_website.schedule_meeting_success", vals)
                else:
                    return request.render("teachas_website.schedule_meeting_fail")
            else:
                return request.render("teachas_website.schedule_meeting_fail")


  

    @http.route(['/check_user/check_validity'], type='json', auth='public', website=True)
    def check_validity(self,checkbox_value, parent_id):

        # user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        session_id=request.env['teachas'].browse(parent_id)

        # _logger.info('\n\n oaskdoad %s \n\n',session_id) works
        # _logger.info('\n\n asdasdad %s \n\n',user_id) works
        # _logger.info('\n\n assdad %s \n\n',type(checkbox_value)) Boolean

        if checkbox_value:
            session_id.validity_check+=1
        else:
            session_id.validity_check-=1

        if session_id.validity_check>=2:
            session_id.stage_id='done'
        else:
            session_id.stage_id='ongoing'

        return True

    @http.route(['/get_popup'], type='json', auth="public", website=True, sitemap=False, csrf=False)
    def get_popup(self, session_id, **kw):
        session = http.request.env['teachas'].sudo().browse(session_id)
        _logger.info("\n\n ha \n\n %s", session)
        user_id = request.env['res.users'].browse(http.request.env.context.get('uid'))
        if user_id.contact_type == 'mentor':
            mentor = 1
        else:
            mentor = 0
        if user_id.contact_type == 'elev':
            elev = 1
        else:
            elev = 0
        return request.env['ir.ui.view']._render_template("teachas_website.more_info_popup_template", {
            'session': session,
            'mentor':mentor,
            'elev': elev
        })
