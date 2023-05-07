document.addEventListener('DOMContentLoaded', () => {
    const formPageLink = document.querySelector('#formPageLink');
    formPageLink.addEventListener('click', (event) => {
        event.preventDefault(); // prevent the link from triggering a page reload
        window.location.href = '/GrouPayEntry';
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const homePageLink = document.querySelector('#homePageLink');
    homePageLink.addEventListener('click', (event) => {
        event.preventDefault(); // prevent the link from triggering a page reload
        window.location.href = '/';
    });
});
