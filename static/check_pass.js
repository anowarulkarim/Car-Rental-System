function checkpass()
{
    var i=0;
    var password= document.getElementById
    ("password").value;
    var confirm_password= document.getElementById
    ("confirm_password").value;
    var pno= document.getElementById
    ("phone_no").value;
    var G= document.getElementById
    ("gender").value;
        if(password!=confirm_password )
        {
            alert("pass dont match ");
            return false;
        }
        if(password.length < 8 )
        {
            alert("password is too short ");
            return false;
        }
        if(pno.length !== 11)
        {
            alert("phone no must be 11 digit ");
            return false;
        }
        if(G == 'M' || G == 'F')
        {i=1 }
        if(i==1)
        {
            return true;
        }
        else
        {
            alert("gender must be M or F ");
            return false;
        }
}