odoo.define('teachas_website.schedule_meeting', function (require) {
    "use strict";

    const PublicWidget = require('web.public.widget');

    const ScheduleMeeting = PublicWidget.Widget.extend({
        selector: '.schedule_meeting',
        events: {
            'click .schedule_meeting_submit': '_onClickDisableButtonSchedule',
            'click .reschedule_meeting_submit': '_onClickDisableButtonReschedule',
        },
        start: function () {
            console.log('OKAY IT WORKS SOO')
        },
        _onClickDisableButtonSchedule: function () {
            let x = document.forms["ScheduleMeeting"]["session_type"].value;
            let z = document.forms["ScheduleMeeting"]["details"].value;
            if (x && z){
                $(".schedule_meeting_submit").hide();
            }
            console.log("mama");
        },
        _onClickDisableButtonReschedule: function () {
            let x = document.forms["RescheduleMeeting"]["session_type"].value;
            let z = document.forms["RescheduleMeeting"]["details"].value;
            if (x && z){
                $(".reschedule_meeting_submit").hide();
            }
            console.log("mama");
        }
    });
    PublicWidget.registry.schedule_meeting = ScheduleMeeting;
    return ScheduleMeeting;

});