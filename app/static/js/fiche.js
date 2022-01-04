
var button = document.getElementsByClassName('demo')
for (i = 0; i<button.length; i++){
    button[i].addEventListener('click',function(){
        var produit = this.dataset.produit
        var action = this.dataset.action
        console.log("produit_id",produit , "action",action)

        console.log('User:',user)
        if(user == 'AnonymousUser'){
            console.log("User is not authenticated")
        }else{
            updateUser(produit, action)
        }
    })
}

function updateUser(produit, action) {
    console.log('User is connected ......')

    var url = '/updateItem/'

    fetch(url,{
        method: 'POST',
        headers:{
            'content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'produit':produit, 'action': action})
        
    })
    .then((response) =>{
        return response.json()

    })
    .then((data) =>{
        console.log('data :', data)
        location.reload()
    })
}
