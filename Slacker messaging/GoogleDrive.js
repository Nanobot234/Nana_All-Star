var makerURL = "https://maker.ifttt.com/trigger/write_docs/with/key/ccmdfLZEhyouzMefiVE28g";
function submitIt(){
	var title  = $("#Yourtitle").val();
	var doc = $("#Whatuwanttosay").val();

	var sendoff = {
		"value1" : title,
		"value2" : doc,
	}
	$.post(makerURL,sendoff);
	$("#Yourtitle").val("");
	$("#Whatuwanttosay").val("");
}
