  function mydelete(id) { //댓글 삭제
         var deleteform = document.getElementById(id);
         deleteform.style.display = 'block';
         var btn_id='c'+id;
       var deletebtn=document.getElementById(btn_id);
       deletebtn.style.display='none';
    }
    
    var init=false;
    function edit() { //댓글 등록
         var d = document.getElementById('comment');
       if(init == false) {
          d.contents.value='';
          init = true;
       }
      } 
