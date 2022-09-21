odoo.define('teachas_website.interactive_sessions_snippet',function(require){

      const PublicWidget=require('web.public.widget');
      var rpc = require('web.rpc');

      // const DynamicSnippetCarousel=require('website.s_dynamic_snippet_carousel');

      var Dynamic = PublicWidget.Widget.extend({
            selector:'.js_interactive_sessions_snippet',
            start:function() {
                  var self=this;
                  rpc.query({
                        route:'/custom_snippets/total_interactive_sessions',
                  }).then(function(result){
                        console.log(result);
                        self.$el.find('#find_me_please').append(...$(result));
                  });
            },
      });
      PublicWidget.registry.js_interactive_sessions_snippet=Dynamic;
      return Dynamic;
});
