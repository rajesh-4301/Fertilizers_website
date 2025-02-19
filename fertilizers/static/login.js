let input1 = document.getElementById("password");
let input2 = document.getElementById("confPassword");
let loginPassword = document.getElementById("loginPassword");

function checkPassword(){
if (input1.value !== input2.value){
   alert("Check your confirmation password");
}
else{
window.location.assign("login/");
}
}
function loginPasswordValue(){

if (loginPassword.value===""){
    alert("Give your password");
}
}
function termsConditions(){
   let newLine = "\n\n";
   let terms = "1.Introduction: \n \t By using Fertilizers.com, you agree to these terms and conditions. Please review them carefully.";
   terms += newLine;
   terms += "2.Products and Pricing: \n \t Products and prices are subject to change without notice. We strive for accuracy but are not liable for errors.";
   terms += newLine;
   terms += "3. Shipping and Delivery \n \t We aim to deliver your order promptly. Delivery times are estimates and can vary. We are not responsible for delays caused by shipping carriers.";
   terms += newLine;
   terms += "4. Returns and Refunds \n \t Returns must be made within 7 days of receipt. Items must be in their original condition. Please refer to our return policy on the website for details.";
   terms += newLine;
   terms += "5.Limitation of Liability \n \t Fertilizers.com is not liable for any indirect or consequential damages related to your use of our site or products.";
   terms += newLine;
   terms += "6.Governing Law \n \t These terms are governed by the laws of India. Disputes will be handled in the courts of Fertilizers.com."
   alert(terms);
}


function toggleFavorite(heart) {
   heart.classList.toggle('selected');
}
function toggleSidebar() {
   const sidebar = document.getElementById("mobileSidebar");
   const overlay = document.getElementById("overlay");
   const isActive = sidebar.classList.contains("active");

   sidebar.classList.toggle("active", !isActive);
   overlay.classList.toggle("active", !isActive);
}

document.querySelectorAll('.has-submenu > a').forEach(menu => {
   menu.addEventListener('click', function (e) {
       e.preventDefault(); 
       this.parentElement.classList.toggle('active');
   });
});

const sizeButtons = document.querySelectorAll('.size-options button');
sizeButtons.forEach(button => {
   button.addEventListener('click', () => {
       sizeButtons.forEach(btn => btn.classList.remove('selected'));
       button.classList.add('selected');
   });
});

function toggleFavorite(heart) {
   heart.classList.toggle('selected');
} 
function toggleSidebar() {
   const sidebar = document.getElementById("mobileSidebar");
   const overlay = document.getElementById("overlay");
   const isActive = sidebar.classList.contains("active");

   if (isActive) {
       sidebar.classList.remove("active");
       overlay.classList.remove("active");
   } else {
       sidebar.classList.add("active");
       overlay.classList.add("active");
   }
}
document.querySelectorAll('.has-submenu > a').forEach((menu) => {
   menu.addEventListener('click', function (e) {
       e.preventDefault(); 
       const parent = this.parentElement;
       parent.classList.toggle('active');
   });
});

function toggleSidebar() {
   var sidebar = document.getElementById("sidebar");
   var overlay = document.getElementById("overlay");
   sidebar.classList.toggle("show");
   overlay.classList.toggle("show");
 }

document.getElementById("overlay").addEventListener("click", toggleSidebar);

    // JavaScript to toggle sidebar on mobile
const hamburger = document.getElementById('hamburger');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

hamburger.addEventListener('click', () => {
  sidebar.classList.toggle('show');
  overlay.classList.toggle('show');
});

overlay.addEventListener('click', () => {
  sidebar.classList.remove('show');
  overlay.classList.remove('show');
});

function toggleSidebar() {
   var sidebar = document.getElementById("sidebar");
   var overlay = document.getElementById("overlay");
   sidebar.classList.toggle("show");
   overlay.classList.toggle("show");
 }

 document.getElementById("overlay").addEventListener("click", toggleSidebar);

 terms += newLine;
   terms += "7.NO PAYMENT GATEWAY \n \t Tis website is just developed to showcase our skills, it has no payment gateways."