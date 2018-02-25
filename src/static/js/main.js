$(window).on( "load", function() {
   $.ajax({
			url: '/api/persons/list',
			type: 'GET',
			success: function(persons){
        $.each( persons, function( index, person ) {
          personRow = "<tr><td>" + person['first_name']+ "</td><td>" + person['last_name'] + "</td></tr>";
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
        newPersonRow = "<tr><td>" + person['first_name']+ "</td><td>" + person['last_name'] + "</td></tr>";
        $('#personsTable tbody').prepend(newPersonRow);
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not add person.");
			}
		});
	});
});
