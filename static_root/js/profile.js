/*var Person = function(name,age,email){
  this.name = name;
  this.age = age;
  this.email = email;
}

var gurpreet = new Person("Gurpreet",18,"gurprit96kaur@gmail.com");
var manpreet = new Person("Manpreet",20,"manpreet.gulati17@gmail.com");

var myName = $("span.name");
var mylink = $("span.links");

myName.html(manpreet.name + ", " + manpreet.age);

mylink.html(manpreet.email);*/


//Tabs Layout Code
$("#tabs").tabs({
    activate: function (event, ui) {
        var active = $('#tabs').tabs('option', 'active');
        $("#tabid").html('the tab id is ' + $("#tabs ul>li a").eq(active).attr("href"));
    }
});
