
function getOS() {
    var userAgent = window.navigator.userAgent,
        platform = window.navigator.platform,
        macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
        windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
        iosPlatforms = ['iPhone', 'iPad', 'iPod'],
        os = null;

    if (macosPlatforms.indexOf(platform) !== -1) {
        os = 'Mac OS';
    } else if (iosPlatforms.indexOf(platform) !== -1) {
        os = 'iOS';
    } else if (windowsPlatforms.indexOf(platform) !== -1) {
        os = 'Windows';
    } else if (/Android/.test(userAgent)) {
        os = 'Android';
    } else if (!os && /Linux/.test(platform)) {
        os = 'Linux';
    }

    return os;
}
function find() {
    if (getOS() == "Android") {
        Swal.fire({
            title: 'Sweet!',
            text: 'andriod',
            imageUrl: '~/cards/img/mohammad.gif',
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'profile name',

        })
    }
    else if (getOS() == "iOS") {
        Swal.fire({
            title: 'Sweet!',
            text: 'ios',
            imageUrl: '~/cards/img/mohammad.gif',
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'profile name',

        })
    }
    else if (getOS() == "Mac OS") {
        Swal.fire({
            title: 'Sweet!',
            text: 'Mac OS',
            imageUrl: '~/cards/img/mohammad.gif',
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'profile name',

        })
    }
    else if (getOS() == "Linux") {
        Swal.fire({
            title: 'Sweet!',
            text: 'Linux',
            imageUrl: '~/cards/img/mohammad.gif',
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'profile name',

        })
    }
    else if (getOS() == "Windows") {
        Swal.fire({
            title: 'Sweet!',
            text: 'Windows',
            imageUrl: '~/cards/img/mohammad.gif',
            imageWidth: 400,
            imageHeight: 200,
            imageAlt: 'profile name',

        })
    }
}

 
    var map = L.map('map').setView([36.5773, 52.6757], 16);

                    L.tileLayer('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'mohammad rahimaee -09363793192'
                    }).addTo(map);
                    L.marker([36.5773, 52.6757], 16).addTo(map).bindPopup('mohammad reza rahimaee -09363793192')
  

function getget() {
    Swal.fire({
        title: 'هویت کاربر',
        text: 'تایید شده توسط سایت',
        imageUrl: 'cards/img/ok.gif',
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'کاربر تایید شده',

    })
}