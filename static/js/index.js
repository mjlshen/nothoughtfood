$(document).ready(function() {
	$('.mhacksLogo').click( function() {
		window.location='https://github.com/mjlshen/time2eat/';
	});
	$('.blogLink').click( function() {
		window.location='https://faiyafrower.blogspot.com/';
	});
	$('.breakLink').click( function() {
		window.location='/breakfast';
	});
	$('.lunchLink').click( function() {
		window.location='/lunch';
	});
	$('.dinnerLink').click( function() {
		window.location='/dinner';
	});
	$(".listRecipes").animate({'top': '+=30'}, 200);
	$("#infoButton").click( function() {
		$("#infoButton").animate({"right": "-=25"}, 500);
		$("#infoBox").animate({'right': '+=192'}, 500);
	});
	$(".closeBox").click( function() {
		$("#infoButton").animate({"right": "+=25"}, 500);
		$("#infoBox").animate({"right": "-=192"}, 500);
	});
});
