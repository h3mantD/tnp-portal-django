function check() {
    var user = document.forms["form1"]["user"].value;
    var passw = document.form1.pass.value;
    if (user == "") {
        alert("USERNAME is empty");
        return false;
    }
    else {
        if (passw == "") {
            alert("Enter the Password");
            document.getElementById("e_msg").innerHTML = "Enter The Password";
            return false;
        }
        else {
            if (passw.length == 8) {
                var hasBigAlpha = false;
                var hasSmallAlpha = false;
                var hasDigit = false;
                var hasSpecialChar = false;

                for (var i = 0; i < passw.length; i++) {
                    var c = pass.charAt(i);
                    if (c > 47 && c < 58)
                        hasDigit = true;
                    if (c > 64 && c < 91)
                        hasBigAlpha = true;
                    if (c > 96 && c < 123)
                        hasSmallAlpha = true;
                    if (c > 32 && c < 48)
                        hasSpecialChar = true;
                }

                if (hasBigAlpha && hasSmallAlpha && hasSpecialChar && hasDigit) {
                    alert("Successfull Logged in");
                    return true;
                }
                else {
                    alert("Password pattern missmatch");
                    document.getElementById("e_msg").innerHTML = "Invalid Password";
                    return false;
                }
            }
            else {
                alert("Invalid Password");
                document.getElementById("e_msg").innerHTML = "Invalid Password";
                return false;
            }
        }
    }
    return true;
}

function checking_val() {
    var fname = document.getElementsByName("fname");
    var hasBigAlpha = false;
    var hasSmallAlpha = false;
    var hasDigit = false;
    var hasSpecialChar = false;
    for(var i=0; i<fname.length; i++) {
        var c = pass.charAt(i);
        if (c > 64 && c < 91)
            hasBigAlpha = true;
        if (c > 96 && c < 123)
            hasSmallAlpha = true;
    }
    if(hasBigAlpha && hasSmallAlpha) {

    }
    else {
        alert("Enter the your name properly!!!!!!!");
        return false;
    }

    
}