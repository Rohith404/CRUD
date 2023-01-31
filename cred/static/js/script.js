$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

$('#btn').click(() => {

        var username = $('#username').val()
        var password = $('#password').val()

        var data = {
            'csrfmiddlewaretoken':'{{ csrf_token }}',
            'username':username,
            'password':password, 
        }

        if(username == ''){
            alert('Enter an username')
        }else if(password == ''){
            alert('Enter an password')
        }
    })