const fs = require('fs');
const path = require('path');
// const prompt = require("prompt-sync")();
// let projectName = prompt("Enter your project name (default: piyushai): ") || "piyushai";
//npm install prompt-sync------terminal me 
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter your project name (default: piyushai): ", (projectName) => {

    projectName = projectName.trim() || "piyushai";

const baseDir = path.join(__dirname, projectName);
console.log(`🚀 ${projectName} website ka structure aur code generate ho raha hai...`);

// 1. Saare Folders create karna
const folders = ['css', 'js', 'gs', 'assets/images/icons', 'assets/fonts'];
folders.forEach(folder => {
    fs.mkdirSync(path.join(baseDir, folder), { recursive: true });
});

// 2. Saari Empty Files create karna
const filesToCreate = {
    '': [
        'index.html',
        'login.html',
        'signup.html',
        'forgot-password.html',
        'verify-otp.html',
        'reset-password.html',

        'home.html',
        'shop.html',
        'product.html',
        'category.html',
        'search.html',

        'cart.html',
        'wishlist.html',
        'checkout.html',
        'payment.html',
        'payment-success.html',
        'payment-failed.html',

        'orders.html',
        'order-details.html',
        'track-order.html',

        'profile.html',
        'edit-profile.html',
        'address.html',
        'add-address.html',

        'notifications.html',
        'messages.html',

        'settings.html',
        'change-password.html',

        'contact.html',
        'about.html',
        'privacy-policy.html',
        'terms.html',
        'faq.html',
        '404.html',

        'README.md'
    ],

    'css': [
        'style.css',
        'variables.css',
        'reset.css',
        'layout.css',
        'navbar.css',
        'footer.css',

        'home.css',
        'login.css',
        'signup.css',
        'shop.css',
        'product.css',
        'category.css',
        'search.css',

        'cart.css',
        'wishlist.css',
        'checkout.css',
        'payment.css',

        'orders.css',
        'track-order.css',

        'profile.css',
        'address.css',
        'settings.css',

        'messages.css',
        'notifications.css',

        'slider.css',
        'buttons.css',
        'forms.css',
        'modal.css',
        'toast.css',
        'loader.css',
        'responsive.css'
    ],

    'js': [
        'config.js',
        'api.js',
        'utils.js',

        'auth.js',
        'login.js',
        'signup.js',
        'forgot-password.js',
        'verify-otp.js',

        'home.js',
        'shop.js',
        'product.js',
        'category.js',
        'search.js',

        'cart.js',
        'wishlist.js',

        'checkout.js',
        'payment.js',

        'orders.js',
        'track-order.js',

        'profile.js',
        'address.js',
        'settings.js',

        'messages.js',
        'notifications.js',

        'slider.js',
        'theme.js',
        'toast.js',
        'loader.js',

        'firebase.js',
        'session.js'
    ],

    'assets/images': [
        'logo.png',
        'favicon.png',

        'banner1.jpg',
        'banner2.jpg',
        'banner3.jpg',

        'default-product.png',
        'avatar.png',

        'empty-cart.png',
        'no-product.png',
        'payment-success.png',
        'payment-failed.png'
    ],

    'assets/images/icons': [
        'home.svg',
        'shop.svg',
        'cart.svg',
        'wishlist.svg',
        'user.svg',
        'search.svg',
        'notification.svg',
        'message.svg',
        'settings.svg',
        'logout.svg',
        'back.svg',
        'menu.svg',
        'close.svg',
        'plus.svg',
        'minus.svg',
        'edit.svg',
        'delete.svg',
        'location.svg',
        'phone.svg',
        'email.svg',
        'star.svg',
        'heart.svg',
        'share.svg'
    ],

    'assets/fonts': [
        'README.txt'
    ]
};

for (const [folder, files] of Object.entries(filesToCreate)) {
    files.forEach(file => {
        fs.writeFileSync(path.join(baseDir, folder, file), `/* ${file} */\n`);
    });
}

// ===============================
// HTML FILES
// ===============================
//index.html
const indexHtmlContent = `
`;
//login.html
const loginHtmlContent = `
`;
//signup.html
const signupHtmlContent = ``;
const homeHtmlContent = `
`;
//shop.html
const shopHtmlContent = ``;
//product.html
const productHtmlContent = `
`;
//category.html
const categoryHtmlContent = ``;
//search.html
const searchHtmlContent = ``;
//cart.html
const cartHtmlContent = ``;
//wishlist.html
const wishlistHtmlContent = ``;
//checkout.html
const checkoutHtmlContent = ``;
//payment.html
const paymentHtmlContent = ``;
//payment-success.html
const paymentSuccessHtmlContent = ``;
//payment-failed.html
const paymentFailedHtmlContent = ``;
//orders.html
const ordersHtmlContent = ``;
//order-details.html
const orderDetailsHtmlContent = ``;
//track-order.html
const trackOrderHtmlContent = ``;
//profile.html
const profileHtmlContent = ``;
//edit-profile.html
const editProfileHtmlContent = ``;
//address.html
const addressHtmlContent = ``;
//add-address.html
const addAddressHtmlContent = ``;
//messages.html
const messagesHtmlContent = ``;
//notifications.html
const notificationsHtmlContent = ``;
//settings.html
const settingsHtmlContent = ``;
//change-password.html
const changePasswordHtmlContent = ``;
//forgot-password.html
const forgotPasswordHtmlContent = ``;
//verify-otp.html
const verifyOtpHtmlContent = ``;
//reset-password.html
const resetPasswordHtmlContent = ``;
//contact.html
const contactHtmlContent = ``;
//about.html
const aboutHtmlContent = ``;
//faq.html
const faqHtmlContent = ``;
//privacy-policy.html
const privacyHtmlContent = ``;
//terms.html
const termsHtmlContent = ``;
//help.html
const helpHtmlContent = ``;
//support.html
const supportHtmlContent = ``;

// ===============================
// CSS FILES
// ===============================

const styleCssContent = ``;
const resetCssContent = ``;
const variablesCssContent = ``;
const layoutCssContent = ``;
const navbarCssContent = ``;
const footerCssContent = ``;
const homeCssContent = ``;
const loginCssContent = ``;
const signupCssContent = ``;
const shopCssContent = ``;
const productCssContent = ``;
const categoryCssContent = ``;
const searchCssContent = ``;
const cartCssContent = ``;
const wishlistCssContent = ``;
const checkoutCssContent = ``;
const paymentCssContent = ``;
const ordersCssContent = ``;
const trackOrderCssContent = ``;
const profileCssContent = ``;
const addressCssContent = ``;
const settingsCssContent = ``;
const messagesCssContent = ``;
const notificationsCssContent = ``;
const responsiveCssContent = ``;

// ===============================
// JS FILES
// ===============================

const loginJsContent = ``;
const signupJsContent = ``;
const homeJsContent = ``;
const shopJsContent = ``;
const productJsContent = ``;
const categoryJsContent = ``;
const searchJsContent = ``;
const cartJsContent = ``;
const wishlistJsContent = ``;
const checkoutJsContent = ``;
const paymentJsContent = ``;
const ordersJsContent = ``;
const trackOrderJsContent = ``;
const profileJsContent = ``;
const addressJsContent = ``;
const settingsJsContent = ``;
const messagesJsContent = ``;
const notificationsJsContent = ``;
const firebaseJsContent = ``;
const utilsJsContent = ``;
const themeJsContent = ``;
const loaderJsContent = ``;
const toastJsContent = ``;
const sliderJsContent = ``;
const sessionJsContent = ``;

// Missing core JS content variables
const configJsContent = ``;
const apiJsContent = ``;
const authJsContent = ``;

// ===============================
// GOOGLE APPS SCRIPT
// ===============================

const codeGsContent = ``;
const authGsContent = ``;
const productGsContent = ``;
const orderGsContent = ``;
const paymentGsContent = ``;
const userGsContent = ``;
const messageGsContent = ``;
const reviewGsContent = ``;
const notificationGsContent = ``;
const couponGsContent = ``;

// ===============================
// WRITE FILES
// ===============================

fs.writeFileSync(path.join(baseDir, "index.html"), indexHtmlContent);
fs.writeFileSync(path.join(baseDir, "login.html"), loginHtmlContent);
fs.writeFileSync(path.join(baseDir, "signup.html"), signupHtmlContent);
fs.writeFileSync(path.join(baseDir, "home.html"), homeHtmlContent);
fs.writeFileSync(path.join(baseDir, "shop.html"), shopHtmlContent);
fs.writeFileSync(path.join(baseDir, "product.html"), productHtmlContent);
fs.writeFileSync(path.join(baseDir, "category.html"), categoryHtmlContent);
fs.writeFileSync(path.join(baseDir, "search.html"), searchHtmlContent);
fs.writeFileSync(path.join(baseDir, "cart.html"), cartHtmlContent);
fs.writeFileSync(path.join(baseDir, "wishlist.html"), wishlistHtmlContent);
fs.writeFileSync(path.join(baseDir, "checkout.html"), checkoutHtmlContent);
fs.writeFileSync(path.join(baseDir, "payment.html"), paymentHtmlContent);
fs.writeFileSync(path.join(baseDir, "payment-success.html"), paymentSuccessHtmlContent);
fs.writeFileSync(path.join(baseDir, "payment-failed.html"), paymentFailedHtmlContent);
fs.writeFileSync(path.join(baseDir, "orders.html"), ordersHtmlContent);
fs.writeFileSync(path.join(baseDir, "order-details.html"), orderDetailsHtmlContent);
fs.writeFileSync(path.join(baseDir, "track-order.html"), trackOrderHtmlContent);
fs.writeFileSync(path.join(baseDir, "profile.html"), profileHtmlContent);
fs.writeFileSync(path.join(baseDir, "edit-profile.html"), editProfileHtmlContent);
fs.writeFileSync(path.join(baseDir, "address.html"), addressHtmlContent);
fs.writeFileSync(path.join(baseDir, "add-address.html"), addAddressHtmlContent);
fs.writeFileSync(path.join(baseDir, "messages.html"), messagesHtmlContent);
fs.writeFileSync(path.join(baseDir, "notifications.html"), notificationsHtmlContent);
fs.writeFileSync(path.join(baseDir, "settings.html"), settingsHtmlContent);
fs.writeFileSync(path.join(baseDir, "change-password.html"), changePasswordHtmlContent);
fs.writeFileSync(path.join(baseDir, "forgot-password.html"), forgotPasswordHtmlContent);
fs.writeFileSync(path.join(baseDir, "verify-otp.html"), verifyOtpHtmlContent);
fs.writeFileSync(path.join(baseDir, "reset-password.html"), resetPasswordHtmlContent);
fs.writeFileSync(path.join(baseDir, "contact.html"), contactHtmlContent);
fs.writeFileSync(path.join(baseDir, "about.html"), aboutHtmlContent);
fs.writeFileSync(path.join(baseDir, "faq.html"), faqHtmlContent);
fs.writeFileSync(path.join(baseDir, "privacy-policy.html"), privacyHtmlContent);
fs.writeFileSync(path.join(baseDir, "terms.html"), termsHtmlContent);
fs.writeFileSync(path.join(baseDir, "help.html"), helpHtmlContent);
fs.writeFileSync(path.join(baseDir, "support.html"), supportHtmlContent);

fs.writeFileSync(path.join(baseDir, "css", "style.css"), styleCssContent);
fs.writeFileSync(path.join(baseDir, "css", "variables.css"), variablesCssContent);
fs.writeFileSync(path.join(baseDir, "css", "reset.css"), resetCssContent);
fs.writeFileSync(path.join(baseDir, "css", "layout.css"), layoutCssContent);
fs.writeFileSync(path.join(baseDir, "css", "navbar.css"), navbarCssContent);
fs.writeFileSync(path.join(baseDir, "css", "footer.css"), footerCssContent);
fs.writeFileSync(path.join(baseDir, "css", "home.css"), homeCssContent);
fs.writeFileSync(path.join(baseDir, "css", "login.css"), loginCssContent);
fs.writeFileSync(path.join(baseDir, "css", "signup.css"), signupCssContent);
fs.writeFileSync(path.join(baseDir, "css", "shop.css"), shopCssContent);
fs.writeFileSync(path.join(baseDir, "css", "product.css"), productCssContent);
fs.writeFileSync(path.join(baseDir, "css", "category.css"), categoryCssContent);
fs.writeFileSync(path.join(baseDir, "css", "search.css"), searchCssContent);
fs.writeFileSync(path.join(baseDir, "css", "cart.css"), cartCssContent);
fs.writeFileSync(path.join(baseDir, "css", "wishlist.css"), wishlistCssContent);
fs.writeFileSync(path.join(baseDir, "css", "checkout.css"), checkoutCssContent);
fs.writeFileSync(path.join(baseDir, "css", "payment.css"), paymentCssContent);
fs.writeFileSync(path.join(baseDir, "css", "orders.css"), ordersCssContent);
fs.writeFileSync(path.join(baseDir, "css", "track-order.css"), trackOrderCssContent);
fs.writeFileSync(path.join(baseDir, "css", "profile.css"), profileCssContent);
fs.writeFileSync(path.join(baseDir, "css", "address.css"), addressCssContent);
fs.writeFileSync(path.join(baseDir, "css", "settings.css"), settingsCssContent);
fs.writeFileSync(path.join(baseDir, "css", "messages.css"), messagesCssContent);
fs.writeFileSync(path.join(baseDir, "css", "notifications.css"), notificationsCssContent);
fs.writeFileSync(path.join(baseDir, "css", "responsive.css"), responsiveCssContent);

fs.writeFileSync(path.join(baseDir, "js", "config.js"), configJsContent);
fs.writeFileSync(path.join(baseDir, "js", "api.js"), apiJsContent);
fs.writeFileSync(path.join(baseDir, "js", "auth.js"), authJsContent);
fs.writeFileSync(path.join(baseDir, "js", "utils.js"), utilsJsContent);
fs.writeFileSync(path.join(baseDir, "js", "login.js"), loginJsContent);
fs.writeFileSync(path.join(baseDir, "js", "signup.js"), signupJsContent);
fs.writeFileSync(path.join(baseDir, "js", "home.js"), homeJsContent);
fs.writeFileSync(path.join(baseDir, "js", "shop.js"), shopJsContent);
fs.writeFileSync(path.join(baseDir, "js", "product.js"), productJsContent);
fs.writeFileSync(path.join(baseDir, "js", "category.js"), categoryJsContent);
fs.writeFileSync(path.join(baseDir, "js", "search.js"), searchJsContent);
fs.writeFileSync(path.join(baseDir, "js", "cart.js"), cartJsContent);
fs.writeFileSync(path.join(baseDir, "js", "wishlist.js"), wishlistJsContent);
fs.writeFileSync(path.join(baseDir, "js", "checkout.js"), checkoutJsContent);
fs.writeFileSync(path.join(baseDir, "js", "payment.js"), paymentJsContent);
fs.writeFileSync(path.join(baseDir, "js", "orders.js"), ordersJsContent);
fs.writeFileSync(path.join(baseDir, "js", "track-order.js"), trackOrderJsContent);
fs.writeFileSync(path.join(baseDir, "js", "profile.js"), profileJsContent);
fs.writeFileSync(path.join(baseDir, "js", "address.js"), addressJsContent);
fs.writeFileSync(path.join(baseDir, "js", "settings.js"), settingsJsContent);
fs.writeFileSync(path.join(baseDir, "js", "messages.js"), messagesJsContent);
fs.writeFileSync(path.join(baseDir, "js", "notifications.js"), notificationsJsContent);
fs.writeFileSync(path.join(baseDir, "js", "firebase.js"), firebaseJsContent);
fs.writeFileSync(path.join(baseDir, "js", "theme.js"), themeJsContent);
fs.writeFileSync(path.join(baseDir, "js", "loader.js"), loaderJsContent);
fs.writeFileSync(path.join(baseDir, "js", "toast.js"), toastJsContent);
fs.writeFileSync(path.join(baseDir, "js", "slider.js"), sliderJsContent);
fs.writeFileSync(path.join(baseDir, "js", "session.js"), sessionJsContent);

fs.writeFileSync(path.join(baseDir, "gs", "Code.gs"), codeGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Auth.gs"), authGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Product.gs"), productGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Order.gs"), orderGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Payment.gs"), paymentGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "User.gs"), userGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Message.gs"), messageGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Review.gs"), reviewGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Notification.gs"), notificationGsContent);
fs.writeFileSync(path.join(baseDir, "gs", "Coupon.gs"), couponGsContent);

console.log('✅ 35 HTML files created successfully!');
console.log('✅ 25 CSS files created successfully!');
console.log('✅ 28 JS files created successfully!');
console.log('✅ 10 Google Apps Script (GS) backend files created successfully!');

console.log(`\n✅ Success! ${projectName} project - HTML, CSS, JS aur GS backend code sab kuch save ho gaya hai.`);
rl.close();

});