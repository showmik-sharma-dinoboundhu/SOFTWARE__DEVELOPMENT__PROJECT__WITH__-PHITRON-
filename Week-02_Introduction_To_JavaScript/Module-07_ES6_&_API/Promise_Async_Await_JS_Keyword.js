const getData = new Promise(function(resolve, reject)
{
    return resolve(20);
    return reject("40 no data found");
});

console.log(getData);
getData
    .then(data => console.log(data))
    .catch((err) => console.log(err));