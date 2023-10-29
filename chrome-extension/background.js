
let payments_word = [
    "payment",
    "checkout",
    "pricing",
    "pay",
    "cart"
   ]
   
   
   chrome.webNavigation.onCompleted.addListener(function(details) {
    console.log("Visited website: " + details.url);
   
   
    for(let i = 0; i < payments_word.length; i++){
     if(url.includes(payments_word[i])){
   
      const url = details.url;
      const requestData = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url , email : "test@test.com" }),
      };
    
      fetch('http://127.0.0.1:5000/add_points', requestData)
        .then(response => {
          if (response.ok) {
            console.log('Website URL sent to logger ');
          } else {
            console.error('Failed to send website URL to logger ');
          }
        })
        .catch(error => {
          console.error('Error sending the request:', error);
        });
         
   
         break;
     }
   }
   
   });
   
   