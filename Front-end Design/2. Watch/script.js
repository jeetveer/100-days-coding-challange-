const hours = document.querySelector("#hours");
const minutes = document.querySelector("#minutes");
const seconds = document.querySelector("#seconds");
const ampm = document.querySelector("#ampm")

setInterval(() => {
    const currentTime = new Date();
    const hour12 = () => {
        if (currentTime.getHours() > 12) {
            return currentTime.getHours() - 12;
        }
        else {
            return currentTime.getHours();
        }
    }

    hours.innerText = hour12();
    minutes.innerHTML = currentTime.getMinutes();
    seconds.innerText = currentTime.getSeconds();
    ampm.innerText = currentTime.getHours() >= 12 ? "PM" : "AM";

})
