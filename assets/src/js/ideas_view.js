
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
    // Does this cookie string begin with the name we want?
    if (cookie.substring(0, name.length + 1) === (name + '=')) {
    	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    	break;
    }
}
}
return cookieValue;
}
$(document).ready(function() {

            $('[data-action="vote"]').on('click', function() {
                var vote = $(this).attr('data-value')
                var $this = $(this)

                $.ajax({
                    url: "{% url 'ideas:vote' idea.id %}",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    data: {
                        'vote': vote
                    },
                    dataType: 'json',
                    method: 'POST',
                    success: function(res) {
                        let clas = res.class
                        let message = res.message
                        if (clas == 'error') {
                            toastr.error(message)
                        } else {
                            toastr.success(message)
                        }
                        if (res.status && res.status == 'Removed') {

                            $this.children('i').css('color', 'grey')
                            $this.children('i').animate({fontSize: '3em'})
                            $this.children('i').animate({fontSize: '2em'})

                        } else if (vote == 'D') {
                            $this.children('i').css('color', 'tomato')
                            $this.children('i').animate({fontSize: '3em'})
                            $this.children('i').animate({fontSize: '2em'})
                            
                        } else {
                            $this.children('i').css('color', 'blue')
                            $this.children('i').animate({fontSize: '3em'})
                            $this.children('i').animate({fontSize: '2em'})
                        }
                    },
                    error: function(res) {
                        toastr.error("An Error Occured")
                    }
                })
            })

        });