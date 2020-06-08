document.addEventListener('DOMContentLoaded', () => {
	var pasta_select=-1
	var salad_select=-1
	var dinnerplatter_select=-1
	var sub_select=-1
	var pizza_select=-1
	var pizza_type_select=-1
	var cartvis=1

	//subtotal calculator
	var cartitems=document.querySelectorAll(".cartitem")
	var subtotal=0
	for(i=0; i < cartitems.length; i++){
		subtotal = subtotal + parseFloat(cartitems[i].title)
	}
	let couponpercent=document.querySelector("#coupon").innerHTML
	if (couponpercent == 0){
		document.querySelector("#coupontext").hidden=true
	}
	if (subtotal >= 50){		
		document.querySelector("#subtotal").innerHTML=(subtotal*(1-couponpercent/100)).toFixed(2)
		document.querySelector("#remaining").innerHTML=""	
		document.querySelector("#percentoff").hidden=false	
		document.querySelector("#couponstatus").innerHTML="Coupon Applied!"
	}else{
		document.querySelector("#subtotal").innerHTML=subtotal.toFixed(2)
		let remaining=parseFloat(50-parseFloat(document.querySelector("#subtotal").innerHTML)).toFixed(2)
		document.querySelector("#remaining").innerHTML='$'+(remaining)
		document.querySelector("#percentoff").hidden=true
		document.querySelector("#couponstatus").innerHTML=" until Coupon applies" 
	}
	document.querySelector("#numitems").innerHTML=cartitems.length
	//cartvis
	document.querySelector('#cartvis').onclick = () => {
		if (cartvis == 0){
			document.querySelector('#shoppingcart').hidden=false
			document.querySelector('#cartvis').innerHTML="Hide Cart"
			cartvis=1
		}else{
			document.querySelector('#shoppingcart').hidden=true
			document.querySelector('#cartvis').innerHTML="Show Cart"
			cartvis=0
		}
	}	
	//pizza
	document.querySelector('#pizza').onclick = () => {
		pizza_select*=-1
		if (pizza_select==1){
			document.querySelector('#pizzadiv').hidden= false;
		}
		else{
			document.querySelector('#pizzadiv').hidden= true;
		}
	}


	//pizza type
	var pizzatypes = document.querySelectorAll(".pizzatype");
	for (i=0; i < pizzatypes.length; i++){
		if (document.addEventListener) {
			pizzatypes[i].addEventListener("click", function() {
				let buttonvalue=this.value;
				let ptypebuttons=document.querySelectorAll(".repizza");
				for (j=0;j<ptypebuttons.length; j++){
					if (ptypebuttons[j].title == buttonvalue){
						if (ptypebuttons[j].hidden){
	            			ptypebuttons[j].hidden= false;
	            		}else{
	            			ptypebuttons[j].hidden= true;
	            		}	            		
					}
				}
			})
		}
	}

	//pizza size - regular
	var pizzanames_reg = document.querySelectorAll(".repizza.Regular");
	for (i=0; i < pizzanames_reg.length; i++){
		if (document.addEventListener) {
			pizzanames_reg[i].addEventListener("click", function() {
				let buttonvalue=this.value;
				let sizebuttons=document.querySelectorAll(".rerepizza.Regular");
				for (j=0;j<sizebuttons.length; j++){
					if (sizebuttons[j].title == buttonvalue){
						if (sizebuttons[j].hidden){
            				sizebuttons[j].hidden= false;
            			}else{
            				sizebuttons[j].hidden= true;
            			}	         		
					}
				}
			})
		}
	}
	//pizza size - sci
	var pizzanames_sci = document.querySelectorAll(".repizza.Sicilian");
	for (i=0; i < pizzanames_sci.length; i++){
		if (document.addEventListener) {
			pizzanames_sci[i].addEventListener("click", function() {
				let buttonvalue=this.value;
				let sizebuttons=document.querySelectorAll(".rerepizza.Sicilian");
				for (j=0;j<sizebuttons.length; j++){
					if (sizebuttons[j].title == buttonvalue){
						if (sizebuttons[j].hidden){
            				sizebuttons[j].hidden= false;
            			}else{
            				sizebuttons[j].hidden= true;
            			}						         		
					}
				}
			})
		}
	}
	//pizza topping popup
	var pizzaclick= document.querySelectorAll(".rerepizza")
	var ntoppings=0
	var ntoppingsselected=0
	var ptoppings=document.querySelectorAll(".ptopping")
	for (i=0; i < pizzaclick.length; i++){
		if (document.addEventListener) {
			pizzaclick[i].addEventListener("click", function() {
				// populate form titles
				let buttonvalue=this
  				document.getElementById("myForm").style.display = "block";
  				//disable all buttons
  				let allbuttons=document.getElementsByTagName('button');
  				for (k=0; k < allbuttons.length; k++){
  					allbuttons[k].disabled=true
  				}
  				document.querySelector('#submitpizza').disabled=false
  				document.querySelector('#closebtn').disabled=false

				document.querySelector("#pizzainfo").innerHTML=buttonvalue.name+" "
				document.querySelector("#submitpizza").value=buttonvalue.value
				//reset checkboxes
				for (j=0; j < ptoppings.length; j++){
					ptoppings[j].checked=false
					ptoppings[j].disabled=false
				}	

				//set allowed number of toppings
				if (this.title == "Cheese"){
					ntoppings=0
				}else if(this.title == "Special"){
					ntoppings=5
				}else{
					ntoppings=this.title[0]
				}
				//disable if max
				if (ntoppings == ntoppingsselected){
					for (j=0; j < ptoppings.length; j++){
						if(ptoppings[j].checked == false){
							ptoppings[j].disabled = true;
						}
					}
				}else{
					document.querySelector('#submitpizza').disabled=true
				}
				//display topping counter
				document.querySelector("#toppingsremaining").innerHTML=0
				document.querySelector("#totaltoppings").innerHTML=ntoppings
			})
		}
	}
	// on click topping selection
	for (i=0; i < ptoppings.length; i++){
		if (document.addEventListener) {
			ptoppings[i].addEventListener("click", function() {
				//counter for number of toppings selected
				if (this.checked){
					ntoppingsselected+=1
				}else{
					ntoppingsselected-=1
				}
				//update counter
				document.querySelector("#toppingsremaining").innerHTML=ntoppingsselected
				document.querySelector("#totaltoppings").innerHTML=ntoppings

				//disable if max
				if (ntoppings == ntoppingsselected){
					document.querySelector('#submitpizza').disabled=false
					for (j=0; j < ptoppings.length; j++){
						if(ptoppings[j].checked == false){
							ptoppings[j].disabled = true;
						}
					}
				}else{
					document.querySelector('#submitpizza').disabled=true
					for (j=0; j < ptoppings.length; j++){
						ptoppings[j].disabled = false;
					}
				}
			})
		}
	}
	//close form button
	document.querySelector("#closebtn").onclick =() => {
		try{
			let allbuttons=document.getElementsByTagName('button');
				for (k=0; j < allbuttons.length; k++){
					allbuttons[k].disabled=false
				}
		}catch(err){
			console.log("")
		}
  		document.getElementById("myForm").style.display = "none";	
	}
	//sub
	document.querySelector('#sub').onclick = () => {
		sub_select*=-1
		if (sub_select==1){
			document.querySelector('#subdiv').hidden= false;
		}
		else{
			document.querySelector('#subdiv').hidden= true;
		}
	}
	//re sub
	var subbuttons = document.querySelectorAll(".resub");
	for (i=0; i < subbuttons.length; i++) {
	    if (document.addEventListener) {
	        subbuttons[i].addEventListener("click", function() {
	        	let buttonvalue=this.value;
	            let sizebuttons=document.querySelectorAll(".reresub");
	            for (j=0;j<sizebuttons.length; j++){
	            	if (sizebuttons[j].title == buttonvalue){
	            		if (sizebuttons[j].hidden){
	            			sizebuttons[j].hidden= false;
	            		}else{
	            			sizebuttons[j].hidden= true;
	            		}	            		
	            	}	            	
	            }
	        });
	    } 
	};
	//pasta
	document.querySelector('#pasta').onclick = () => {
		pasta_select*=-1
		if (pasta_select==1){
			document.querySelector('#pastadiv').hidden= false;
		}
		else{
			document.querySelector('#pastadiv').hidden= true;
		}
	}
	//salad
	document.querySelector('#salad').onclick = () => {
		salad_select*=-1
		if (salad_select==1){
			document.querySelector('#saladdiv').hidden= false;
		}
		else{
			document.querySelector('#saladdiv').hidden= true;
		}
	}
	//dp
	document.querySelector('#dinnerplatter').onclick = () => {
		dinnerplatter_select*=-1
		if (dinnerplatter_select==1){
			document.querySelector('#dinnerplatterdiv').hidden= false;
		}
		else{
			document.querySelector('#dinnerplatterdiv').hidden= true;
		}
	}
	//re dp
	var dpbuttons = document.querySelectorAll(".redp");
	for (i=0; i < dpbuttons.length; i++) {
	    if (document.addEventListener) {
	        dpbuttons[i].addEventListener("click", function() {
	        	let buttonvalue=this.value;
	            let sizebuttons=document.querySelectorAll(".reredp");
	            for (j=0;j<sizebuttons.length; j++){
	            	if (sizebuttons[j].title == buttonvalue){
	            		if (sizebuttons[j].hidden){
	            			sizebuttons[j].hidden= false;
	            		}else{
	            			sizebuttons[j].hidden= true;
	            		}	            		
	            	}	            	
	            }
	        });
	    } 
	};
	
})


