document.getElementById('btn').addEventListener("click",function(){
    let user_name=document.getElementById("email").value
    let user_password=document.getElementById("password").value

})

const loginForm =document.querySelector(".login-form");

loginForm.addEventListener("submit",async(e)=>{
    e.preventDefault();



    const email =document.getElementById("email").value;
    const password =document.getElementById("password").value;
    // Data-vai oru Object-il vaikka
    const userData = {
        email: email,
        password: password
    };

    try {
        // FastAPI-kku POST request anuppa
        const response = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData) // Data-vai JSON string-a matha
        });

        const result = await response.json();

        if (response.ok) {
            alert("Login Success: " + result.message);
            // Inga neenga vera page-ku redirect pannalam (e.g., window.location.href = "/dashboard")
        } else {
            alert("Login Failed: " + result.detail);
        }
    } catch (error) {
        console.error("Error:", error);
    }



})