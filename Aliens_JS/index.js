var $tbody = document.querySelector('tbody');
var $dateInput = document.querySelector('#date');
var $searchBtn = document.querySelector('#search');

$searchBtn.addEventListener('click', handleSearchButtonClick);

var filteredReports = dataSet;

function renderTable() {
  $tbody.innerHTML = '';
  for (var i = 0; i < filteredReports.length; i++) {
    var report = filteredReports[i];
    var fields = Object.keys(report);
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = report[field];
    }
  }
}

function handleSearchButtonClick() {
  var filterState = $dateInput.value.trim().toLowerCase();

  filteredReports = dataSet.filter(function(report) {
    var addressState = report.datetime;

    return addressState === filterState;
  });
  renderTable();
}

renderTable();