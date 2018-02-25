$(function(){
	$('#addPerson').click(function(){
		var firstName = $('#firstNameInput').val();
		var lastName = $('#lastNameInput').val();
		$.ajax({
			url: '/api/persons',
			data: JSON.stringify({'first_name': firstName, 'last_name': lastName}),
      contentType: "application/json",
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not add person.");
			}
		});
	});
});
