odoo.define('teachas_website.dashboard',function(require){
"use strict";

      const PublicWidget=require('web.public.widget');

      var Dashboard = PublicWidget.Widget.extend({
            selector:'#session_table',
            events: {
                  'click .session_done_input': '_onInput',
            },
            start:function() {
                  console.log('OKAY IT WORKS SOO')
                  $('.session_done_input').each(function(){
                        var test = localStorage.getItem( $(this).attr('id')) === 'true'? true: false;
                        $(this).prop('checked', test || false);
                  });
                  
            },

            _onInput:function(e){
                  var self=this;

                  var checkbox_value=$(e.target).is(':checked');
                  var parent_id=$(e.target).parent().parent().data('value');

                  localStorage.setItem($(e.target).attr('id'),checkbox_value);

                  console.log('EVENT '+checkbox_value);

                  // self._rpc({
                  //       model: "teachas",
                  //       method: "change_validity",
                  //       args:[checkbox_value, parent_id],
                  // });

                  self._rpc({
                        route:'/check_user/check_validity',
                        params:{
                              checkbox_value:checkbox_value, 
                              parent_id:parent_id,
                        },
                  });

            },
      });
      PublicWidget.registry.dashboard=Dashboard;
      return Dashboard;
      
});