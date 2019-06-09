new Chart(document.getElementById("bug-upvotes"), {
    type: 'horizontalBar',
        
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            backgroundColor: '#700CBC',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    options: {
        legend: { display: false }
    }
});
    
new Chart(document.getElementById("feature-upvotes"), {
    type: 'horizontalBar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            backgroundColor: '#700CBC',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },
        
    options: {
        legend: { display: false }
    }
});
        
new Chart(document.getElementById("bug-status"), {
    type: 'pie',
    data: {
      labels: ["To Do", "In Progress", "Done", "Cancelled"],
      datasets: [{
        backgroundColor: ["#2E2FE3", "#700CBC","#AE0D7A","#5D1D3A"],
        borderColor: "#D4D4F7",
        data: [2478,5267,734,784]
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
      labels: ["To Do", "In Progress", "Done", "Cancelled"],
      datasets: [{
        backgroundColor: ["#2E2FE3", "#700CBC","#AE0D7A","#5D1D3A"],
        borderColor: "#D4D4F7",
        data: [2478,5267,734,784]
      }]
    },
    options: {
      title: {
        display: false
      }
    }
});
