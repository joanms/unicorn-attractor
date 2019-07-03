// The Ajax code is based on Anthony Bonello's project: https://github.com/abonello/project_5/blob/master/static/js/my_charts.js

$.ajax({
  type: "GET",
  url: "get_chart_data",
  dataType: "json",
  async: true,

  success: function (data) {
    var bug_titles = [];
    var bug_upvotes = [];
    var feature_titles = [];
    var feature_upvotes = [];
    var bug_status = [];
    var bug_quantity = [];
    var feature_status = [];
    var feature_quantity = [];

    $.each(data.message.bugs, function (i, content) {
      bug_titles.push(content.title);
      bug_upvotes.push(content.votes);
      bug_status.push(content.comments);
      bug_quantity.push(content.comments);
    });

    $.each(data.message.features, function (i, content) {
      feature_titles.push(content.title);
      feature_upvotes.push(content.votes);
      feature_status.push(content.comments);
      feature_quantity.push(content.comments);
    });

    new Chart(document.getElementById("bug-upvotes"), {
      type: 'horizontalBar',

      data: {
        labels: bug_titles,
        datasets: [{
          backgroundColor: '#700CBC',
          data: bug_upvotes
        }]
      },

      options: {
        legend: { display: false }
      }
    });

    new Chart(document.getElementById("feature-upvotes"), {
      type: 'horizontalBar',
      data: {
        labels: feature_titles,
        datasets: [{
          backgroundColor: '#700CBC',
          data: feature_upvotes
        }]
      },

      options: {
        legend: { display: false }
      }
    });

    new Chart(document.getElementById("bug-status"), {
      type: 'pie',
      data: {
        labels: bug_status,
        datasets: [{
          backgroundColor: ["#2E2FE3", "#700CBC", "#AE0D7A", "#5D1D3A"],
          borderColor: "#D4D4F7",
          data: bug_quantity
        }]
      },
      options: {
        title: {
          display: false
        }
      }
    });

    new Chart(document.getElementById("feature-status"), {
      type: 'pie',
      data: {
        labels: feature_status,
        datasets: [{
          backgroundColor: ["#2E2FE3", "#700CBC", "#AE0D7A", "#5D1D3A"],
          borderColor: "#D4D4F7",
          data: feature_quantity
        }]
      },
      options: {
        title: {
          display: false
        }
      }
    });
