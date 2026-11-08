// // check js open or not
// alert()

function handleDiposit()
{
    // convert string to num
    var convertInputvalue = getConvertedValue("deposit-amount-input", "value");

    // convert string to num
    var convertDepositamount = getConvertedValue("deposit-amount-output", "innerText");

    // Checking num:
    console.log(convertInputvalue, convertDepositamount);

    var sum = convertInputvalue + convertDepositamount;
    console.log(sum);

    // After calculation num remove from deposit bar:
    document.getElementById("deposit-amount-input").value = "";




    // Working in total amount:
    // set innertext
    setInnertext(deposit-amount-output, sum);


    var totalAmount = document.getElementById("total-amount-output").innerText;
    
    // Total amount convertion:
    var convertTotalamount = getConvertedValue("total-amount-output", "innerText");
    var totalSum = convertInputvalue + convertTotalamount;

    
    // Set innertext:
    setInnertext(total-amount-output, totalSum);

}




function getConvertedValue(id, element)
{
    var value = document.getElementById(id).element;
    return parseInt(value);
}



function handleWithdraw()
{
    // converted string to num;
    var convertWithdrawtk = getConvertedValue("withdraw-input", "value");

    var convertwithdrawoutput = getConvertedValue("withdraw-amount-output", "innerText");

    var sum = convertWithdrawtk + convertwithdrawoutput;
    console.log(sum);

    // set innertext:
    setInnertext(withdraw-amount-output, sum);


    // Remove the bar of withdraw:
    document.getElementById("withdraw-input").value = "";






    // Working in total amount:

    // Total amount convertion:
    var convertTotalamount = getConvertedValue("total-amount-output", "innerText");

    var totalAmountafterWithdraw = convertTotalamount - convertWithdrawtk
    
 
    // set innertext:
    setInnertext(total-amount-output, totalAmountafterWithdraw);

}


// short format for code of innerText:
function setInnertext(id, value)
{
    document.getElementById(id).innerText = value;
}

