$(document).ready(function() {
	document.form.inputTime.focus();
	$('.mhacksLogo').click( function() {
		window.location='https://github.com/mjlshen/time2eat';
	});
	$('.blogLink').click( function() {
		window.location='https://faiyafrower.blogspot.com/';
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
	$("#otherMeal").click( function() {
		$("#mealChoice").animate({"top": "+=80"}, 500);
	});
	$("#mealChoice").click( function() {
		$("#mealChoice").animate({"top": "-=80"}, 500);
	});
});
