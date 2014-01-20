$(document).ready(function() {
	document.form.inputAnagrams.focus();
	$('.mhacksLogo').click( function() {
		window.location='http://www.mhacks.org/';
	});
	$(".listAnagrams").animate({'top': '+=30'}, 200);
	$("#infoButton").click( function() {
		$("#infoButton").animate({"right": "-=25"}, 500);
		$("#infoBox").animate({'right': '+=192'}, 500);
	});
	$(".closeBox").click( function() {
		$("#infoButton").animate({"right": "+=25"}, 500);
		$("#infoBox").animate({"right": "-=192"}, 500);
	});
	$("#otherMeal").click( function() {
		$("#mealChoice").animate({"top": "+=100"}, 500);
	});
});
