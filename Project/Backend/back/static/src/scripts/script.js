//Меню навигации
const navMenu = document.querySelector('.nav__icon-block');
const navIcon = document.querySelector('.nav__icon');
const navLinks = document.querySelectorAll('.popup__link');
const popupMenu = document.querySelector('.nav__popup');
if(navMenu){
    navMenu.addEventListener("click", function(e) {
        navIcon.classList.toggle('_active');
        popupMenu.classList.toggle('_active');
    });
}
navLinks.forEach(navLinks => {
    navLinks.addEventListener("click", function(e){
        navIcon.classList.remove('_active');
        popupMenu.classList.remove('_active');
    });
});
const nav = document.querySelector('.nav');
window.addEventListener("scroll", function(){
    let concept = this.document.querySelector('.concept');
    let conceptTop = concept.getBoundingClientRect().top;
    nav.classList.toggle("_sticky", conceptTop <= 0);
    if(!(nav.classList.contains('_sticky'))){
        navIcon.classList.remove('_active');
        popupMenu.classList.remove('_active');
    }
});
//Меню навигации кейса
window.addEventListener("scroll", function(){
    let company = this.document.querySelector('.company');
    let companyTop = company.getBoundingClientRect().top;
    nav.classList.toggle("_sticky", companyTop <= 0);
    if(!(nav.classList.contains('_sticky'))){
        navIcon.classList.remove('_active');
        popupMenu.classList.remove('_active');
    }
});






