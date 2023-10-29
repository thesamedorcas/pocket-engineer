
chrome.webNavigation.onCompleted.addListener(function(details) {
    
    console.log("Visited website: " + details.url);

    
   });