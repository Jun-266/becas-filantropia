document.addEventListener('DOMContentLoaded', () => {
    
    const body = document.querySelector("body");
    const sidebar = document.querySelector("nav");
    const toggle = document.querySelector(".toggle");
    const searchBtn = document.querySelector(".search-box");
    const modeSwitch = document.querySelector(".toggle-switch");
    const modeText = document.querySelector(".mode-text");


    toggle.addEventListener("click", ()=> {
        sidebar.classList.toggle("close");
    })

    searchBtn.addEventListener("click",()=>{
        sidebar.classList.remove("close");
    })

    modeSwitch.addEventListener("click", ()=>{

        body.classList.toggle("dark");
        if (body.classList.contains("dark")) {
            modeText.innerText = "Light mode"
        } else {
            modeText.innerText = "Dark mode"
        }
    })
})


/*
    document.addEventListener('DOMContentLoaded', () => {

    let listElements = document.querySelectorAll('.list__button--click');
    listElements.forEach(listElement => {
        listElement.addEventListener('click', () => {

            listElement.classList.toggle('arrow');

            let height = 0;
            let menu = listElement.nextElementSibling;
            
            if(menu.clientHeight == "0"){
                height=menu.scrollHeight;
            }
            menu.style.height = `${height}px`;
        });
    });

    
});
*/