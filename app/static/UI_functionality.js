    $(document).ready(function(){
                  $('.user-profile').click(function() {
                      if(!$(this).hasClass('active')){
                          
                          $('.user-profile.active').removeClass('active');
                          $(this).addClass('active');
                          
                          var temp =   $('#'+$(this).attr('data-up'));
                          
                          hideUI('.chat-container')
                          showUI('#'+$(this).attr('data-up'));
                          temp.addClass('active').removeClass('hidechat');
                          temp.prevAll('.chat-container').addClass('hidechat').removeClass('active');
                          temp.nextAll('.chat-container').removeClass('active').removeClass('hidechat');
                      }
                  });
            showUI('#cont1');
        });
        
        function showUI(ele){
            console.log($(ele));
            var kids = $(ele).children(), temp;
            for( var i = kids.length-1 ; i >=0  ; i-- ){
                temp  = $(kids[i]);
                
                if(temp.is('div')){
                    temp.animate({
                        marginTop:0,
                    },400).css({opacity:1}).fadeIn()
                }
                else{
                    temp.css({opacity:1}).fadeIn()
                }   
            }
        }
        
         function hideUI(ele){
            console.log($(ele));
            var kids = $(ele).children(), temp;
            for( var i = kids.length-1 ; i >=0  ; i-- ){
                temp  = $(kids[i]);
                
                if(temp.is('div')){
                    temp.animate({
                        marginTop:'30px',
                    }).css({opacity:0});
                }
                else{
                    temp.css({opacity:0});
                }   
            }
        }