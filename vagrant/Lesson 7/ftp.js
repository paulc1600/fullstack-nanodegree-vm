function Login(form) {
    var username = form.username.value;
    var password = form.password.value;
    var server = form.server.value;
    var local = form.local.value;
    if (username && password && server && local) {
            window.open(local, '_blank', 
              'toolbar=yes,location=yes,status=yes,' + 
              'scrollbars=auto,copyhistory=no,menubar=no,width=' 
              + ((screen.AvailWidth/2)-12) + ',height=' + 
              (screen.AvailHeight-124) +',left=0,top=0,resizable=yes');
            window.open("ftp://" + username + ":" + 
              password + "@" + server, '_blank', 
              'toolbar=yes,location=yes,status=yes,' + 
              'scrollbars=auto,copyhistory=no,menubar=no,width=' 
              + ((screen.AvailWidth/2)-12) + ',height=' 
              + (screen.AvailHeight-124) +',left=' + ((screen.AvailWidth/2)) 
              + '),top=0,resizable=yes');
            }
        else {
            alert("NO BLANK FIELDS!");
            }
    }
