// Responsive code for mobile


console.log(screen.width)
if(screen.width<=400){
    document.getElementsByClassName("container")[0].classList.remove("Player")
    tab1.style.width = '100%'
    tab1.style.height = '50%'
    tab2.style.width = '0%'
    tab2.style.height = '0%'

    btn2.style.visibility = "hidden"
    sItem.style.height = "75vh"  
}