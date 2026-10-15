// // check js open or not
// alert()

function handleDiposit()
{
    var inputValue = document.getElementById("deposit-amount-input").value;
    console.log(inputValue);

    // convert string to num
    var convertInputvalue = convertTonumber(inputValue);

    var depositAmount = document.getElementById("deposit-amount-output").innerText
    console.log(depositAmount);

    // covert string to num
    var convertDepositamount = convertTonumber(depositAmount);

    // Checking num:
    console.log(convertInputvalue, convertDepositamount);

    var sum = convertInputvalue + convertDepositamount;
    console.log(sum);

    // After calculation num remove from deposit bar:
    document.getElementById("deposit-amount-input").value = "";








    // Working in total amount:
    // Set in deposit amount:
    document.getElementById("deposit-amount-output").innerText = sum;


    // Total amount input:
    var totalAmount = document.getElementById("total-amount-output").innerText;
    
    // Total amount convertion:
    var convertTotalamount = convertTonumber(totalAmount);
    var totalSum = convertInputvalue + convertTotalamount;

    // set in total amount:
    document.getElementById("total-amount-output").innerText = totalSum;
    








    // // After calculation num remove from deposit bar:
    // document.getElementById("deposit-amount-input").value = "";

}

function convertTonumber(value)
{
    return parseInt(value);
}



function handleWithdraw()
{
    var inputWithdraw = document.getElementById("withdraw-input").value;
    console.log(inputWithdraw);

    // converted string to num;
    var convertWithdrawtk = convertTonumber(inputWithdraw);
   
    var outputWithdraw = document.getElementById("withdraw-amount-output").innerText;
    console.log(outputWithdraw);

    var convertwithdrawoutput = convertTonumber(outputWithdraw);

    var sum = convertWithdrawtk + convertwithdrawoutput;
    console.log(sum);


    // set sum in deposit box:
    document.getElementById("withdraw-amount-output").innerText = sum;

    // Remove the bar of withdraw:
    document.getElementById("withdraw-input").value = "";






    // Working in total amount:
    // set in deposit amount:




    // Total amount input:
    var totalAmount = document.getElementById("total-amount-output").innerText;
    
    // Total amount convertion:
    var convertTotalamount = convertTonumber(totalAmount);

    var totalAmountafterWithdraw = convertTotalamount - convertWithdrawtk
    document.getElementById("total-amount-output").innerText = totalAmountafterWithdraw;




    // // Remove the bar of withdraw:
    // document.getElementById("withdraw-input").value = "";
}

