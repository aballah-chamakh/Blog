$(document).ready(function(){

var comment_section = $('#comment_section')
var btn_like = $('.btnff_liffke')
console.log(comment_section);
btn_like.click(function(event){
  console.log(event);
})
$.ajax({
  url : 'http://127.0.0.1:8000/comment/',
  method : 'get' ,
  success : function(data){
    data.map(function(obj){
   comment_section.append("<li>"+obj.content+"<li/><br/><button class='btn_like' id="+obj.id+" >"+obj.id+"</button>")
    })

  } ,
  error : function(res){
console.log(res);
  },
})
















  // alert('hello world ya m3alem')
  // var create_comment_btn = $('comment_create')
  // var toogle_like_btn = $('toogle_like')
  // var delete_btn = $('delete_btn')
  // var comment_content = $('comment_content')
  // create_comment_btn.click(fuction(event){
  //   '<button id=comment_id ><button/>'
  // })
})
