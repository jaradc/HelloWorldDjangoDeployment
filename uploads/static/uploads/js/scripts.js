
window.onload = function () {
    const message = document.querySelector(".system-message");
    if (message){
        setTimeout(() => message.remove(), 3000);
    }
};
