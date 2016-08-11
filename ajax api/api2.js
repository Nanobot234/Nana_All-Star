function grabData(){
		var name = $('title').val();
	
	$.ajax({	
		url:'http:www.omdbapi.com/?t=' + title,
		success:function(result){
			//when array is succesful, the results are given back in the screen
			print_result(result);
		}
		
	})
 
}
 function print_result(obj)
{
	//removes previous content  displayed in web browser
	$('#content').text('');
	//iterate through objects stored in result and print to screen
	for(var i in obj)
	{
		$('#content').append('<p>' + i + ':' + obj[i] + '<p>');
	}
}

$('#submit').click(function()
{
	grabData();
})
