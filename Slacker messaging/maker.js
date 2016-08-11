var makerURL ="https://maker.ifttt.com/trigger/send_msg/with/key/ccmdfLZEhyouzMefiVE28g";
function submitIt(){
	var message = $("#message").val();
	var img = $("#imgURL").val();

	var sendoff = {
		"value1" : message,
		"value2" : img,
	}
	$.post(makerURL,sendoff);
	$("#message").val("");
	$("#imgURL").val("");
}

