function searchrecords()
{
    var input,table,tr,td,filter,i,txtdata;
    input=document.getElementById("searchtxt");
    filter= input.value.toUpperCase();
    table=document.getElementByID("table1");
    tr=table.getElementById("tr");
    for(i=0;i<tr.length;i++)
    {
        td=tr[i].getElementByTagName("td")[0];
        if(td)
        {
            txtdata=td.innerText;
            if(txtdata.toUppercase().indexOf(filter)>-1)
            {
                tr[i].style.display="";
            }
            else
            {
                tr[i].style.display="None";
            }
        }
    }
}