var MyProject = {};

    $(document).ready(function(){
                  $('.user-profile').click(function() {
                      
                            $('.chat-container').hide();
                            $('.user-profile.active').removeClass('active');
                            
                            $('#'+$(this).attr('data-up')).show();
                            $(this).addClass('active');
                      
                      /*

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
                      */
                  });
            
            //showUI('#cont1');
            //showUI('#editor1');
            
                    
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
        
    var cmeditor1 = CodeMirror.fromTextArea(document.getElementById("editor1-textarea"), {
            mode: {name: "stex",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: false,
            indentUnit: 4,
            matchBrackets: true
        });
        
    var cmeditor2 = CodeMirror.fromTextArea(document.getElementById("editor2-textarea"), {
            mode: {name: "python",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: true,
            indentUnit: 4,
            matchBrackets: true
        });
        
    var cmeditor3 = CodeMirror.fromTextArea(document.getElementById("editor3-textarea"), {
            mode: {name: "r",
                   version: 3,
                   singleLineStringErrors: false},
            lineNumbers: true,
            indentUnit: 4,
            matchBrackets: true
        });
        
            $('.chat-container').hide();
            $('#cont1').show();

             $('.editor-input').hide();
            $('#editor1').show();
            
            cmeditor1.on('focus',function(){
                if( cmeditor1.getValue() == "Type text here" ) {
                    cmeditor1.setValue("");
                }
            });
            
            cmeditor2.on('focus',function(){
                if( cmeditor2.getValue() == "Type Python code here" ) {
                    cmeditor2.setValue("");
                }
            });
            
            cmeditor3.on('focus',function(){
                if( cmeditor3.getValue() == "Type R code here" ) {
                    cmeditor3.setValue("");
                }
            });
            
        MyProject.cmeditor1 = cmeditor1;
        MyProject.cmeditor2 = cmeditor2;
        MyProject.cmeditor3 = cmeditor3;
        
        console.log(cmeditor1.getValue());
        console.log(MyProject.cmeditor1.getValue());
                     
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
