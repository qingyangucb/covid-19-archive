var date;
var counties;

function getData() {
	date = document.getElementById("date").value;
  counties = document.getElementById("counties").value;
  // console.log(date);
  // console.log(counties);
  var url = 'getData/' + date + '/' + counties;
  // console.log(url);
  d3.json(url).then(function(results) {
      console.log(results);
    })
}

