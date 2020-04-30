const form =
     'Name Quiz: <div class="form-group">' +
        '<input type="text" name="question">' +
     '</div>' +
     'Total Quiz: <div class="form-group">' +
        '<input type="text" name="question">' +
     '</div>' +
      '<div id="question1" class="question">' +
        '<form>' +
          '<div class="form-group">' +
            '<input type="text" name="number" class="numberctr" value="1" disabled>' +
          '</div>' +
          
          '<div class="form-group">' +
            'Question: <input type="text" name="question">' +
          '</div>' +
          '<div class="form-group">' +
            '<input type="radio" name="o1" value="Option 1"> <input type="text" name="question"> <br>' +
            '<input type="radio" name="o2" value="Option 2"> <input type="text" name="question"> <br>' +
            '<input type="radio" name="o3" value="Option 3"> <input type="text" name="question"> <br>' +
            '<input type="radio" name="o4" value="Option 4"> <input type="text" name="question">' +
          '</div>' +
          '<div class="form-group">' +
            'Answer: <input type="number" name="correct">' +
          '</div>' +
        '</form>' +
        '<div class="actions">' +
          '<button class="clone">Add</button>' +
          '<button class="remove">Remove</button>' +
        '</div>' +
      '</div>';

var regex = /^(question)(\d+)$/i;


function clone() {
  //$('#quiz').append(form);
  var cl = $(this).parents(".question").clone();
    
  cl.appendTo("#quiz");
  var cloneIndex = $(".question").length;
  
    cl.attr("id", "question" +  cloneIndex);
    
    cl.find('input.numberctr').attr("name", "number" + cloneIndex).val(cloneIndex);
  
    cl.on('click', 'button.clone', clone)
    cl.on('click', 'button.remove', remove);
}

function remove(){
  $(this).parents(".question").remove();
  $('.question').each(function(index, event){
    
    let cloneIndex = index + 1;
    console.log(cloneIndex);
    $(this).attr("id", "question" +  cloneIndex);
    $(this).find('input.numberctr').attr("name", "number" + cloneIndex).val(cloneIndex);
  });
}


function createQuestion () {
  $('#quiz').html(form);
  $('#createQuiz').hide();
  $("button.clone").on("click", clone);
  $("button.remove").on("click", remove);
}