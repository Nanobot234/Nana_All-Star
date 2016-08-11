function grabData(){
	//ajax data from random api
	$.ajax({	
		url:'https://randomuser.me/api/',
		dataType: 'json',
		success:function(data){
			//when array is succesful, the results are given back in the screen
			print(data);
		}
		
	})
 
}
 function print(obj)
{
	//removes previous content  displayed in web browser
	$('#content').text('');
	//iterate through objects stored in result and print to screen
	for(var i in obj)	

	{
		if(i == "info"){
		
		$('#content').append('<p>' + i + ':' + obj[i] + '<p>');
	}
		if(i == "results"){
		$('#content').append('<p>' + i + ':' + obj[i] + '<p>');
		}
	}
	}


 $('#submit').click(function()
{
	grabData();
})
