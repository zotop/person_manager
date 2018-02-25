function remove_person(personRow, personId) {
  $.ajax({
    url: '/api/persons/' + personId,
    type: 'DELETE',
    success: function(response){
      console.log(response);
      $(personRow).remove();
    },
    error: function(error){
      console.log(error);
      alert("Error: Could not remove person.");
    }
  });
}

function create_person_row(person) {
  var personRow = $("<tr person_id='" + person['id']+ "'><td>" +
  person['first_name']+ "</td><td>" + person['last_name'] + "</td>" +
  "<td><button>Delete</button></td>" + "</tr>");
  $(personRow).find('button').click(function(){
    remove_person(personRow, person['id']);
  });
  return personRow;
}


$(window).on( "load", function() {
   $.ajax({
			url: '/api/persons/list',
			type: 'GET',
			success: function(persons){
        $.each( persons, function( index, person ) {
          var personRow = create_person_row(person);
          $('#personsTable tbody').append(personRow);
        });
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not retrieve persons list.");
			}
		});
});

$(function(){
	$('#addPerson').click(function(){
		var firstName = $('#firstNameInput').val();
		var lastName = $('#lastNameInput').val();
		$.ajax({
			url: '/api/persons',
			data: JSON.stringify({'first_name': firstName, 'last_name': lastName}),
      contentType: "application/json",
			type: 'POST',
			success: function(person){
        console.log(person);
        var newPersonRow = create_person_row(person);
        $('#personsTable tbody').prepend(newPersonRow);
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not add person.");
			}
		});
	});
});
