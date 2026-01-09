const form = document.querySelector('.form')
const messagebox = document.querySelector('.message')
form.addEventListener('submit', async(e)=>{
    e.preventDefault();
     const data = {
        sepal_length: parseFloat(document.getElementById("sepal-length").value),
        sepal_width: parseFloat(document.getElementById("sepal-width").value),
        petal_length: parseFloat(document.getElementById("petal-length").value),
        petal_width: parseFloat(document.getElementById("petal-width").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify(data)
        })

        const apiResponse = await response.json();
        const {prediction}=apiResponse;
        messagebox.innerHTML=`Predicted Iris Species: <span>${prediction}</span>`;
    } catch (err) {
        console.log(err);
    }
})