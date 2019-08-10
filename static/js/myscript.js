$(document).ready(function(){
       $('select').formSelect();
       $('.collapsible').collapsible();
       $('.datepicker').datepicker();
       $('.timepicker').timepicker();
      });
      
      $('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year,
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,
        });
        
       $('.timepicker').pickatime({
            selectHours: true, // Creates a dropdown to control month
            selectMinutes: 60, // Creates a dropdown of 15 years to control year,
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,
        });
        
      
document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});