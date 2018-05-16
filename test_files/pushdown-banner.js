function insertPushdownBanner(usersegmentname,pageurl,callback,callbackerror){

	var pushDownURL="/servlet/Satellite?pagename=SXM/Utility/PushdownBannerServiceWrapper&nonPIIsegmentName="+usersegmentname+"&pageURL="+pageurl;
		
	// var pushDownURL="/servlet/Satellite?pagename=SXM/Utility/PushdownBannerServiceWrapper&nonPIIsegmentName=Trailer"
		   $.ajax({
	             type: "GET",
	             cache: true,
	             url: pushDownURL,
	             dataType: "json",
	             success: callback,
	             error:   callbackerror
	         });

}

//Below is to test error scenarios. Provided wrong pagename

function insertPushdownBannerErrorTest(usersegmentname,pageurl,callback,callbackerror){

	var pushDownURL="/servlet/Satellite?pagename=SXM/Utility/PushdownBannerServiceWrapper1&nonPIIsegmentName="+usersegmentname+"&pageURL="+pageurl;
		
	// var pushDownURL="/servlet/Satellite?pagename=SXM/Utility/PushdownBannerServiceWrapper&nonPIIsegmentName=Trailer"
		   $.ajax({
	             type: "GET",
	             cache: true,
	             url: pushDownURL,
	             dataType: "json",
	             success: callback,
	             error:   callbackerror
	         });

}
