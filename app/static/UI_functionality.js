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
                          temp.nextAll('.chat-container').removeClass('active').addClass('hidechat');
                      }
                  });
            showUI('#cont1');
            showUI('#editor1');
            
                    
                    $('.script-editor').click(function() {
                        
                            $('.editor-input').hide();
                            $('.script-editor.active').removeClass('active');
                            
                            $('#'+$(this).attr('data-up')).show();
                            $(this).addClass('active');
                        /*
                      if(!$(this).hasClass('active')){
                
                      $('.script-editor.active').removeClass('active');
                      $(this).addClass('active');
                      
                      var temp =   $('#'+$(this).attr('data-up'));
                      
                      hideUI('.editor-input')
                      showUI('#'+$(this).attr('data-up'));
                      temp.addClass('active').removeClass('hidechat');
                      temp.prevAll('.editor-input').addClass('hidechat').removeClass('active');
                      temp.nextAll('.editor-input').removeClass('active').addClass('hidechat');*/
        });
        
    CodeMirror.fromTextArea(document.getElementById("editor1-textarea"), {
            mode: {name: "stex",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: false,
            indentUnit: 4,
            matchBrackets: true
        });
        
    CodeMirror.fromTextArea(document.getElementById("editor2-textarea"), {
            mode: {name: "python",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: true,
            indentUnit: 4,
            matchBrackets: true
        });
        
    CodeMirror.fromTextArea(document.getElementById("editor3-textarea"), {
            mode: {name: "r",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: true,
            indentUnit: 4,
            matchBrackets: true
        });

             $('.editor-input').hide();
            $('#editor1').show();
                     
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
