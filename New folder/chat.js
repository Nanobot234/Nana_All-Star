var database= firebase.database().ref();
//Funtion to send the message u write			
function sendMessage(){
	var firstName = $("#first").val();
	var lastName = $("#last").val();
	//var yourComment = $('#comment').val();


	//success:function(result){
			//when array is succesful, the results are given back in the screen
	//		print_result(result);
	//	}

	//send to your database
	database.push({
	'firstName':firstName,
	'lastName':lastName
	//'yourComment':yourComment
	});
}
	
  
	function getData(){
	}
   database.on('child_added',function(dataRow){
        	var row=dataRow.val();
        	$("#database_msg").append("<p>" + "first Name:" + row.firstName + "<p></p>" + "last Name:" + row.lastName);// + "</p>");
    })
}
    
