function removePerson(personRow, personId) {
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

function showPersonPopup(personId) {
  $.ajax({
    url: '/api/persons/' + personId,
    type: 'GET',
    success: function(response){
      $("#personName").text(response['first_name'] + " " + response['last_name']);
      profilePicUrl = "static/images/blank-profile-picture.png";
      if (response['profile_picture_url']) {
        profilePicUrl = response['profile_picture_url'];
      }
      $("#personModal").find(".profile-pic").attr('src', profilePicUrl);
      $("#personModal").css("display", "block");
    },
    error: function(error){
      console.log(error);
      alert("Error: Could not retrieve person.");
    }
  });
}

function createPersonRow(person) {
  var personRow = $("<tr person_id='" + person['id']+ "'><td>" +
  person['first_name']+ "</td><td>" + person['last_name'] + "</td>" +
  "<td><button class='viewPerson'>View</button></td>" +
  "<td><button class='deletePerson'>Delete</button></td>" +
  "</tr>");
  $(personRow).find('.viewPerson').click(function(){
    showPersonPopup(person['id']);
  });
  $(personRow).find('.deletePerson').click(function(){
    removePerson(personRow, person['id']);
  });
  return personRow;
}

$(window).on( "load", function() {
   $.ajax({
			url: '/api/persons/list',
			type: 'GET',
			success: function(persons){
        $.each( persons, function( index, person ) {
          var personRow = createPersonRow(person);
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
        var newPersonRow = createPersonRow(person);
        $('#personsTable tbody').prepend(newPersonRow);
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not add person.");
			}
		});
	});
});


$(function(){
	$('#importRandomPerson').click(function(){
		$.ajax({
			url: '/api/persons/import/random',
			type: 'POST',
			success: function(person){
        console.log(person);
        var newPersonRow = createPersonRow(person);
        $('#personsTable tbody').prepend(newPersonRow);
			},
			error: function(error){
				console.log(error);
        alert("Error: Could not import random person.");
			}
		});
	});
});

$(function(){
	$('#closePersonModal').click(function(){
		$("#personModal").css("display", "none");
	});
});
